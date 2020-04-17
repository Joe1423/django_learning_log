from django.db import models

#references -> https://docs.djangoproject.com/en/3.0/ref/models/fields/

#To activate model go to settings.py in the folder that share name with the project, and add this app name to the tuple INSTALLED_APPS

# Create your models here.
class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Entry(models.Model):
    """Something specific learnt about a topic."""
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """To string."""
        return self.text[:50] + "..."

