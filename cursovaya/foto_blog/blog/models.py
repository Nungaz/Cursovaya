from django.db import models
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=250, verbose_name="Название")
    slug = models.SlugField(max_length=260, unique=True, verbose_name="URL")
    body = models.TextField(blank=True, verbose_name="Контент")
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/", blank=True, verbose_name="Фото")
    time_cre = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_up = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    published = models.BooleanField(default=True, verbose_name="Публикация")
    cat = models.ForeignKey("Category", on_delete=models.PROTECT,
                            verbose_name="Категория")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = "Новости"
        ordering = ['-time_cre']


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Категория")
    slug = models.SlugField(max_length=250, unique=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = "Категории"


class Photos(models.Model):
    image = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name="картинки для блога", blank=True, null=True,
                              default=None)
    add_image = models.ImageField(upload_to="photo/%Y/%m/%d/add/", blank=True, null=True,
                                  verbose_name="Добавить картинку")

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = "Изображения"
