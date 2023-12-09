from django.db import models


class Category(models.Model):
    SNEAKERS = 'SNEAKERS'
    BOOTS = 'BOOTS'
    SANDALS = 'SANDALS'
    SLIPPERS = 'SLIPPERS'
    OTHER = 'OTHER'

    CATEGORY_CHOICES = [
        (SNEAKERS, 'SNEAKERS'),
        (BOOTS, 'BOOTS'),
        (SANDALS, 'SANDALS'),
        (SLIPPERS, 'SLIPPERS'),
        (OTHER, 'OTHER'),
    ]
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='OTHER')

    @staticmethod
    def get_all_categories():
        return Category.objects.all()
