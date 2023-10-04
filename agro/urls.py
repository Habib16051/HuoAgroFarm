from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'agro'  # Define an app namespace

urlpatterns = [ 
               
    # Home page
    path('', views.HomePageView.as_view(), name='home'),
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
    
    # ContactsView URls for
    path('contact/', views.ContactView.as_view(), name='contact'),
    # It will be added if we use class based views
    path('contact/success/', TemplateView.as_view(template_name='success.html'), name='success'),
    
    
    # Six Seasons
    path('summer/', views.SummerView.as_view(), name='summer'),
    path('rainy/', views.RainyView.as_view(), name='rainy'),
    path('autumn/', views.AutumnView.as_view(), name='autumn'),
    path('late_autumn/', views.LateAutumnView.as_view(), name='late_autumn'),
    path('winter/', views.WinterView.as_view(), name='winter'),
    path('spring/', views.SpringView.as_view(), name='spring'),
    
    # Documentation Download
    path('document/', views.download_pdf, name='document'),
    
    
    # Search for blog articles
    path('search/', views.blog_search, name='search'),

    

]
