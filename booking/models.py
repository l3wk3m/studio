import uuid
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

TIME_CHOICES = (
    ("9am to 12pm", "9am to 12pm"),
    ("12pm to 3pm", "12pm to 3pm"),
    ("3pm to 6pm", "3pm to 6pm"),
)

# Artist model extending base user model
class Artist(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(User, null=True, blank=True)
    contact_phone = models.CharField(max_length=15, null=True, blank=True)
    
    def __str__(self):
            return f"{self.first_name + ' ' + self.last_name + ', username: ' + self.username}"

class Studio(models.Model):
    """
    Django database model for studio spaces
    """
    studio_id = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.name
  

class StudioBooking(models.Model):
    """
    Django database model for available studios
    """
    booking_id = models.CharField(max_length=32, null=False, editable=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booking_time = models.CharField(max_length=12, choices=TIME_CHOICES, default="9am to 12pm")
    created_on = models.DateTimeField(auto_now=True)

    def _generate_booking_id(self):
        """
        Generate a random, unique booking id using UUID
        """
        return uuid.uuid4().hex.upper()

    def __str__(self):
        # formatted_start_time = self.start_time.strftime('%Y-%m-%d %H:%M')
        return f"{self.artist.username} | {self.studio} | {self.booking_date} at {self.booking_time}"