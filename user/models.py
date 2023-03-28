from django.db import models

class User(models.Model):
    first_name = models.CharField('First Name', max_length= 255)
    second_name = models.CharField('Second Name', max_length=255)
    mail = models.EmailField('Email', max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.second_name} {self.mail}"