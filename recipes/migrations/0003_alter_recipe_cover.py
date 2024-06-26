# Generated by Django 5.0.1 on 2024-05-05 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0002_recipe_delete_recipes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="cover",
            field=models.ImageField(
                blank=True,
                default="",
                upload_to="recipes/covers/%Y/%m/%d/",
            ),
        ),
    ]
