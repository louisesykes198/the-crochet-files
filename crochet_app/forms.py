from django import forms
from .models import Project
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from PIL import Image  
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comment

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'category', 'description', 'skill_level', 'materials_needed', 'notes', 'pattern', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40, 'class': 'form-control'}),
            'materials_needed': forms.Textarea(attrs={'rows': 3, 'cols': 40, 'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'rows': 3, 'cols': 40, 'class': 'form-control'}),
            'pattern': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_pattern(self):
        """Ensure only PDF files are allowed for pattern uploads."""
        pattern = self.cleaned_data.get('pattern')
        if pattern:
            ext_validator = FileExtensionValidator(allowed_extensions=['pdf'])
            ext_validator(pattern)
        return pattern

    def clean_image(self):
        """Ensure only valid JPEG or PNG images are allowed and under 5MB."""
        image = self.cleaned_data.get('image')
        if image:
            # Check file size (max 5MB)
            if image.size > 5 * 1024 * 1024:
                raise ValidationError("Image file is too large ( > 5MB ). Please upload a smaller image.")
            
            # Validate file extension
            ext_validator = FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])
            ext_validator(image)

            # Validate actual image format with Pillow
            try:
                img = Image.open(image)
                if img.format not in ['JPEG', 'PNG']:
                    raise ValidationError('Only JPEG and PNG images are allowed.')
            except Exception as e:
                raise ValidationError(f'Invalid image file: {e}')
        return image

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        """Ensure the email is unique."""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("A user with that email address already exists.")
        return email
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']



