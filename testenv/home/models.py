# myapp/models.py

from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _
from testenv.settings import AUTH_USER_MODEL
# # from .managers import CustomUserManager

from .managers import CustomUserManager

class CustomUser(AbstractUser):
    FARMER = 'FM'
    SALESMAN = 'SM'
    REGIONALMANAGER = 'RMG'
    TECHSUPPORT = 'TSP'
    PROJECTMANAGER = 'PMG'

    USER_TYPES = (
        (FARMER, 'base farmer'),
        (SALESMAN, 'salesman'),
        (TECHSUPPORT, 'tech support'),
        (REGIONALMANAGER, 'regional manager'),
        (PROJECTMANAGER, 'project manager')
    )

    REQUIRED_FIELDS = ['role']

    role = models.CharField(max_length=25, choices=USER_TYPES)
    manager = models.ForeignKey('self', null=True,blank=True, related_name='sub', on_delete=models.CASCADE)
    objects= CustomUserManager()

    def get_all_children(self, include_self=True):
            userlist = []
            if include_self:
                userlist.append(self)
            for users in CustomUser.objects.filter(manager=self):
                _userlist = users.get_all_children(include_self=True)
                if 0 < len(_userlist):
                    userlist.extend(_userlist)
            return userlist
    
    # def is_higher(self,include_self=True):
    #     pass


    def __str__(self):
        return "<{}: {}>".format(self.role, self.username)
    def __repr__(self):
        return self.__str__()


class Farm(models.Model):
    """A marker with name and location."""

    name = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    owner = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='farms')


    def __str__(self):
        """Return string representation."""
        return self.name


class Plot(models.Model):
    """A marker with name and location."""
    id=models.CharField(max_length=255,primary_key=True)
    name = models.CharField(max_length=255)
    rotation=models.CharField(max_length=255)
    # crop=models.CharField(max_length=255)
    # crop_yield=models.CharField(max_length=255)
    farm = models.ForeignKey(Farm, related_name='plots',on_delete=models.CASCADE)

    def __str__(self):
        """Return string representation."""
        return self.name

class DataZone(models.Model):
    plot= models.ForeignKey(Plot, related_name='zones',on_delete=models.CASCADE)
    zone= models.CharField(max_length=255)
    lastYear= models.CharField(max_length=255)
    pH05=models.CharField(max_length=255)
    BEB=models.CharField(max_length=255)
    BEC=models.CharField(max_length=255)
    BEM=models.CharField(max_length=255)
    besoin=models.CharField(max_length=255)
    product=models.CharField(max_length=255)
    apport=models.CharField(max_length=255)
    area=models.CharField(max_length=255)
    productAmount=models.CharField(max_length=255)
    firstYear=models.CharField(max_length=255)
    

