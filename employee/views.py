from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from employee.serializers import EmployeeSerializer, DesignationSerializer, LocationSerializer, CountrySerializer, CompanySerializer, DepartmentSerializer, OfficeshiftSerializer, RelationSerializer, EmpEmergencyContactSerializer, EmpSocialNetworkSerializer
from employee.models import Employee, Designation, Location, Country, Company, Department, Office_shift, Relation, EmpEmergencyContacts, EmpSocialNetwork

# Create your views here.
class ListEmployeeAPIView(ListAPIView):
    """This endpoint list all of the available Employees from the database"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class CreateEmployeeAPIView(CreateAPIView):
    """This endpoint allows for creation of a Employee"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class UpdateEmployeeAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific Employee by passing in the id of the Employee to update"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DeleteEmployeeAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Employee from the database"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# ------------------------
# Designation 
# ------------------------

class ListDesignationAPIView(ListAPIView):
    """This endpoint list all of the available Designations from the database"""
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer

class CreateDesignationAPIView(CreateAPIView):
    """This endpoint allows for creation of a Designation"""
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer

class UpdateDesignationAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific Designation by passing in the id of the Designation to update"""
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer

class DeleteDesignationAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Designation from the database"""
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer

# ------------------------
# Location 
# ------------------------

class ListLocationAPIView(ListAPIView):
    """This endpoint list all of the available Locations from the database"""
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class CreateLocationAPIView(CreateAPIView):
    """This endpoint allows for creation of a Location"""
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class UpdateLocationAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific Location by passing in the id of the Location to update"""
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class DeleteLocationAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Location from the database"""
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

# ------------------------
# Country 
# ------------------------

class ListCountryAPIView(ListAPIView):
    """This endpoint list all of the available Countrys from the database"""
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CreateCountryAPIView(CreateAPIView):
    """This endpoint allows for creation of a Country"""
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class UpdateCountryAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific Country by passing in the id of the Country to update"""
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class DeleteCountryAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Country from the database"""
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

# ------------------------
# Company 
# ------------------------

class ListCompanyAPIView(ListAPIView):
    """This endpoint list all of the available Companys from the database"""
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CreateCompanyAPIView(CreateAPIView):
    """This endpoint allows for creation of a Company"""
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class UpdateCompanyAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific Company by passing in the id of the Company to update"""
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class DeleteCompanyAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Company from the database"""
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


# ------------------------
# Department 
# ------------------------

class ListDepartmentAPIView(ListAPIView):
    """This endpoint list all of the available Departments from the database"""
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class CreateDepartmentAPIView(CreateAPIView):
    """This endpoint allows for creation of a Department"""
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class UpdateDepartmentAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific Department by passing in the id of the Department to update"""
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DeleteDepartmentAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Department from the database"""
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

# ------------------------
# Subdepartment 
# ------------------------

# class ListSubdepartmentAPIView(ListAPIView):
#     """This endpoint list all of the available Subdepartments from the database"""
#     queryset = Subdepartment.objects.all()
#     serializer_class = SubdepartmentSerializer

# class CreateSubdepartmentAPIView(CreateAPIView):
#     """This endpoint allows for creation of a Subdepartment"""
#     queryset = Subdepartment.objects.all()
#     serializer_class = SubdepartmentSerializer

# class UpdateSubdepartmentAPIView(UpdateAPIView):
#     """This endpoint allows for updating a specific Subdepartment by passing in the id of the Subdepartment to update"""
#     queryset = Subdepartment.objects.all()
#     serializer_class = SubdepartmentSerializer

# class DeleteSubdepartmentAPIView(DestroyAPIView):
#     """This endpoint allows for deletion of a specific Subdepartment from the database"""
#     queryset = Subdepartment.objects.all()
#     serializer_class = SubdepartmentSerializer


# ------------------------
# Office_shift 
# ------------------------

class ListOfficeShiftAPIView(ListAPIView):
    """This endpoint list all of the available Office_shifts from the database"""
    queryset = Office_shift.objects.all()
    serializer_class = OfficeshiftSerializer

class CreateOfficeShiftAPIView(CreateAPIView):
    """This endpoint allows for creation of a Office_shift"""
    queryset = Office_shift.objects.all()
    serializer_class = OfficeshiftSerializer

class UpdateOfficeShiftAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific Office_shift by passing in the id of the Office_shift to update"""
    queryset = Office_shift.objects.all()
    serializer_class = OfficeshiftSerializer

class DeleteOfficeShiftAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Office_shift from the database"""
    queryset = Office_shift.objects.all()
    serializer_class = OfficeshiftSerializer


# ------------------------
# Relation 
# ------------------------

class ListRelationAPIView(ListAPIView):
    """This endpoint list all of the available Relation from the database"""
    queryset =  Relation.objects.all()
    serializer_class = RelationSerializer

class CreateRelationAPIView(CreateAPIView):
    """This endpoint allows for creation of a Relation by passing in the id of the Relation to update"""
    queryset = Relation.objects.all()
    serializer_class = RelationSerializer

class UpdateRelationAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific Relation by passing in the id of the Relation to update"""
    queryset = Relation.objects.all()
    serializer_class = RelationSerializer

class DeleteRelationAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Relation from the database"""
    queryset = Relation.objects.all()
    serializer_class = RelationSerializer


# ------------------------
# EmpEmergencyContacts 
# ------------------------

class ListEmpEmergencyContactsAPIView(ListAPIView):
    """This endpoint list all of the available EmpEmergencyContacts from the database"""
    queryset =  EmpEmergencyContacts.objects.all()
    serializer_class = EmpEmergencyContactSerializer

class CreateEmpEmergencyContactsAPIView(CreateAPIView):
    """This endpoint allows for creation of a EmpEmergencyContacts by passing in the id of the EmpEmergencyContacts to update"""
    queryset = EmpEmergencyContacts.objects.all()
    serializer_class = EmpEmergencyContactSerializer

class UpdateEmpEmergencyContactsAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific EmpEmergencyContacts by passing in the id of the EmpEmergencyContacts to update"""
    queryset = EmpEmergencyContacts.objects.all()
    serializer_class = EmpEmergencyContactSerializer

class DeleteEmpEmergencyContactsAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific EmpEmergencyContacts from the database"""
    queryset = EmpEmergencyContacts.objects.all()
    serializer_class = EmpEmergencyContactSerializer


# ------------------------
# EmpSocialNetwork 
# ------------------------

class ListEmpSocialNetworkAPIView(ListAPIView):
    """This endpoint list all of the available EmpSocialNetwork from the database"""
    queryset =  EmpSocialNetwork.objects.all()
    serializer_class = EmpSocialNetworkSerializer

class CreateEmpSocialNetworkAPIView(CreateAPIView):
    """This endpoint allows for creation of a EmpSocialNetwork by passing in the id of the EmpSocialNetwork to update"""
    queryset = EmpSocialNetwork.objects.all()
    serializer_class = EmpSocialNetworkSerializer

class UpdateEmpSocialNetworkAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific EmpSocialNetwork by passing in the id of the EmpSocialNetwork to update"""
    queryset = EmpSocialNetwork.objects.all()
    serializer_class = EmpSocialNetworkSerializer

class DeleteEmpSocialNetworkAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific EmpSocialNetwork from the database"""
    queryset = EmpSocialNetwork.objects.all()
    serializer_class = EmpSocialNetworkSerializer

