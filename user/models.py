from django.db import models

class User(models.Model):
    first_name = models.CharField('First Name', max_length=255)
    second_name = models.CharField('Second Name', max_length=255)
    mail = models.EmailField('Email', max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.second_name} {self.mail}"


class Log(models.Model):
    get = 'GET'
    post = 'POST'
    put = 'PUT'
    delete = 'DELETE'
    methods = [
        (get, 'GET'),
        (post, 'POST'),
        (put, 'PUT'),
        (delete, 'DELETE'),
    ]
    path = models.CharField('Path', max_length=255)
    method = models.CharField('Method', choices=methods, default='GET', max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.timestamp}, {self.method}'

    class Meta:
        verbose_name = 'Logs'
