from django import template
from documents.models import Category

register = template.Library()

@register.filter
def dotcomma(value):
    """
    Raqamni nuqtalar bilan ajratadi.
    15000000 → 15.000.000
    """
    try:
        value = int(value)
        return f"{value:,}".replace(",", ".")
    except (ValueError, TypeError):
        return value
    
@register.simple_tag(name="get_cats")
def get_categories(user):
    categories = Category.objects.filter(user=user).distinct()
    return categories