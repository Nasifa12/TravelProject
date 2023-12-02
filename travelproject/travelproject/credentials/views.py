from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password1']
        Cpassword = request.POST['password2']
        user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                        last_name=last_name, email=email)
        user.save();
        print("user created")
    return render(request, "register.html")
