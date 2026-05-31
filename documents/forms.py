from django import forms
from .models import Category, Documents
from django.core.exceptions import ValidationError
from django.utils.text import slugify

from django import forms
from .models import Category, Documents
from django.core.exceptions import ValidationError
from django.utils.text import slugify

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ['name', 'price', 'image', 'description', 'category']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        self.user = user
        
        self.fields['category'].empty_label = "Hujjat turi tanlanmagan!"
        if self.user:
            self.fields['category'].queryset = Category.objects.filter(user=self.user)

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        
        if name and self.user:
            slug = slugify(name)
            if Documents.objects.filter(slug=slug, user=self.user).exists():
                self.add_error('name', "Sizda bu nomli hujjat allaqachon mavjud!")
        
        return cleaned_data

class AddCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.user = user

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        user = self.user
        slug = slugify(name)
        if Category.objects.filter(slug=slug, user=user):
            self.add_error("name", "Siz bu postavshikni allaqachon kiritgansiz! iltimos boshqa nom kiriting")
        return cleaned_data