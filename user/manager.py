from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class PersonManager(BaseUserManager):
    def _create_user(
        self,
        email,
        password,
        is_staff,
        is_admin,
        is_superuser,
        **extra_fields
    ):
        if not email:
            raise ValueError("Users must have an email")

        now = timezone.now()
        user = self.model(
            email=email,
            staff=is_staff,
            admin=is_admin,
            superuser=is_superuser,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        user = self._create_user(
            email, password, False, False, False, **extra_fields
        )
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_active", True)
        user = self._create_user(
            email, password, True, True, True, **extra_fields
        )
        return user
