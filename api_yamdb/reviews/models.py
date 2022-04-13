from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'
    USER_ROLES = [
        (USER, 'user'),
        (MODERATOR, 'moderator'),
        (ADMIN, 'admin'),
    ]
    username = models.SlugField(
        'Имя пользователя',
        help_text='Имя пользователя',
        max_length=150,
        blank=False,
        unique=True
    )
    email = models.EmailField(
        'Электронная почта',
        help_text='Электронная почта пользователя',
        blank=False,
        unique=True
    )
    bio = models.TextField(
        'Немного о себе',
        help_text='Биография пользователя',
        blank=True,
    )
    confirmation_code = models.CharField(
        'Код подтверждения',
        help_text='Код подтверждения пользователя',
        max_length=200,
    )
    role = models.CharField(
        'Роль',
        help_text='Роль пользователя',
        max_length=150,
        blank=False,
        choices=USER_ROLES,
        default='user',
    )

    @property
    def is_admin(self):
        if self.role == self.ADMIN or self.is_superuser:
            return True

    @property
    def is_moderator(self):
        if self.role == self.MODERATOR or self.is_superuser:
            return True

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = (
            'username',
        )

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(
        'название',
        max_length=256
    )
    slug = models.SlugField(
        'slug',
        unique=True
    )

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(
        'название',
        max_length=50,
    )
    slug = models.SlugField(
        'slug',
        unique=True,
    )

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(
        'название',
        max_length=200,
    )
    year = models.IntegerField(
        'год',
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='titles',
    )

    def __str__(self):
        return self.name