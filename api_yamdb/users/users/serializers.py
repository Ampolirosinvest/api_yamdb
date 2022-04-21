from email.policy import default
from pkgutil import read_code
from pyexpat import model
from attr import fields
from rest_framework import serializers
<<<<<<< HEAD:api_yamdb/api/serializers.py
from reviews.models import Comment, User, Category, Genre, Title, Review
=======
>>>>>>> join:api_yamdb/users/users/serializers.py
from rest_framework.validators import UniqueValidator
from users.models import User


class SignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    def validate_username(self, value):
        if value.lower() == 'me':
            raise serializers.ValidationError(
                'Выберите другое имя пользователя'
            )
        return value

    class Meta:
        fields = ('username', 'email')
        model = User


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())],
        required=True,
    )
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        fields = ('username', 'email', 'first_name',
                  'last_name', 'bio', 'role')
        model = User
<<<<<<< HEAD:api_yamdb/api/serializers.py


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'slug')
        model = Category
        lookup_field = 'slug'


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'slug')
        model = Genre
        lookup_field = 'slug'


class TitleCreateSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug'
    )
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        many=True
    )

    class Meta:
        model = Title
        fields = '__all__'


class TitleReadSerializer(serializers.ModelSerializer):
    category = CategorySerializer(
        read_only=True
    )
    genre = GenreSerializer(
        read_only=True,
        many=True
    )
    rating = serializers.IntegerField()

    class Meta:
        model = Title
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):

<<<<<<< HEAD:api_yamdb/api/serializers.py
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )
    class Meta:
        fields = ('id', 'text', 'author', 'score', 'pub_date')
        model = Review

    def validate(self, data):
        review = Review.objects.filter(
            title = self.context['view'].kwargs.get('title_id'),
            author = self.context['request'].user
        )
        request = self.context.get('request')
        if review.exists() and request.method == 'POST':
            raise serializers.ValidationError(
                'Ваш отзыв на это произведение уже опубликован'
            )
        return data

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True,
    )

    class Meta:
        model=Comment
        fields = ('id', 'text', 'author', 'pub_date')
=======
#     class Meta:
#         fields = ('pub_date', 'review')
#         model = Category
#         lookup_field = 'slug'
=======
>>>>>>> 2a758645c99555ec945f65f2e6aba65a30cdf4f2:api_yamdb/users/users/serializers.py
>>>>>>> join:api_yamdb/users/users/serializers.py
