from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from .models import *
import random
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.db.models import Q
from django.contrib.sessions.backends.db import SessionStore


# Create your views here.

def master(request): 
    categories = Categories.objects.all().order_by('name')
    subcategories = Subcategories.objects.all()    
    context = {        
        'cate' : categories ,
        'sub':subcategories,
    }
    return render(request, "Master/master.html",context)

sign=Signup()
def signup(request):
    if request.method=="POST":        
        sign.firstname=request.POST['firstname']
        sign.lastname=request.POST['lastname']
        sign.email=request.POST['email']        
        sign.phone=request.POST['phone'] 
        sign.password=request.POST['password']                   
       
        if Signup.objects.filter(email=sign.email).exists():            
            return JsonResponse({'opstatus':'Error'})
        else:                   
            otp = ''
            rand = random.choice('0123456789')
            rand1 = random.choice('0123456789')
            rand2 = random.choice('0123456789')
            rand3 = random.choice('0123456789')
            otp = rand + rand1 + rand2 + rand3 

            request.session['otp'] = otp                  
            subject = 'Email Verification'
            message = otp
            email_from= settings.EMAIL_HOST_USER
            recipient_list = [sign.email]
            send_mail( subject, message, email_from, recipient_list )                                             
            return JsonResponse({'opstatus':'Success'})
    categories = Categories.objects.all().order_by('name')
    subcategories = Subcategories.objects.all()    
    context = {        
        'cate' : categories ,
        'sub':subcategories,
    }
    return render(request, "UserLog/signup.html",context)

def signupAuthentication(request):
    if request.session.has_key('otp'):
        otp = request.session['otp'] 
        print(otp)
        try:
            otpobj = request.POST.get('otp')   
            print(otpobj)
            if otp == otpobj:
                print('wait')
                sign.save()
                print('save')
                return JsonResponse({'opstatus':'Success'})                                                              
        except:            
            return redirect('signupAuthentication')
    return render(request,'UserLog/SignupAuthentication.html')

def signin(request):
    if request.method=="POST":
        try:
            e=request.POST['email'] 
            request.session['email']=e            
            p=request.POST['password']                       
            x=Signup.objects.get(email=e)                         
            if x.password==p:
                # messages.success(request, f'you are now logged')
                return JsonResponse({'optstatus':'success'})
                # return redirect('home')
            else:
                messages.warning(request, 'Please input correct password')
                # return JsonResponse({'optstatus':'error'})
        except:
            messages.warning(request,'Enter Username And Password.')
    categories = Categories.objects.all().order_by('name')
    subcategories = Subcategories.objects.all()    
    context = {        
        'cate' : categories ,
        'sub':subcategories,
    }
    return render(request, "UserLog/signin.html",context)

def signout(request):
    if request.session.has_key('email'):
        del request.session['email']
        return redirect('/')

def forgot_password(request):         
    if request.method == 'POST':
        email = request.POST.get('email')
        request.session['forgot'] = email
        if Signup.objects.filter(email=email).exists():            
            otp = ''
            rand = random.choice('0123456789')
            rand1 = random.choice('0123456789')
            rand2 = random.choice('0123456789')
            rand3 = random.choice('0123456789')
            otp = rand + rand1 + rand2 + rand3                        
            request.session['otp'] = otp
                
            subject = 'Forgot Password'
            message = otp
            email_from= settings.EMAIL_HOST_USER
            recipient_list = [email]            
            send_mail( subject, message, email_from, recipient_list )
            return JsonResponse({'optstatus':'Success'})
        else:
            return JsonResponse({'opstatus':'Error'})   
    return render(request,'UserLog/forgot-password.html')

def forgotOtp(request):
    e = request.session['forgot']   
    if request.session.has_key('otp'):
        otp = request.session['otp'] 
        print(otp)             
        if request.method == 'POST':                                               
            if otp == request.POST.get('otp'):
                del request.session['otp']
                return JsonResponse({'optstatus':'Success'})
            else:
                return JsonResponse({'optstatus':'Wrong'})
    return render(request,'UserLog/forgotOtp.html')

def newpassword(request):
    if request.session.has_key('forgot'):
        e = request.session['forgot']             
        if request.method == "POST":                
            new_pass = request.POST.get('newpassword')   
            print(new_pass)                
            obj = Signup.objects.get(email = e)      
            print(obj.email)      
            obj.password = new_pass
            obj.confirmpassword = new_pass
            obj.save()
            del request.session['forgot']
            return JsonResponse({'optstatus':'Success'})
    else:
        return JsonResponse({'optstatus':'SecondTime'})
    return render(request,'UserLog/newpassword.html')

def home(request):  
    categories = Categories.objects.all().order_by('name')
    subcategories = Subcategories.objects.all()    

    context = {
        'cate' : categories ,
        'sub':subcategories,
    }
    return render(request, "Home/home.html",context)


