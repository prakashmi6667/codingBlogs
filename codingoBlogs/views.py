from django.shortcuts import render, redirect, reverse
from blogs.models import Customer
# Create your views here.
def session_Required(function):
    def wrap(request, *args, **kwargs):
        if request.session.has_key('LoggedInCustomer'):
            return function(request, *args, **kwargs)
        else:
            return redirect(reverse('login'))
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def login(request):
    try:
        __context = {}
        if request.method == 'POST':
            objCustomer = Customer.objects.values('id', 'name', 'email').filter(
                email=request.POST['email'], password=request.POST['password'])
            if len(objCustomer) > 0:
                request.session['LoggedInCustomer'] = objCustomer[0]
                return redirect(reverse('blogs'))
            else:
                __context['error'] = 'Invalid email and password!'
        
        
        return render(request, 'login.html',__context)
    except Exception as error:
        return render(request,'error.html',{"error":error})

def signup(request):
    try:
        __context = {}
        if request.method == 'POST':
            obj = Customer.objects.create(
                    name=request.POST['name'],
                    email=request.POST['email'],
                    password=request.POST['password'],
                    mobile_no=request.POST['mobile'])
            
            objCustomer =  Customer.objects.values('id', 'name', 'email').filter(id=obj.id)
            if len(objCustomer) > 0:
                request.session['LoggedInCustomer'] = objCustomer[0]
                return redirect(reverse('blogs'))
            else:
                __context['error'] = 'Invalid email and password!'

        return render(request, 'signup.html',__context)
    except Exception as error:
        return render(request,'error.html',{"error":error})

def logout(request):
    try:
        __context = {}
        del request.session['LoggedInCustomer']
        return redirect(reverse('login'))
    except Exception as ex:
        return render(request, 'Franchise_404.html', {'error': ex})