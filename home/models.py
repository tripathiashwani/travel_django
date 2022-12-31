from django.db import models

# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    # arena = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    # members = models.CharField(max_length=15)
    # budget = models.CharField(max_length=15)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class search(models.Model):
    search=models.CharField(max_length=200)
    
    def __str__(self):
        return self.search