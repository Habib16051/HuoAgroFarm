from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from .models import Product, FarmerProfile, Review, BlogPost
from .forms import ReviewForm  # Import any necessary forms


# HomePage

class HomePageView(TemplateView):
    template_name = 'agro/home.html'


# Product CRUD
    

# View for listing agricultural products
class ProductListView(ListView):
    model = Product
    template_name = 'agro/product_list.html'
    context_object_name = 'products'

# View for displaying a single product detail
class ProductDetailView(DetailView):
    model = Product
    template_name = 'agro/product_detail.html'
    context_object_name = 'product'

# View for displaying a farmer's profile
class FarmerProfileView(DetailView):
    model = FarmerProfile
    template_name = 'agro/farmer_profile.html'
    context_object_name = 'farmer'
    slug_field = 'user__username'
    slug_url_kwarg = 'username'

# View for submitting a review for a product
class SubmitReviewView(View):
    template_name = 'agro/submit_review.html'

    @login_required
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        form = ReviewForm()
        return render(request, self.template_name, {'form': form, 'product': product})

    @login_required
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.reviewer = request.user
            review.save()
            return redirect('product_detail', product_id=product_id)
        return render(request, self.template_name, {'form': form, 'product': product})

# View for listing blog posts
class BlogListView(ListView):
    model = BlogPost
    template_name = 'agro/blog_list.html'
    context_object_name = 'posts'

# View for displaying a single blog post
class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'agro/blog_detail.html'
    context_object_name = 'post'
