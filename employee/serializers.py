from rest_framework import serializers
from .models import Employee, Designation, Location, Country, Company, Department, Office_shift, Relation, EmpEmergencyContacts, EmpSocialNetwork

class EmployeeSerializer(serializers.ModelSerializer):

    # designation = serializers.SlugRelatedField(
    #     many=True, 
    #     read_only=True,
    #     slug_field="title"
    # )
    class Meta:
        model = Employee
        fields = "__all__"
        

class DesignationSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(many=True, read_only=True)    
    class Meta:
        model = Designation
        fields = "__all__"



class LocationSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(many=True, read_only=True)    
    class Meta:
        model = Location
        fields = "__all__"


class CountrySerializer(serializers.ModelSerializer):
    employee = LocationSerializer(many=True, read_only=True)    
    class Meta:
        model = Country
        fields = "__all__"
    

class CompanySerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(many=True, read_only=True)    
    class Meta:
        model = Company
        fields = "__all__"
    
class DepartmentSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(many=True, read_only=True)    
    class Meta:
        model = Department
        fields = "__all__"
    
# class SubdepartmentSerializer(serializers.ModelSerializer):
#     employee = EmployeeSerializer(many=True, read_only=True)    
#     class Meta:
#         model = Subdepartment
#         fields = "__all__"

   
class OfficeshiftSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(many=True, read_only=True)    
    class Meta:
        model = Office_shift
        fields = "__all__"

class RelationSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(many=True, read_only=True)    
    class Meta:
        model = Relation
        fields = "__all__"


class EmpEmergencyContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpEmergencyContacts
        fields = "__all__"

class EmpSocialNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpSocialNetwork
        fields = "__all__"
    



    