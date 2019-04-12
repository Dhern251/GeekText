from django.db import models
from helloworld.models import BookDetails

class Product(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.CharField(max_length = 1000, default = 'https://upload.wikimedia.org/wikipedia/commons/b/b9/No_Cover.jpg')

    def __unicode__(self):
        return unicode(self.pk)

class Cart(models.Model):
    userId = models.IntegerField()

class CartItems(models.Model):
    cartId = models.ForeignKey(Cart, on_delete=models.CASCADE)
    productId = models.ForeignKey(BookDetails,on_delete = models.CASCADE)
    quantity = models.IntegerField()

class SavedForLater(models.Model):
    cartId = models.ForeignKey(Cart, on_delete=models.CASCADE)
    productId = models.ForeignKey(BookDetails,on_delete = models.CASCADE)




