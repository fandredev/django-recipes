from rest_framework import serializers

from authors.validators import AuthorRecipeValidator
from recipes.models import Recipe

# USANDO O SERIALIZER DE FORMA MANUAL

# class RecipeSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=65)
#     description = serializers.CharField(max_length=165)
#     public = serializers.BooleanField(
#         source="is_published"
#     )  # Renomeia o campo is_published para public (CASO QUEIRA) usando source, se não usar, o campo será is_published

#     preparation = serializers.SerializerMethodField(
#         method_name="get_preparation"
#     )  # SEMPRE que queremos fazer algumas operações com o campo, usamos SerializerMethodField e criamos um método com o nome get_<nome_do_campo>

#     category_name = serializers.StringRelatedField(
#         source="category"
#     )  # Como queremos o nome da categoria (__str__) e não o id, usamos StringRelatedField

#     author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

#     def get_preparation(self, recipe: Recipe):
#         return f"{recipe.preparation_time} {recipe.preparation_time_unit}"


# USANDO O SERIALIZER DE FORMA AUTOMÁTICA
class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = [  # Tente não usar o __all__ para não expor campos sensíveis
            "id",
            "title",
            "description",
            "category",
            "public",
            "preparation",
            "author",
            "preparation_time",
            "preparation_time_unit",
            "preparation_step",
            "preparation_step_is_html",
            "servings_unit",
            "servings",
            "cover",
        ]

    public = serializers.BooleanField(source="is_published", read_only=True)
    category = serializers.StringRelatedField(read_only=True)
    preparation = serializers.SerializerMethodField(
        method_name="get_preparation", read_only=True
    )

    def get_preparation(self, recipe: Recipe):
        return f"{recipe.preparation_time} {recipe.preparation_time_unit}"

    def validate(self, attrs):
        if self.instance is not None and attrs.get("servings") is None:
            attrs["servings"] = self.instance.servings

        if self.instance is not None and attrs.get("preparation_time") is None:
            attrs["preparation_time"] = self.instance.preparation_time

        super_validate = super().validate(attrs)
        AuthorRecipeValidator(data=attrs, ErrorClass=serializers.ValidationError)

        return super_validate

    # # VALIDAÇÃO DE CAMPOS
    # def validate_title(self, title: str):
    #     if len(title) < 5:
    #         raise serializers.ValidationError("O título deve ter mais de 5 caracteres")

    #     return title
