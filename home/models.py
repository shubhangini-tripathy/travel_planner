from django.db import models

# Create your models here.


class Travel(models.Model):
    destination = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    user_id = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    def __str__(self):
        """A string representation of the model."""
        return self.destination[:50]

    
    

