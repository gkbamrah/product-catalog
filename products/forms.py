from django import forms
from .models import Tag, Category

class ProductSearchForm(forms.Form):
    search = forms.CharField(max_length=100, 
                             required=False, 
                             label="Search", 
                             widget=forms.TextInput(attrs={
                                 'placeholder': 'Search products...'
                                 })   
                             )

    category = forms.ModelChoiceField(queryset=Category.objects.all(), 
                                      empty_label="All Categories", 
                                      label="Category",
                                      required=False,
                                      widget=forms.Select()) 
    
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), 
                                          label="Tags",
                                          widget=forms.CheckboxSelectMultiple, 
                                          required=False)
    
