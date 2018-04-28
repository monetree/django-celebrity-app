from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Register
from .forms import SignupForm


# def register_view(request):
#     signup_form = SignupForm(request.POST or None)
#     context = {
#         "form": signup_form 
#     }
#     if signup_form.is_valid():
#         print(signup_form.cleaned_data)
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         login_ip = request.META['REMOTE_ADDR']
#         context = {
#             'error' : 'registration failed'
#         }
#         obj = Register(username=username,email=email,password=password,login_ip=login_ip)
#         if obj:
#             obj.save()
#             return HttpResponseRedirect('/index')
#         else:
#             return HttpResponseRedirect('/register',context)

#     return render(request,'register.html',{'form':signup_form})

def register_view(request):
    signup_form = SignupForm(request.POST or None)
    context = {
            "form" : signup_form
        }
    if request.method == 'POST':
        if signup_form.is_valid():
            username         = signup_form.cleaned_data['username']
            email            = signup_form.cleaned_data['email']
            password         = signup_form.cleaned_data['password']
            conform_password = signup_form.cleaned_data['conform_password']
            if len(password) <= 5:
                print('password is too short')
                return HttpResponseRedirect('/register',context)
            elif password != conform_password:           
                print('password should match')
                return HttpResponseRedirect('/register',context)

            login_ip         = request.META['REMOTE_ADDR']
            obj              = Register(username=username,email=email,password=password,login_ip=login_ip)
            obj.save()
            return HttpResponseRedirect('/index',context)
    return render(request,'register.html',context)




