from django.db import models
from django.urls import reverse, NoReverseMatch


class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    url = models.CharField(max_length=255, help_text="Можно указать либо url-имя, либо абсолютный путь")
    is_named_url = models.BooleanField(default=False, help_text="Отметьте, если в поле URL указано имя маршрута (named url)")


    def get_level(self):
        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent
        return level


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        if not self.url:
            return "#missing-url"
        if self.is_named_url:
            try:
                return reverse(self.url)
            except NoReverseMatch:
                return "#invalid-named-url"
        return self.url
