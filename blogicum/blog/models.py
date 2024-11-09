from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class BaseModel(models.Model):
    is_published = models.BooleanField('Опубликовано', default=True)
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField('Заголовок', max_length=256)
    description = models.TextField('Описание')
    slug = models.SlugField('Идентификатор', unique=True)


class Location(BaseModel):
    name = models.CharField('Название места', max_length=256)


class Post(BaseModel):
    title = models.CharField('Заголовок', max_length=256)
    text = models.TextField('Текст')
    pub_date = models.DateTimeField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL
    )
