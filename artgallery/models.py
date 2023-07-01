from django.db import models
from django.urls import reverse

from users.models import CustomUser

def fields_of_art():
    return [
        ('visual_arts', 'Visual arts'),
        ('fine_art', 'Fine art'),
        ('conceptual_art', 'Conceptual art'),
        ('sculpture', 'Sculpture'),
        ('painting', 'Painting'),
        ('installation_art', 'Installation art'),
        ('drawing', 'Drawing'),
        ('illustration', 'Illustration'),
        ('decorative_arts', 'Decorative arts'),
        ('abstract_art', 'Abstract art'),
        ('mixed_media', 'Mixed media'),
        ('digital_art', 'Digital art'),
        ('applied_arts', 'Applied arts'),
        ('pop_art', 'Pop art'),
    ]

def get_profile_img_filepath(self):
    return f'profile_images'/{self.pk}/{"profile_image.png"}

def get_default_profile_image():
    return 'profile_images/dummy_image.png'

class Artist(CustomUser):
    profile_image = models.ImageField(
        max_length = 255,
        upload_to = get_profile_img_filepath, 
        null = True,
        blank =  True,
        default = get_default_profile_image,
    )    
    nickname = models.CharField(max_length=100, null=True, blank=True)    
    bio = models.CharField(max_length=300, null=True, blank=True)    
    activity = models.CharField(choices = fields_of_art(), max_length=50)
    ''' Social Media '''
    instagram_username = models.CharField(verbose_name="Instagram", max_length=50)
    twitter_username = models.CharField(verbose_name="Twitter", max_length=50)
    linkedin_username = models.CharField(verbose_name="Linkedin", max_length=50)
    pinterest_username = models.CharField(verbose_name="Pinterest", max_length=50)

    def get_instagram_urlpath(self):
        return f'https://www.instagram.com'/'{self.instagram_username}'
    
    def get_twitter_urlpath(self):
        return f'https://twitter.com'/'{self.twitter_username}'
    
    def get_linkedin_urlpath(self):
        return f'https://www.linkedin.com/in'/'{self.linkedin_username}'
    
    def get_pinterest_urlpath(self):
        return f'https://www.pinterest.com'/'{self.pinterest_username}'


class ArtWork(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="name of art work", max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    score = models.PositiveSmallIntegerField(range(1, 11))
    style = models.CharField(choices = fields_of_art(), max_length=50)
    size = models.PositiveIntegerField()
    weight = models.FloatField()
    option = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}: {self.artist}'
    
    def get_absolute_url(self):
        return reverse("artwork view", args=[self.id])
