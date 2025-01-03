from django.db import models

# Create your models here.
class Items (models.Model):
    Name = models.CharField(max_length=100)
    Description = models.TextField()
    Quantity = models.IntegerField()
    Price = models.FloatField()
    Category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    Date_Added = models.DateField(auto_now_add=True)
    Last_Update = models.DateField(auto_now=True)

    def __str__(self):
        return self.Name
    
class Categories(models.Model):
    Name = models.CharField(max_length=100) 
    
    def __str__(self):
        return self.Name