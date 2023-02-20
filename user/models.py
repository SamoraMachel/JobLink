from django.db import models
from typing import List

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import PersonManager
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254)
    date_joined = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    superuser = models.BooleanField(default=False)
    
    # Social Media
    twitter = models.CharField(_("twitter"), max_length=150, null=True, blank=True)
    instagram = models.CharField(_("instagram"), max_length=150, null=True, blank=True)
    facebook = models.CharField(_("facebook"), max_length=150, null=True, blank=True)
    linkedin = models.CharField(_("linkein"), max_length=150, null=True, blank=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: List[str] = ["email"]

    objects = PersonManager()

    def __str__(self) -> str:
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def clean(self):
        pass

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_superuser(self):
        return self.superuser
    

class Company(CustomUser):
    company_name = models.CharField(_("company_name"), max_length=100)
    company_image = models.CharField(_("company_image"), max_length=200)
    website = models.CharField(_("website"), max_length=150, null=True, blank=True)
    
class User(CustomUser):
    full_name = models.CharField(_("full_name"), max_length=100)
    photo = models.CharField(_("photo"), max_length=200)
    skills = models.CharField(_("skills"), max_length=200, null=True, blank=True)
    education = models.JSONField(_("education"), null=True, blank=True)
    experience = models.JSONField(_("experience"), null=True, blank=True)
    blogs = models.JSONField(_("blogs"), null=True, blank=True)
    tool = models.CharField(_("tools"), max_length=200)
    location = models.CharField(_("location"), max_length=100)
    pay_range = models.CharField(_("pay_range"), max_length=100)
    
