from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    """Client model"""
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return self.name


class FeatureRequest(models.Model):
    """Feature Request model"""
    PRODUCT_AREA_CHOICES = (
                            ('PL', 'Policies'),
                            ('BL', 'Billing'),
                            ('CL', 'Claims'),
                            ('RP', 'Reports')
    )

    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    client = models.ForeignKey('Client')
    priority = models.PositiveSmallIntegerField()
    target_date = models.DateField()
    url = models.URLField()
    product_area = models.CharField(max_length=2, choices=PRODUCT_AREA_CHOICES)

    class Meta:
        verbose_name = "Feature Request"
        verbose_name_plural = "Feature Requests"

    def __str__(self):
        return self.title
    