from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create profile model to extend the existent user model
class Profile(models.Model):
    # CASCADE means that if the user is delete it also deletes the profile.
    #  But if you delete the profile you do not delete the user
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #Add an profile image and save it in the profile_pics directory
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    #overwrite the save method to resize images on upload
    def save(self):
        super().save()
        
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


