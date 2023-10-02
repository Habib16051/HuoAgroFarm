from django.db import models
from django.contrib.auth.models import User

# Model for agricultural products (crops, livestock, etc.)
class Product(models.Model):
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    date_listed = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='product_images/')
    
    class Meta:
        ordering = ['-date_listed', ]

    def __str__(self):
        return self.name
    

# Model for farmer profiles
class FarmerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    contact_number = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    products = models.ManyToManyField(Product, blank=True, related_name='farmer')

    def __str__(self):
        return self.user.username

# Model for user reviews and ratings
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.reviewer.username} for {self.product.name}"

# Model for blog posts
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_posted', ]

    def __str__(self):
        return self.title
