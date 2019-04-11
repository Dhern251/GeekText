from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$',views.shoppingcart,name = 'shoppingcart'),
    url(r'^removesc/',views.removesc,name = 'removesc'),#remove shoppingcart
    url(r'^removesfl/',views.removesfl,name = 'removesfl'),#remove saved for later
    url(r'^saveforlater/$',views.saveforlater,name = 'saveforlater'),#save for later from cart
    url(r'^addtocart/$',views.addtocart,name = 'addtocart'),#add to cart from SFL
    url(r'^changequantity/$',views.changequantity,name = 'changequantity'),
]