from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class Hghghgh(models.Model):
    "Generated Model"
    fgasdg = models.BigIntegerField()
    dfgsfs = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="hghghgh_dfgsfs",
    )
    dfssdgsdf = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="hghghgh_dfssdgsdf",
    )
    sfdgsdfg = models.ManyToManyField(
        "home.Hghghgh", blank=True, related_name="hghghgh_sfdgsdfg",
    )
