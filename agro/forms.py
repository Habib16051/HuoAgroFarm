from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'text']

    rating = forms.ChoiceField(
        choices=[(i, i) for i in range(1, 6)],
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    text = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-textarea'}),
        max_length=500,
        help_text="Write your review here (maximum 500 characters).",
    )

# contact/forms.py
class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)
