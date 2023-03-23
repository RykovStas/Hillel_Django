from django.db import models

class People(models.Model):
    first_name = models.CharField('First Name')
    last_name = models.CharField('Last Name')
    email_ = models.EmailField('Email')

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email_}"