from django.contrib.auth.models import User
from rest_framework import serializers
# from testenv.home.models import Farm, Farmer, Plot, ProjectManager, RegionalManager, Salesman, TechSupport
from rest_framework import exceptions
from django.core.exceptions import PermissionDenied
from testenv.home.models import CustomUser, Farm,Plot

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username','role','manager', 'first_name', 'last_name')

    def validate(self, data):   
      
        parent_entity = data['manager']
        children=self.context['request'].user.get_all_children()
       
       
            # raise Exception(self.context['request'].user.role ==('FM' or 'PMG' or 'TSP'))
        if parent_entity == self.context['request'].user:
                return data
        if parent_entity in children:
            return data
        else:
            raise PermissionDenied()

# class ProjectManagerSerializer(serializers.HyperlinkedModelSerializer):
#     user=UserSerializer(required=True)
#     class Meta:
#         model = ProjectManager
#         fields = ['name','user']
    
#     # def create(self, validated_data):
#     #     """
#     #     Overriding the default create method of the Model serializer.
#     #     :param validated_data: data containing all the details of student
#     #     :return: returns a successfully created student record
#     #     """
#     #     user_data = validated_data.pop('user')
#     #     user = UserSerializer.create(UserSerializer(), validated_data=user_data)
#     #     projectmanager, created = ProjectManager.objects.update_or_create(user=user, parent=validated_data.pop('parent'))
#     #     return projectmanager

# class TechSupportSerializer(serializers.HyperlinkedModelSerializer):
    
#     class Meta:
#         model = TechSupport
#         fields = ['name']

# class RegionalManagerSerializer(serializers.HyperlinkedModelSerializer):
#     user=UserSerializer(required=True)
#     class Meta:
#         model = RegionalManager
#         fields = ['name','parent','user']

#     def create(self, validated_data):
#         """
#         Overriding the default create method of the Model serializer.
#         :param validated_data: data containing all the details of student
#         :return: returns a successfully created student record
#         """
#         user_data = validated_data.pop('user')
#         user = UserSerializer.create(UserSerializer(), validated_data=user_data)
#         regionalmanager, created = RegionalManager.objects.update_or_create(user=user,name=validated_data.pop('name'), parent=validated_data.pop('parent'))
#         return regionalmanager

#     def validate(self, data):   
      
#         parent_entity = data['parent']
        
#         if parent_entity.user == self.context['request'].user:
#             return data
#         else:
#             raise PermissionDenied()

# class SalesmanSerializer(serializers.HyperlinkedModelSerializer):
#     # parent=RegionalManagerSerializer(many=True, required=True)
#     user=UserSerializer(required=True)
#     class Meta:
#         model = Salesman
#         fields = ['name','parent','user']
    
#     def create(self, validated_data):
#         """
#         Overriding the default create method of the Model serializer.
#         :param validated_data: data containing all the details of student
#         :return: returns a successfully created student record
#         """
#         user_data = validated_data.pop('user')
#         user = UserSerializer.create(UserSerializer(), validated_data=user_data)
#         salesman, created = Salesman.objects.update_or_create(user=user,name=validated_data.pop('name'), parent=validated_data.pop('parent'))
#         return salesman

#     def validate(self, data):   
      
#         parent_entity = data['parent']
        
#         if parent_entity.user == self.context['request'].user:
#             return data
#         elif parent_entity.parent.user ==self.context['request'].user:
#             return data
#         else:
#             raise PermissionDenied()

# class FarmerSerializer(serializers.HyperlinkedModelSerializer):
#     user=UserSerializer(required=True)
#     class Meta:
#         model = Farmer
#         fields = ['name','parent','user']

#     def create(self, validated_data):
#         """
#         Overriding the default create method of the Model serializer.
#         :param validated_data: data containing all the details of student
#         :return: returns a successfully created student record
#         """
#         user_data = validated_data.pop('user')
#         user = UserSerializer.create(UserSerializer(), validated_data=user_data)
#         farmer, created = Farmer.objects.update_or_create(user=user,name=validated_data.pop('name'), parent=validated_data.pop('parent'))
#         return farmer

#     def validate(self, data):   
      
#         parent_entity = data['parent']
        
#         if parent_entity.user == self.context['request'].user:
#             return data
#         elif parent_entity.parent.user ==self.context['request'].user:
#             return data
#         elif parent_entity.parent.parent.user ==self.context['request'].user:
#             return data
#         else:
#             raise PermissionDenied()

class PlotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plot
        fields = ['name','rotation']

class FarmSerializer(serializers.HyperlinkedModelSerializer):
    # owner = UserSerializer(required=True)
    plots=PlotSerializer(many=True, required=False)
    
    class Meta:
        model = Farm
        fields = ['name','adress','plots','owner']
    
    def validate(self, data):   
      
        parent_entity = data['owner']
        children=self.context['request'].user.get_all_children()
       
       
            # raise Exception(self.context['request'].user.role ==('FM' or 'PMG' or 'TSP'))
        if parent_entity == self.context['request'].user:
            if self.context['request'].user.role ==('FM' or 'PMG' or 'TSP'):
                return data
            else:
                raise PermissionDenied()
        elif parent_entity in children:
            if parent_entity.role ==('FM' or 'PMG' or 'TSP'):
                return data
            else:
                raise PermissionDenied()
        else:
            raise PermissionDenied()
        

        # elif Salesman.objects.filter(user_id=parent_entity.parent).exists():
        #     if parent_entity.parent.user == self.context['request'].parent.user:
        #         return data
        #     else:
        #         raise exceptions.NotAcceptable(detail=None, code=None)
        # else:
        #     raise exceptions.NotAcceptable(detail=None, code=None)

