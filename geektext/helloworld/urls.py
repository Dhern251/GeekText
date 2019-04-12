from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$',views.index,name = 'bookdetails'),
    url(r'^addtocart2/$',views.addtocart2,name = 'addtocart2'),#add to cart from bookdetails

]