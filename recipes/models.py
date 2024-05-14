from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.db.models import F, Value
from django.db.models.functions import Concat


class Category(models.Model):
    """Class Category for recipes"""

    name = models.CharField(max_length=65)

    def __str__(self):
        return str(self.name)


class RecipeManager(models.Manager):
    def get_queryset(self):
        # self aqui é o Recipe.objects
        return (
            super()
            .get_queryset()
            .filter(is_published=False)
            .annotate(
                author_full_name=Concat(
                    F("author__first_name"),
                    Value(" "),
                    F("author__last_name"),
                    Value(" ("),
                    F("author__username"),
                    Value(")"),
                )
            )
        ).order_by("-id")


class Recipe(models.Model):
    """Class Recipe"""

    objects = RecipeManager()

    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField(unique=True)
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_step = models.TextField()
    preparation_step_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(
        upload_to="recipes/covers/%Y/%m/%d/",
        blank=True,
        default="",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )

    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return str(self.title)

    # Get the absolute url for the recipe
    def get_absolute_url(self):
        return reverse("recipes:recipe", args=(self.pk,))

    # Sempre que eu usar .save(), isso vai ser executado
    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f"{slugify(self.title)}"
            self.slug = slug

        return super().save(*args, **kwargs)
