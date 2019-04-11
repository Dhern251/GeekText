from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import CartItems, Product, SavedForLater
from django.db.models import Sum, F,Value
from django.db import models




def shoppingcart(request):
    
    all_items = CartItems.objects.filter(cartId = 1)#showing information of Cart #1
    totalItems = list(all_items.aggregate(Sum('quantity')).values())[0]
    primary = all_items.values_list('productId', flat=True)
    total = Product.objects.filter(pk__in=primary).aggregate(
    total = Sum(F('price') * F('cartitems__quantity'), 
    output_field = models.FloatField()))['total']
    saved_items = SavedForLater.objects.filter(cartId = 1)
    totalsaveditems = saved_items.count()
    context = { 'all_items': all_items,
                'totalItems': totalItems,
                'total':total,
                'saved_items' : saved_items,
                'totalsaveditems' : totalsaveditems,
            }

    return render(request, 'shoppingcart/shoppingcart.html', context)

def removesc(request):#shoppingcart remove
    item = CartItems.objects.get(pk=request.POST['item'])
    item.delete()
    return redirect('/shoppingcart/')

def removesfl(request):#saved for later remove
    item = SavedForLater.objects.get(pk=request.POST['item'])
    item.delete()
    return redirect('/shoppingcart/')

def saveforlater(request):#removes item from shopping cart and adds it to saved for later
    item = CartItems.objects.get(pk=request.POST['item'])
    b = SavedForLater(cartId = item.cartId,productId = item.productId)
    b.save()
    item.delete()
    return redirect('/shoppingcart/')

def addtocart(request):#removes item from Saved for later and adds it to shopping cart
    item = SavedForLater.objects.get(pk=request.POST['item'])
    b = CartItems(cartId = item.cartId,productId = item.productId,quantity = 1)
    b.save()
    item.delete()
    return redirect('/shoppingcart/')

def changequantity(request):#removes item from Saved for later and adds it to shopping cart
    item = CartItems.objects.get(pk=request.POST['item'])
    item.quantity = request.POST['quantity']
    item.save()
    return redirect('/shoppingcart/')






