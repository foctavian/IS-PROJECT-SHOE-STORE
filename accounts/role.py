from django.db import models


class Role(models.Model):
    CUSTOMER = 1
    GUEST = 2
    SELLER = 3
    ADMIN = 4

    ROLE_CHOICES = (
        (CUSTOMER, "customer"),
        (GUEST, "guest"),
        (SELLER, "seller"),
        (ADMIN, "admin")
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()
