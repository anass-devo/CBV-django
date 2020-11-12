from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
# Create your views here.


class PostList(ListView): # name in template [object_list , post_list]
    model = Post 
    #context_object_name = "all_posts" # si on veu changer le nom du context dans la template
    ordering = ["-created_at"] # pour classifier selon la date de creation
    #queryset = Post.objects.filter(active=True) # attribus qui nou permet d'etablir des requete sur le model pour revenie avec des resultat souhaité
    template_name = "post/test.html" # pour préciser le nom de template html q'on vas utiliser au lieu d'utiliser les template choisi auomatiquement par django
    
    def get_queryset(self):
        return Post.objects.filter(active=True) # cette methode nou spermet les meme option que lattribut queryset
    
    def get_context_data(self, **kwargs): # cette methode nou permet de modifer et envoyer le contexxt qu'on veu de notre class vers la template et aussi des valeur spécifier pour les utiliser dans la template
        context=super().get_context_data(**kwargs)
        context['myname']="anass laaroussi"
        context['profession']="pythn developper"
        return context

class PostDetail(DetailView):
    model = Post  

class PostUpdate():
    model = Post 

class PostCreate():
    model = Post 