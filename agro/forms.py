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
