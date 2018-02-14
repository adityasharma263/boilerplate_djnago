from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator

# Create your models here.
class User(models.Model):

    name = models.CharField(max_length=10,
                            blank=False, null=False)
    mobile = models.BigIntegerField(blank=True, null=True,
                                    validators=[MaxValueValidator(9999999999),
                                                MinValueValidator(7000000000)]
                                    )
    email = models.EmailField(
        max_length=300, unique=True, blank=True, null=True)
    follows = models.ManyToManyField('User', related_name='followed_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        default_permissions = ('add', 'change', 'delete', 'view')
        ordering = ('-updated_at',)
        db_table = 'user'
        app_label = 'app'


class Post(models.Model):

    post_text = models.TextField(validators=MaxLengthValidator(80),
                                 blank=False, null=False)
    user = models.ForeignKey(
        User, null=False, blank=False, on_delete=models.CASCADE,
        related_name='user_post')
    published_on = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.post_text

    class Meta:
        default_permissions = ('add', 'change', 'delete', 'view')
        ordering = ('-updated_at',)
        db_table = 'post'
        app_label = 'app'