def product(request):
    categories = Categories.objects.all().order_by('name')
    
    SubcategoryID=request.GET.get('subcategory')

    if SubcategoryID:
        product = Product.objects.filter(subcategories = SubcategoryID)          
        subcategory = get_object_or_404(Subcategories, id=SubcategoryID)
        category = subcategory.subcat
        print(category)              
        
        context = {
            'cate':categories,
            'SingleCat' : category ,        
            'product' : product ,    
            'subcategory':subcategory,
        }  
        return render(request, "Product/product.html",context)
    else:         
        product = Product.objects.all()
        context = {                    
            'product' : product ,
            'cate':categories,
        } 
        return render(request, "Product/product.html",context)
    return render(request, "Product/product.html")

def productdetail(request,pk): 
    categories = Categories.objects.all().order_by('name')
    subcategory  = get_object_or_404(Subcategories,pk=pk) 
    prodetail  = get_object_or_404(Product,pk=pk)   
    
    #for related product
    #similarity_query = Q(category=prodetail.categories) & ~Q(pk=prodetail.pk)
    #related_products = Product.objects.filter(similarity_query)[:4]

    print(prodetail)
    prodetail.save()    
    context = {
        'cate' : categories ,
        'subcategory': subcategory,
        'p' : prodetail ,        
    }
    return render(request, "Product/productdetail.html",context)


def add_to_cart(request,pk):
    quantity = int(request.POST.get('quantity', 1))
    cart = request.session.get('cart', [])

    item_exists = False
    for item in cart:
        if item['id'] == pk:
            item['quantity'] += quantity
            item_exists = True
            break
    
    if not item_exists:
        cart.append({'id': pk, 'quantity': quantity})
        
    request.session['cart'] = cart    
    return JsonResponse({'optstatus':'added'}) 
    #if request.session.has_key('email'):
    #    per = Signup.objects.get(email=request.session['email'])         
    #    p = get_object_or_404(Product, pk=pk)             
    #    if request.method == 'POST':             
    #        if Mycart.objects.filter(product__id=p.pk, user__id=per.pk,status=False).exists():
    #            messages.warning(request, 'This item is already in the cart')
    #            return JsonResponse({'optstatus':'exists'})
    #            # return redirect('product')
    #        else:
    #            quantity = request.POST.get('quantity')
    #            print(quantity)
    #            cart=Mycart()                                                 
    #            cart.user=per
    #            cart.product=p 
    #            cart.quantity = quantity
    #            cart.save()
    #            return JsonResponse({'optstatus':'added'})           
    #    return render(request, 'Master/product.html', {'p': p, 'per': per})
    #else:
    #    return redirect('/signin/')

def show_mycart(request):
    cart = request.session.get('cart', [])
    items = Product.objects.filter(id__in=cart)
    print(items)
    for item in items:
        for cart_item in cart:
            if cart_item['id'] == item.pk:
                item.quantity = cart_item['quantity']
                break
        else:
            item.quantity = 0
    return render(request, 'Cart/showmycart.html', {'al': items})

#    if request.session.has_key('email'):
#        obj = Signup.objects.get(email=request.session['email'])
#        categories = Categories.objects.all().order_by('name')
#        subcategories = Subcategories.objects.all()    
#        all = Mycart.objects.filter(user_id=obj.id)                         
#        l=[]                                                    
#        total=0
#        for i in all:            
#            l.append(i)                                     
#            total=total + i.product.price * i.quantity    
            
#        #wishlist = Wishlist.objects.filter(user_id=obj.id)                         
#        #wish=[] 
#        #for i in wishlist:                       
#        #    wish.append(i)
#        return render(request,'Cart/showmycart.html',{'al':l,'all':all,'n':obj,'total':total,'cate' : categories ,'sub':subcategories,})
#    else:
#        return redirect('signin') 

#def cart_update(request, id):
#    if request.session.has_key('email'): 
#        user=Signup.objects.get(email=request.session['email'])       
#        # product=get_object_or_404(Product,id=id)
#        cart=Mycart.objects.get(id=id,user__id=user.id)        

#        if cart.quantity < cart.product.total_stock:        
#            cart.quantity += 1                        
#            cart.save()
#            return redirect('showmycart')
#        else:
#            messages.warning(request, f'Not available {cart.product.total_stock+1} Product')
#            return redirect('showmycart')   
      

#def cart_remove(request, id):
#    if request.session.has_key('email'): 
#        user=Signup.objects.get(email=request.session['email'])       
#        # product=get_object_or_404(Product,id=id)
#        cart=Mycart.objects.get(id=id,user__id=user.id)

#        if cart.quantity == 1:
#            return redirect('showmycart')

#        elif cart.quantity <= cart.product.total_stock:        
#            cart.quantity -= 1             
#            cart.save()
#            return redirect('showmycart')       

#def remove_items(request,id):
#    if request.session.has_key('email'):
#        obj = Signup.objects.get(email=request.session['email'])
#        y=Mycart.objects.get(id=id,user__id=obj.id)                        
#        y.delete()
#        return redirect('showmycart')
