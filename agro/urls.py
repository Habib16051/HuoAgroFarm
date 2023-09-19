from django.urls import path
from . import views

app_name = 'agro'  # Define an app namespace

urlpatterns = [
    # URL patterns for agricultural products
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),

    # URL patterns for farmer profiles
    path('farmer/<str:username>/', views.FarmerProfileView.as_view(), name='farmer_profile'),

    # URL patterns for submitting reviews
    path('products/<int:product_id>/submit-review/', views.SubmitReviewView.as_view(), name='submit_review'),

    # URL patterns for blog posts
    path('blog/', views.BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
]
