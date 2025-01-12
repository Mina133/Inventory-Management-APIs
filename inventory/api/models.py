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
    low_stock_threshold = models.PositiveIntegerField(default=10)

    store  = models.ForeignKey('Store', on_delete=models.CASCADE)
    barcode = models.CharField(max_length=100, unique=True)


    def __str__(self):
        return self.Name
    
class Categories(models.Model):
    Name = models.CharField(max_length=100) 
    
    def __str__(self):
        return self.Name
    
class Store(models.Model):
    Number_of_stores = 0
    Name = models.CharField(max_length=100, default='Store {}'.format(Number_of_stores+1))
    Location = models.CharField(max_length=100)

    Staff_members = models.ManyToManyField('staff_member')

    def __str__(self):
        return self.Name
    
class staff_member(models.Model):
    user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE)
    Name = models.CharField(max_length=100, default='John Doe')
    Position = models.CharField(max_length=100, default='Manager')
    def __str__(self):
        return self.Name