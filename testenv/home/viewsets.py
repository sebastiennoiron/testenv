
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Permission, User, Group
# ViewSets define the view behavior.
# from testenv.home.models import Farm,Plot,Farmer, ProjectManager, RegionalManager, Salesman, TechSupport
from rest_framework import viewsets

from testenv.home.permissions import FarmPerm,UserPerm

# from testenv.home.permissions import FarmPerm, IsOwnerOrReadOnly, ProjectManagerPerm, RegionalManagerPerm, SalesmanPerm,OnlySalesman, OnlyTechSupport, FarmerPerm
from .decorators import farmer_required
# from testenv.home.serializers import FarmSerializer, PlotSerializer, FarmerSerializer, ProjectManagerSerializer, SalesmanSerializer,TechSupportSerializer,RegionalManagerSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from testenv.home.models import CustomUser, Farm,Plot
from testenv.home.serializers import FarmSerializer, PlotSerializer,UserSerializer
from django.db.models import F, Q, When

class UserViewSet(viewsets.ModelViewSet):
  
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    permission_classes=[UserPerm]
    
    # def get_queryset(self):
        
    #     return self.request.user.get_all_children()


class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
    permission_classes = [FarmPerm]


    def get_queryset(self):
        children=self.request.user.get_all_children()
        Farmlist=Farm.objects.none()
        for c in children:
            Farmlist|=Farm.objects.filter(owner=c)
        return Farmlist
 
        
        # def get_farms(user,FarmQuery):
            
           
        #     if user.farms.exists():
        #         FarmQuery |= user.farms
            
        #     if user.sub.exists():
        #         userlist=user.sub.all()
        #         for subs in userlist:
        #             FarmQuery=get_farms(subs,FarmQuery)
        #     else:
        #         return FarmQuery
                
        # return get_farms(user,FarmQuery)

          
     
class PlotViewSet(viewsets.ModelViewSet):
    queryset = Plot.objects.all()
    serializer_class = PlotSerializer
    permission_classes=[]

   