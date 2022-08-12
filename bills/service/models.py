from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Bills(models.Model):
    client_name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bills')
    client_org = models.TextField()
    account_number = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    date = models.DateTimeField()
    service = models.TextField()

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.service
