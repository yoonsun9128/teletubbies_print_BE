from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
import store
from store.models import Filter
class UserManager(BaseUserManager):
    def create_user(self, email, username, phone_number, address, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username = username,
            phone_number = phone_number,
            address = address
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('username', True)
        extra_fields.setdefault('phone_number', True)
        extra_fields.setdefault('address', True)
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    username = models.CharField(max_length=100)
    phone_number = models.IntegerField(blank=True)
    address = models.CharField(max_length=100)
    reward = models.IntegerField(blank=True, default=0)
    

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    extra_kwargs = {
        'reword' : False
    }
    
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    filter_option = models.ForeignKey('store.Filter_option', on_delete=models.CASCADE)
    # order_number = models.IntegerField() 필요없을듯? order_id로 쓰면될듯
    total_order_price = models.IntegerField()
    order_reward = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    filter_option = models.ForeignKey('store.Filter_option', on_delete=models.CASCADE)
    # image = models.ForeignKey(Image, on_delete=models.CASCADE)   
    