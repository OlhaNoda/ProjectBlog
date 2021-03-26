from django import template
from blog.models import Category

register = template.Library()


@register.inclusion_tag('blog/menu.html')
def get_menu():
    categories = Category.objects.all()
    return {'categories': categories, }
