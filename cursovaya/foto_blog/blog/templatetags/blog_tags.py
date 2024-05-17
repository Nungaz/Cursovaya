from django import template
from blog.models import *

register = template.Library()


@register.inclusion_tag('blog/list_cat.html')
def show_cat(sort=None, cat_sell=0):
    if not sort:
        cats = Category.objects.all
    else:
        cats = Category.objects.order_by(sort)
    return {'cats': cats, 'cat_selected': cat_sell}

