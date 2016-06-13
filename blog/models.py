# Import = fait référence à certains morceaux d'autres fichiers
from django.db import models
from django.utils import timezone

class Post(models.Model): # C'est cette ligne qui permet de définir notre modèle. C'est un object
# Le mot clef spécial class permet d'indiquer que nous sommes en train de définir un objet.
# Post est le nom de notre modèle. Vous pouvez lui donner un autre nom
    #mais vous ne pouvez pas utiliser de caractères spéciaux ou accentués ni insérer des espaces.
    #Le nom d'une classe commence toujours par une majuscule.
# models.Model signifie que Post est un modèle Django. Comme ça, Django sait qu'il doit l'enregistrer dans la base de données.

    """Définitions des objets (= modèles) => Déf d'un blog post"""
# Propriétés = type du champ (texte ? nombre ? date ? relation à un autre objet, un utilisateur ?) :
    author = models.ForeignKey('auth.User') # auteur = C'est un lien vers un autre modèle.
    title = models.CharField(max_length=200) # titre = Cela nous permet de définir un champ texte avec un nombre limité de caractères.
    text = models.TextField() # texte = Cela nous permet de définir un champ texte sans limite de caractères. Parfait pour le contenu d'un blog post !
    created_date = models.DateTimeField(default=timezone.now) # date de création = Définit que le champ en question est une date ou une heure.
    published_date = models.DateTimeField(blank=True, null=True) # date de publication

    def publish(self):
    # def = création d'une fonction/méthode avec le nom publish
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title # renvoie du texte (string) avec un titre de Post


# Create your models here.
