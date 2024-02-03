from django.shortcuts import render,redirect,get_object_or_404
from Lsp.models import ServiceProvider,RequestBox
from django.http import JsonResponse

# Create your views here.
from django.contrib.gis.measure import Distance, D
from geopy.distance import distance
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from Lsp.forms import RequestForm

def getServiceProvider(request):
     if request.method == "POST":
        skill = request.POST["skill"]
        lat = float(request.POST["lat"])
        long = float(request.POST["long"])
        
        list = []
        final = []
        for sp in ServiceProvider.objects.filter(category=skill,available=True).values():
            sp["Distance"] = int(distance((lat,long),(sp["lat"],sp["long"])).kilometers)
            list.append(sp)
        list.sort(key=lambda x: x["Distance"])
        for i in list:
            if i["Distance"] < 10:
                final.append(i)
        return render(request,'customer\listing2.html',{"list":final,"Category":skill})
     else:
         return render(request,'customer\search.html')
     
# views.py


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return redirect('signup')

        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
            return redirect('signup')

        # Check if the email is already registered
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered.')
            return redirect('signup')

        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password1)

        # Additional logic (e.g., send confirmation email)

        messages.success(request, 'Account created successfully. You can now log in.')
        return redirect('loginUser')  # Redirect to the login page after successful registration

    return render(request, "customer/register.html")


def availability(request,id):
    provider = get_object_or_404(ServiceProvider,id=id)
    return JsonResponse({"id":id,"status":provider.available})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home')  # Redirect to the home page or any desired page after successful login
        else:
            messages.error(request, 'Login failed. Please check your username and password.')
            return HttpResponse("Not found")
    else :
        return render(request,'customer/login.html')

def Request(request,id):
    if request.method == "POST":
         customerName = request.POST["customerName"]
         customerPhone = request.POST["customerPhone"]
         customerAddress = request.POST["customerAddress"]
         customerEmail = request.POST["customerEmail"]
         date = request.POST["date"]
         time = request.POST["time"]
         id = request.POST["id"]
         user = get_object_or_404(User,id=id)
         obj = RequestBox.objects.create(user=user,customerName=customerName,customerPhone=customerPhone,customerAddress=customerAddress,
                                        customerEmail=customerEmail,date=date,time=time)
         return redirect('list')

    else:
        
        return render(request,"customer/request.html",{"id":id})
