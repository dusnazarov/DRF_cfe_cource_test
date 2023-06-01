# 1)  wiews.py 3,4,5,6 /////////////////////////////////////
# from django.db import models


# class Product(models.Model):
#     title = models.CharField(max_length=120)
#     content = models.TextField(blank=True, null=True)
#     price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)


# 2)  wiews.py 7 /////////////////////////////////////
# from django.db import models


# class Product(models.Model):
#     title = models.CharField(max_length=120)
#     content = models.TextField(blank=True, null=True)
#     price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)

#     @property
#     def sale_price(self):
#         return "%.2f" %(float(self.price)*0.8)    

#     def get_discount(self):
#         return "1222"
    
    
#     def get_content(self):
#         return f"This is my {self.title}"


 # 3)  products/wiews.py  /////////////////////////////////////
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price)*0.8)    

    def get_discount(self):
        return "1222"    
    
    def get_content(self):
        return f"This is my {self.title}"
    