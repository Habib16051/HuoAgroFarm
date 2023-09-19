from django.contrib import admin
from .models import Product, FarmerProfile, Review, BlogPost

# Register the Product model with the admin site
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'seller', 'price', 'quantity', 'location', 'date_listed', 'image')
    list_filter = ('seller', 'location')
    search_fields = ('name', 'description', 'location')
    date_hierarchy = 'date_listed'

# Register the FarmerProfile model with the admin site
@admin.register(FarmerProfile)
class FarmerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'contact_number')
    list_filter = ('location',)
    search_fields = ('user__username', 'user__email', 'location')

# Register the Review model with the admin site
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'reviewer', 'rating', 'date_posted')
    list_filter = ('rating',)
    search_fields = ('product__name', 'reviewer__username')

# Register the BlogPost model with the admin site
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')
    list_filter = ('author',)
    search_fields = ('title', 'content')

# You can further customize the admin views and actions as needed
