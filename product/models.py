from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 100)
    url = models.TextField()
    pub_date = models.DateTimeField()
    votes_total = models.IntegerField()
    image = models.ImageField(upload_to = "images/")
    icon = models.ImageField(upload_to = "images/")
    body = models.TextField()
    hunter = models.ForeignKey(User, on_delete = models.CASCADE, default = "")

    def __str__(self):
        return self.title
        
    def summary(self):
        return self.body[:165]
    
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

class Vote(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, default ="")
    hunter = models.ForeignKey(User, on_delete = models.CASCADE, default = "")

    def __str__(self):

        return self.hunter.username + " " + self.product.title