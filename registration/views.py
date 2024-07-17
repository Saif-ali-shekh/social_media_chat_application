
from django.http import HttpResponse
from registration.models import Custom_User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import random
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login




def email_send(fname, email):
    otp1 = random.randint(100000, 999999)
    subject = "Welcome to Artistry ChatHub ||"
    message = f"Hello {fname} ||\nWelcome to Artistry ChatHub website, Please confirm your email address to activate account\n\nYour OTP is: {otp1}"
    from_email = settings.EMAIL_HOST_USER 
    to_list = [email]
    send_mail(subject, message, from_email, to_list, fail_silently=True)
    return otp1

def otpcheck(request):
    if request.method == "POST":
        try:
            get_otp = int(request.POST['get_otp'])
            gen_otp = request.session.get('gen_otp')
            if  get_otp != gen_otp:
                 otp_error = 'The provided OTP does not match. Please double-check and try again.'

                 return render(request, 'otpcheck.html',{'otp_error':otp_error})
        except:
            return render(request, 'otpcheck.html', {'otp_error': 'Invalid OTP. Please enter a valid number.'})
        
        first_name = request.session.get('first_name')
        print(first_name)
        last_name = request.session.get('last_name')
        username = request.session.get('username')
        email = request.session.get('email')
        password = request.session.get('password') 
        user = Custom_User.objects.create(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
        return render(request, 'login.html')
    return render(request, 'otpcheck.html')




#Register
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Checking  if username or email already exists
        if Custom_User.objects.filter(username=username).exists():
            username_error ="Username already exists. Please choose a different one."
            return render(request, 'registration.html',{'username_error':username_error})
        if Custom_User.objects.filter(email=email).exists():
            username_error ="Username already exists. Please choose a different one."
            print("exist")
            return render(request, 'registration.html')
        
        gen_otp = email_send(first_name, email)
        request.session['gen_otp'] = gen_otp
        request.session['first_name'] =first_name
        request.session['last_name'] = last_name
        request.session['username'] = username
        request.session['email'] = email
        request.session['password'] = password
        return redirect('otpcheck')
        


    return render(request, 'registration.html')


# views.py
def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
         user = Custom_User.objects.get(email=email,password=password)
         print(user)
        # user = authenticate(request, username=email, password=password)
         if user is not None:
            login(request, user)
            return redirect('chatpage')  
         else:
            msg1 = "Invalid username or password. Please try again."
            return render(request, 'login.html', {'msg1': msg1})
        except:
            msg1 = "Invalid username or password. Please try again."
            return render(request, 'login.html', {'msg1': msg1})
    
    return render(request, 'login.html')

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User


@login_required(login_url='user_login')
def chatPage(request, *args, **kwargs):
    print("chatpage")
    first_name = None  
    if request.user.is_authenticated:  
        first_name = request.user.first_name  
        print(first_name)

    context = {'first_name': first_name} 
    return render(request, "chat/chatPage.html", context)



def logout_user(request):
    logout(request)
    
    return redirect('user_login')
