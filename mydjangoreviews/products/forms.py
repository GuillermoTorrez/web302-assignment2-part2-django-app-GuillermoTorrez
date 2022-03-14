# Now we need to define a form class for each of our models in forms.py
# In this file, we must import the forms object from the Django module and Product and Category classes from the models module.

from django import forms
from .models import Product, Category

# Then create a class for the form as child class of the Modelform class which is in the form object.

class ProductForm(forms.ModelForm):
    class Meta:
        # Inside of the nested Meta class, there will be two class variable
        model = Product
        # The fields variable is a tuple of the names of all of the form fields which should be included in this form.
        fields = ('name','category','price', 'image',)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
