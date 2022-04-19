from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book, Cart, Customer
from .forms import CreateUserForm, CreateCustomerForm, CreateBookForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    books = Book.objects.all()
    context = {'books': books}
    # if request.user.is_staff:
        # return redirect(to='/admin/', args=context)
    # else:
    return render(request, 'book/home.html', context)


def logoutPage(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                print("working")
                login(request,user)
                return redirect('/')
        context={}
    #    return render(request,'book/login.html',context

        # context = {}
        return render(request, 'book/login.html', context)

def registerPage(request):
    if request.methods == 'POST':
        form = CreateUserForm(request.POST)
        customer_form = CreateCustomerForm(request.POST)
        if form.is_valid() and customer_form.is_valid():
            user = form.save()
            customer = customer_form.save(commit=False)
            customer.user = user 
            customer.save()
        
    else:
        form = CreateUserForm()
        customer_form = CreateCustomerForm()
    context = {
        'form': form,
        'customer_form': customer_form
    }
    return render(request, 'book/register.html', context)

def addbook(request):
    if request.method=='POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = CreateBookForm()

    context = {
        'form': form
    }

    return render(request, 'book/addbook.html', context)

@login_required
def viewcart(request):
    cust = Customer.objects.filter(user=request.user)
    for c in cust:
        carts = Cart.objects.all()
        for cart in carts:
            if (cart.customer==c):
                context = {
                    'cart': cart 
                }
                return render(request, 'book/viewcart.html', context)
            else:
                return render(request, 'book/emptycart.html')

    return redirect('/')


def addtocart(request, pk):
    book = Book.objects.get(id=pk)
    customers = Customer.objects.filter(user=request.user)

    for customer in customers:
        carts = Cart.objects.all()
        reqcart = ''

        for cart in carts:
            if (cart.customer==customer):
                reqcart = cart
                break
        if reqcart=='':
            reqcart = Cart.objects.create(customer=customer)
        reqcart.books.add(book)

    return redirect('/')

               
        
