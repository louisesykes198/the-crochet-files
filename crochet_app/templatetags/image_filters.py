from django import template
import os

register = template.Library()

@register.filter
def to_webp(image_url):
    """
    Converts an image URL ending in .png or .jpg/.jpeg to .webp.
    """
    base, ext = os.path.splitext(image_url)
    if ext.lower() in ['.png', '.jpg', '.jpeg']:
        return f"{base}.webp"
    return image_url
