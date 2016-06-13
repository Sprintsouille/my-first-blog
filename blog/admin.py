from django.contrib import admin
from .models import Post

# Enregistre le modèle pour qu'il soit visible dans l'interface admin
admin.site.register(Post)

# Register your models here.
