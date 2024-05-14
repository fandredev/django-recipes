from collections import defaultdict
from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    """Class Category for recipes"""

    name = models.CharField(max_length=65)

    def __str__(self):
        return str(self.name)


class Recipe(models.Model):
    """Class Recipe"""

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

    # validação no form e no admin (bom demais!)
    def clean(self, *args, **kwargs):
        error_messages = defaultdict(list)

        recipe_from_db = Recipe.objects.filter(title__iexact=self.title).first()

        if recipe_from_db:
            if recipe_from_db.pk != self.pk:
                error_messages["title"].append("Já existe uma receita com esse título.")

        if error_messages:
            raise ValidationError(error_messages)
