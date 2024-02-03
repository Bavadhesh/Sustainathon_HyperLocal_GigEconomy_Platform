function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        console.log("Geolocation is not supported by this browser.");
    }
}

function showPosition(position) {
    // Get latitude and longitude
    var lat = position.coords.latitude;
    var long = position.coords.longitude;

    // Set the values in the form
    document.getElementById('latitude').value = lat;
    document.getElementById('longitude').value = long;
    document.getElementById('geo').innerHTML="Ok";
}