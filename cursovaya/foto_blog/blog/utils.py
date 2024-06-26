from .models import *

menu = [
    {'title': 'Главная страница', 'url': 'index'},
    {'title': 'Добавить статью', 'url': 'addpost'},
    {'title': 'Добавить картинки', 'url': 'addimg'},
    {'title': 'Блог', 'url': 'blogs'},
]


class DataMixin:
    paginate_by = 5

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu
        context['cat'] = cats

        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
