# permissions.py
from rest_framework import permissions
# from .models import ProjectManager, RegionalManager, Salesman, Farmer, TechSupport
from django.core.exceptions import PermissionDenied

# class CustomObjectPermissions(permissions.DjangoObjectPermissions):
#     """
#     Similar to `DjangoObjectPermissions`, but adding 'view' permissions.
#     """
#     perms_map = {
#         'GET': ['%(app_label)s.view_%(model_name)s'],
#         'OPTIONS': ['%(app_label)s.view_%(model_name)s'],
#         'HEAD': ['%(app_label)s.view_%(model_name)s'],
#         'POST': ['%(app_label)s.add_%(model_name)s'],
#         'PUT': ['%(app_label)s.change_%(model_name)s'],
#         'PATCH': ['%(app_label)s.change_%(model_name)s'],
#         'DELETE': ['%(app_label)s.delete_%(model_name)s'],
#     }

# class IsOwnerOrReadOnly(permissions.BasePermission):
#     """
#     Object-level permission to only allow owners of an object to edit it.
#     Assumes the model instance has an `owner` attribute.
#     """

#     def has_permission(self, request, view):
#         if request.user.is_authenticated:
#             return True
#         return False

#     def has_object_permission(self, request, view, obj):
#         if obj.owner == request.user:
#             return True
#         return False

class FarmPerm(permissions.BasePermission): # farmer crud own farm + salesman crud own farmer farm
   
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj): 
        
        children=request.user.get_all_children()
             
        if obj.owner == request.user:
            return True
        elif obj.owner in children:
            return True
        return False
   
  
class UserPerm(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.role == 'FM':
            return True
        elif request.method in request.method in permissions.SAFE_METHODS:
            return True
        else :
            return False
   
    def has_object_permission(self, request, view, obj): 
        
        children=request.user.get_all_children()
             
        if obj.manager == request.user:
            return True
        elif obj.manager in children:
            return True
        return False

 
# class RegionalManagerPerm(permissions.BasePermission):
#     def has_permission(self, request, view):

#         if RegionalManager.objects.filter(user_id=request.user).exists() and request.method in permissions.SAFE_METHODS:
#             return True 
#         elif ProjectManager.objects.filter(user_id=request.user).exists():
#             return True
       
#     def has_object_permission(self, request, view, obj):
        
#         if RegionalManager.objects.filter(user_id=request.user).exists():
#             if obj.user == request.user:
#                 return True
#             else:
#                 raise PermissionDenied()
#         elif ProjectManager.objects.filter(user_id=request.user).exists():
#             if obj.parent.user == request.user:
#                 return True
#             else:
#                 raise PermissionDenied()
#         else:
#             raise PermissionDenied()

