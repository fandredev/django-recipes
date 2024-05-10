from django.contrib import admin
from .models import Category, Recipe

# Register your models here.


class CategoryAdmin(admin.ModelAdmin): ...


admin.site.register(Category, CategoryAdmin)


@admin.register(Recipe)
class RecipesAdmin(admin.ModelAdmin):
    # Campos que serão exibidos na listagem
    list_display = ("id", "title", "category", "author", "created_at", "is_published")

    # Campos que serão links para a edição
    list_display_links = ("title", "category")

    # Campos que serão usados para filtrar os registros (Criará um campo de busca)
    search_fields = ("title", "description", "slug")

    # Campos que serão usados para filtrar os registros (Criará um campo de filtro)
    list_filter = ("category", "author", "is_published", "preparation_step_is_html")

    # Quantidade de registros por página
    list_per_page = 10

    # Campos que poderão ser editados diretamente na listagem
    list_editable = ("is_published",)

    # Campos que serão ordenados
    ordering = ("-id",)

    # O campo slug será preenchido automaticamente com o valor do campo title
    prepopulated_fields = {"slug": ("title",)}
