from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser, PermissionsMixin




class CustomUser(AbstractUser):
# class CustomUser(AbstractBaseUser, PermissionsMixin):
    

    # email = models.EmailField(
    #     verbose_name='email address',
    #     max_length=255,
    #     unique=True,
    # )

    # username = models.CharField(blank=False, unique=True, max_length=255)

    # is_active = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=False) # an admin user; non super-user
    # is_admin = models.BooleanField(default=False) # a superuser

    name = models.CharField(blank=True, max_length=255)
    phone = models.CharField(blank=True, max_length=255)

    # USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email   


# class MyUserManager(BaseUserManager):
#     def create_user(self, email, username,first_name, last_name, password=None):
#         user = self.model(
#             email=self.normalize_email(email),
#             username=username,
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self,email, username, password, first_name, last_name):
#         user = self.create_user(
#             email=self.normalize_email(email),
#             username=username,
#             password=password,
#             first_name=first_name,
#             last_name=last_name,
#         )

#         user.is_staff = True
#         user.is_admin = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user

# class CustomUser(AbstractBaseUser):
#     email =             models.EmailField(verbose_name='email', max_length=60, unique=True)
#     username =          models.CharField(max_length=30, unique=True)
#     date_joined =       models.DateField(verbose_name='date joined', auto_now_add=True)
#     last_login =        models.DateField(verbose_name='last login', auto_now=True)
#     is_admin =          models.BooleanField(default=False)
#     is_active =         models.BooleanField(default=True)
#     is_staff =          models.BooleanField(default=False)
#     is_superuser =      models.BooleanField(default=False)
#     rating =            models.FloatField(default=0, blank=True, null=True)
#     reviews_count =     models.IntegerField(default=0)
#     first_name =        models.CharField(verbose_name='first_name', max_length=30, blank=True)
#     last_name =         models.CharField(verbose_name='last_name', max_length=30,blank=True)
#     phone = models.CharField(blank=True, max_length=255)

#     USERNAME_FIELD = 'email' 
#     #this field means that when you try to sign in the username field will be the email 
#     #change it to whatever you want django to see as the username when authenticating the user
#     REQUIRED_FIELDS = ['username', 'first_name', 'last_name',]

#     objects = MyUserManager()

#     def __str__(self):
#         return self.first_name + ' - ' + self.email

#     def has_perm(self, perm, obj=None):
#         return self.is_admin

#     def has_module_perms(self, app_label):
#         return True