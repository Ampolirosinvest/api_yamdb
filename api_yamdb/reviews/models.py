<<<<<<< HEAD
=======
<<<<<<< HEAD
# from cgitb import text
>>>>>>> join
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


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
        ordering = ['username']

    def __str__(self):
        return self.username
=======
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from users.models import User
>>>>>>> 2a758645c99555ec945f65f2e6aba65a30cdf4f2


class Category(models.Model):
    name = models.CharField(
        'название',
        max_length=256,
        default=None
    )
    slug = models.SlugField(
        'slug',
        max_length=50,
        unique=True
    )

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(
        'название',
        max_length=100,
        default=None
    )
    slug = models.SlugField(
        'slug',
        max_length=50,
        unique=True
    )

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(
        'название',
        max_length=200,
    )
    year = models.IntegerField(
        'год',
    )
    description = models.TextField(
        'описание',
        max_length=200,
        blank=True,
        null=True
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='titles',
    )
    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.SET_NULL,
        related_name='titles',
    )

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Review(models.Model):
<<<<<<< HEAD
    text = models.TextField()
    author = models.ForeignKey(
=======
<<<<<<< HEAD
    text = models.TextField(
        'Отзыв',
        # max_length=1000,
        # blank=True,
        # null=True
    )
    reviewer = models.ForeignKey(
>>>>>>> join
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    pub_date = models.DateTimeField('Дата добавления', auto_now_add=True)
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    score = models.IntegerField(validators=[MinValueValidator(1),
                                             MaxValueValidator(10)])

    class Meta:
        ordering = ('-pub_date',)
        constraints = [
            models.UniqueConstraint(
<<<<<<< HEAD
                fields=['title', 'author'],
=======
                fields=['title', 'reviewer'],
=======
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    pub_date = models.DateTimeField('Дата добавления', auto_now_add=True)
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    score = models.IntegerField(validators=[MinValueValidator(1),
                                MaxValueValidator(10)])

    class Meta:
        ordering = ('-pub_date',)
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'],
>>>>>>> 2a758645c99555ec945f65f2e6aba65a30cdf4f2
>>>>>>> join
                name='unique_relationships'
            ),
        ]
    
    def __str__(self):
        return self.text

<<<<<<< HEAD

class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True)
    
    class Meta:
        ordering = ('id',)
=======
    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True)

    class Meta:
        ordering = ('id', )
>>>>>>> 2a758645c99555ec945f65f2e6aba65a30cdf4f2
