from django import template
import os

register = template.Library()

@register.filter
def to_webp(image_url):
    # Ensure the image URL is a valid static path
    if 'static/' in image_url:
        base, ext = os.path.splitext(image_url)
        if ext.lower() in ['.png', '.jpg', '.jpeg']:
            return f"{base}.webp"  # Return the correct .webp URL without any query params
    return image_url



