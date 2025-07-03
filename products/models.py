from django.db import models

class Watch(models.Model):
    brand = models.CharField(max_length=20)
    desk = models.TextField()
    image = models.ImageField(upload_to='watch-images/', blank=True, null=True, default='default/watch.png')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.brand