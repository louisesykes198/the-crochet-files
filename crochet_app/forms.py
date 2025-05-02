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
        fields = [
            'name', 'category', 'description',
            'skill_level', 'materials_needed',
            'notes', 'pattern', 'image'
        ]
        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 4, 'cols': 40, 'class': 'form-control'
            }),
            'materials_needed': forms.Textarea(attrs={
                'rows': 3, 'cols': 40, 'class': 'form-control'
            }),
            'notes': forms.Textarea(attrs={
                'rows': 3, 'cols': 40, 'class': 'form-control'
            }),
            'pattern': forms.ClearableFileInput(
                attrs={'class': 'form-control'}
            ),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


def clean_pattern(self):
    pattern = self.cleaned_data.get('pattern')

    if pattern and hasattr(pattern, 'file'):
        # Optional: Size check
        if pattern.size > 10 * 1024 * 1024:  # 10MB limit
            raise ValidationError("Pattern file is too large ( > 10MB ).")

        # Extension check (manual instead of using FileExtensionValidator)
        if hasattr(pattern, 'name'):
            if not pattern.name.lower().endswith('.pdf'):
                raise ValidationError(
                    "Only PDF files are allowed for pattern uploads.")

    return pattern


def clean_image(self):
    image = self.cleaned_data.get('image')

    # Only validate if it's a freshly uploaded file
    if image and hasattr(image, 'file'):
        # Check file size
        if image.size > 5 * 1024 * 1024:
            raise ValidationError(
                "Image file is too large ( > 5MB ). "
                "Please upload a smaller image."
            )

    if (hasattr(image, 'name') and
            not image.name.lower().endswith(('.jpg', '.jpeg', '.png'))):
        raise ValidationError("Only JPG, JPEG, and PNG files are allowed.")


        # Check actual image format
        try:
            img = Image.open(image)
            if img.format.upper() not in ['JPEG', 'PNG']:
                raise ValidationError('Only JPEG and PNG images are allowed.')
        except Exception as e:
            raise ValidationError(f'Invalid image file: {e}')

    # For already-uploaded Cloudinary images, skip validation
    return image
    print(f"image type: {type(form.cleaned_data.get('image'))}")


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        """Ensure the email is unique."""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError(
                 "A user with that email address already exists.")
        return email


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']



