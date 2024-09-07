from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from authors.models import Profile

User = get_user_model()


# isso é um sinal que é acionado sempre que um novo usuário é criado
# Aqui no caso, SEMPRE que um novo usuário é criado, um perfil é criado para ele


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        profile = Profile.objects.create(author=instance)
        profile.save()
