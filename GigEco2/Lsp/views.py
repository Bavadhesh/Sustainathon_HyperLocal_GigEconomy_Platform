from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .models import ServiceProvider,RequestBox,Booklogs
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth.models import User

def login_view(request):
    if request.user.is_authenticated:
         return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home')  # Redirect to the home page or any desired page after successful login
        else:
            messages.error(request, 'Login failed. Please check your username and password.')

    return render(request, 'Lsp/login.html')

def home_view(request):
    if request.user.is_authenticated :
           profile = get_object_or_404(ServiceProvider,user=request.user)
           return render(request,'Lsp/home.html',{"profile":profile})
    else:
         return redirect('login')

def changeAvailable(request,status):
    if request.user.is_authenticated :
           profile = get_object_or_404(ServiceProvider,user=request.user)
           if status == 1:
               profile.available = True
           else:
                profile.available = False
           profile.save()
           return redirect('home')
    else:
         return redirect('login')
    
def requestBox(request):
     if request.user.is_authenticated :
           obj = RequestBox.objects.filter(user=request.user).order_by('date', 'time')

           return render(request,'Lsp/requestBox.html',{"requests":obj})

     else:
         return redirect('login')



def send_email(request,id):
    if request.user.is_authenticated:
        user = get_object_or_404(ServiceProvider,user=request.user)
        
        customer = get_object_or_404(RequestBox,id=id)
        subject = 'Request accepted'
        message = 'Hello, '+customer.customerName + '\n' + user.Name +' accepted your request' + '\n' + 'Service Provider will be availbale at ' + ' ' + str(customer.date) + ' ' + str(customer.time)
        from_email = 'friday191103@gmail.com'
        recipient_list = [customer.customerEmail,]

        send_mail(subject, message, from_email, recipient_list)
        customer.accepted = True
        Booklogs.objects.create(user=request.user,customerName=customer.customerName,customerPhone=customer.customerPhone,customerAddress=customer.customerAddress,
                                        customerEmail=customer.customerEmail,date=customer.date,time=customer.time)
        customer.delete()

        return redirect("reqbox")

def send_decline_email(request,id):

    if request.user.is_authenticated:
        user = get_object_or_404(ServiceProvider,user=request.user)
        customer = get_object_or_404(RequestBox,id=id)
        subject = 'Request declined'
        message = 'Hello,'+customer.customerName + '\n' +'Your request made on' + ' ' + str(customer.date) + ' '+ str(customer.time) + '  has been declined by  '+user.Name+' '+'(Service provider)'
        from_email = 'friday191103@gmail.com'
        recipient_list = [customer.customerEmail,]

        send_mail(subject, message, from_email, recipient_list)
        
        
        customer.delete()

        return redirect("reqbox")

def signout(request):
     if request.user.is_authenticated:
          logout(request)
          return redirect('login')
     return redirect('login')

# your_app_name/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            # Passwords do not match, handle accordingly (e.g., return an error message)
            return render(request, 'Lsp/signup.html', {'error_message': 'Passwords do not match.'})

        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)

        # Authenticate and log in the user
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('profile')  # Replace 'home' with the name or path of your home page

    return render(request, 'Lsp/signup.html')

# views.py

from django.contrib.auth.decorators import login_required

@login_required
def create_service_provider(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        contact_no = request.POST.get('contact_no')
        whatsapp_no = request.POST.get('whatsapp_no')
        email = request.POST.get('email')
        lat = request.POST.get('lat')
        long = request.POST.get('long')
        
        # Handle file upload separately
        profile_photo = request.FILES.get('profile_photo')

        # Check if all required fields are present
        
        service_provider = ServiceProvider(
            user=request.user,
            Name=name,
            category=category,
            contactno=contact_no,
            Whatsappno=whatsapp_no,
            email=email,
            lat=lat,
            long=long,
            profilePhoto=profile_photo
        )
        service_provider.save()
        messages.success(request, 'Service provider created successfully.')
        return redirect('home')  # Redirect to a success page or any other page
        
    
    return render(request, 'Lsp/Lspreg.html')

# views.py
from django.shortcuts import render
from .models import Booklogs
from django.contrib.auth.decorators import login_required

@login_required
def book_log(request):
    # Query Booklogs based on the logged-in user
    book_logs = Booklogs.objects.filter(user=request.user)

    context = {
        'book_logs': book_logs
    }

    return render(request, 'Lsp/booklogs.html', context)
