from django.shortcuts import render, HttpResponse,redirect
from django.http import HttpResponse
from .models import BookDetails
from django.template import loader
from shoppingcart.models import CartItems, Cart


# Create your views here.
#def myView(request):
	#return render(request, 'helloworld/bookdetails.html') #sprint2 helloworld

#3/23
def home(request):
	numbers = [1,2,3,4,5]
	name = 'Vicky G'
	args = {'myName': name}
	return render(request, 'helloworld/bookdetails.html', args) #got html from under templates

def get(self, request):
	bookdetails = BookDetails.objects.all()
	return render(request, 'helloworld/bookdetails.html', args)

def bookdetails_view(request):
	obj = BookDetails.objects.get(id=1)
	context = {
		'object': obj
	}
	return render(request, 'helloworld/bookdetails.html', {})

def index(request):
	all_bookdetails = BookDetails.objects.all()
	template = loader.get_template('helloworld/bookdetails.html')
	context = { 
		'all_bookdetails': all_bookdetails,
	}
	return HttpResponse(template.render(context,request))

def addtocart2(request):#removes item from Saved for later and adds it to shopping cart
	selected_book = BookDetails.objects.get(pk=request.POST['item'])
	b = CartItems(cartId = Cart.objects.get(pk = 1), productId = selected_book,quantity = 1)
	b.save()
	return redirect('/shoppingcart/')