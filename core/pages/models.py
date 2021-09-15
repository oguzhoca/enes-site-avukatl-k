from django.db import models

class Contact(models.Model):
    Adınız = models.CharField(max_length=100)
    Soyadınız = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Telefonunuz = models.CharField(max_length=100)
    Mesajınız = models.TextField(blank=True)

    def __str__(self):
        return self.Adınız
