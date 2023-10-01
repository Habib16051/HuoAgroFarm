from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from .models import Product, FarmerProfile, Review, BlogPost
from .forms import ReviewForm  # Import any necessary forms

from django.core.mail import EmailMessage
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail
from django.views.generic.edit import FormView


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
    
    
# Contacts view
# views.py

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = 'success/'  # Redirect URL upon successful form submission

    def form_valid(self, form):
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']

        send_mail(
            subject,
            message,
            'huo143@gmail.com',  # Sender's email address
            [email],  # Recipient's email address
            fail_silently=False,
        )
        return super().form_valid(form)


# Function based Contact View Controller

# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']

#             send_mail(
#                 subject,
#                 message,
#                 'huo143@gmail.com',  # Sender's email address
#                 [email],  # Recipient's email address
#                 fail_silently=False,
#             )
#             return render(request, 'success.html')  # Redirect to a success page
#     else:
#         form = ContactForm()

#     return render(request, 'contact.html', {'form': form}) 