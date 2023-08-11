from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class CarPost(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to="images", blank=True)
    content = models.TextField(blank=True, verbose_name="Contenue")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length=255, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_on = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name="Publié")
    
    class Meta:
        ordering = ['-created_on']
        verbose_name = "Voiture"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs) 
    
    @property
    def author_or_default(self):
        return self.author.get_username  if self.author else "L'auteur inconnu"
    
    def get_absolute_url(self):
        return reverse('posts:home')
       
    
