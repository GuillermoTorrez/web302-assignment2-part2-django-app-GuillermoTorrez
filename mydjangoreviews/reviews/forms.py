from django import forms
from products.models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        # Inside of the nested Meta class, there will be two class variable
        model = Review
        # The fields variable is a tuple of the names of all of the form fields which should be included in this form.
        fields = ('product_id','comment', 'date_review', 'rate',)