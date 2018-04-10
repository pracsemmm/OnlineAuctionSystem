from django.shortcuts import render
from first_app.forms import UserForm,UserProfileInfoForm,ProductForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from .models import Product,Customer_Bid


def input_bid_value(request):
    print("came here")
    if request.method == 'POST':
        bid_value=request.POST.get('bid_value')
        product_id = request.POST.get('hidden_id')
        username = user
        product = Product.objects.get(pk=product_id)
        cb = Customer_Bid(customer=user,product=product,bid=bid_value)
        cb.save()
        print('bid added')
        return HttpResponseRedirect(reverse('first_app:seller_dashbord'))




def index(request):
    all_products = Product.objects.all()
    return render(request,'first_app/index.html',{'all_products':all_products})
def user_signup(request):
    registered=False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()
            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()
    return render(request,'first_app/signup.html',
                            {'user_form':user_form,'profile_form':profile_form,'registered':registered})

def seller_signup(request):
    registered=False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()
            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()
    return render(request,'first_app/seller_signup.html',
                            {'user_form':user_form,'profile_form':profile_form,'registered':registered})



@login_required
def product_adder_page(request):
    registered=False
    if request.method == 'POST':
        product_form = ProductForm(data=request.POST)
        if product_form.is_valid():
            product=product_form.save(commit=False)
            product.save()
            registered=True
        else:
            print(product_form.errors)
    else:
        product_form=ProductForm()
    return render(request,'first_app/product_adder_page.html',
                            {'product_form':product_form,'registered':registered})





def seller_dashbord(request):
    return render(request,'first_app/seller_dashbord.html')

def customer_dashbord(request):
    return render(request,'first_app/customer_dashbord.html')
def user_login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)#authenticate automatically
        if user:
            if user.is_active:
                login(request,user)#if user is active then login the user
                return HttpResponseRedirect(reverse('first_app:customer_dashbord'))#reverse to home page
            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried to login and failed")
            print("Username: {} and Password: {}".format(username,password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request,'first_app/login.html')


def seller_login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)#authenticate automatically
        if user:
            if user.is_active:
                login(request,user)#if user is active then login the user
                return HttpResponseRedirect(reverse('first_app:seller_dashbord'))#reverse to home page
            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried to login and failed")
            print("Username: {} and Password: {}".format(username,password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request,'first_app/seller_login.html',{})

@login_required
def special(request):
    return HttpResponse('You are logged IN Nice!')
@login_required
def seller_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('first_app:index'))

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('first_app:index'))

@login_required
def product_add(request):
    product_form = ProductForm()
    return render(request,'',{'product_form':product_form})
