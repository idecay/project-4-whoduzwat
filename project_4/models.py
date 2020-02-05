from django.db import models


class FamilyMember(models.Model):
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, default='username', blank=True)
    password = models.CharField(max_length=100, default ='password', blank=True)
    is_parent = models.BooleanField(default=False)
    profile_image = models.TextField(default='', blank=True)


class Family(models.Model):
    family_name = models.CharField(max_length=100)
    family_members = models.ForeignKey(FamilyMember, on_delete=models.CASCADE, related_name="family_members")


class Chore(models.Model):
    task = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default='', blank=True)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    image_url = models.TextField(default='', blank=True)
    person_responsible = models.ForeignKey(
        FamilyMember,
        models.SET_NULL,
        blank=True,
        null=True,
        related_name="family_member")
    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name="family")



