from django.urls import path, include
from employee import views
# from rest_framework import routers, urlpatterns

# router = routers.DefaultRouter()
# router.register('employee', views.ListEmployeeAPIView)
# router.register('designation', views.ListDesignationAPIView)

urlpatterns = [
    path("",views.ListEmployeeAPIView.as_view(),name="employee_list"),
    path("create/", views.CreateEmployeeAPIView.as_view(),name="employee_create"),
    path("update/<int:pk>/",views.UpdateEmployeeAPIView.as_view(),name="update_employee"),
    path("delete/<int:pk>/",views.DeleteEmployeeAPIView.as_view(),name="delete_employee"),

    path("designation/",views.ListDesignationAPIView.as_view(),name="designation_list"),
    path("designation/create/", views.CreateDesignationAPIView.as_view(),name="designation_create"),
    path("designation/update/<int:pk>/",views.UpdateDesignationAPIView.as_view(),name="update_designation"),
    path("designation/delete/<int:pk>/",views.DeleteDesignationAPIView.as_view(),name="delete_designation"),

    path("location/",views.ListLocationAPIView.as_view(),name="location_list"),
    path("location/create/", views.CreateLocationAPIView.as_view(),name="location_create"),
    path("location/update/<int:pk>/",views.UpdateLocationAPIView.as_view(),name="update_location"),
    path("location/delete/<int:pk>/",views.DeleteLocationAPIView.as_view(),name="delete_location"),
    
    path("country/",views.ListCountryAPIView.as_view(),name="country_list"),
    path("country/create/", views.CreateCountryAPIView.as_view(),name="country_create"),
    path("country/update/<int:pk>/",views.UpdateCountryAPIView.as_view(),name="update_country"),
    path("country/delete/<int:pk>/",views.DeleteCountryAPIView.as_view(),name="delete_country"),
    
    path("company/",views.ListCompanyAPIView.as_view(),name="company_list"),
    path("company/create/", views.CreateCompanyAPIView.as_view(),name="company_create"),
    path("company/update/<int:pk>/",views.UpdateCompanyAPIView.as_view(),name="update_company"),
    path("company/delete/<int:pk>/",views.DeleteCompanyAPIView.as_view(),name="delete_company"),
    
    path("department/",views.ListDepartmentAPIView.as_view(),name="department_list"),
    path("department/create/", views.CreateDepartmentAPIView.as_view(),name="department_create"),
    path("department/update/<int:pk>/",views.UpdateDepartmentAPIView.as_view(),name="update_department"),
    path("department/delete/<int:pk>/",views.DeleteDepartmentAPIView.as_view(),name="delete_department"),
    
    # path("department/",views.ListSubdepartmentAPIView.as_view(),name="department_list"),
    # path("department/create/", views.CreateSubdepartmentAPIView.as_view(),name="department_create"),
    # path("department/update/<int:pk>/",views.UpdateSubdepartmentAPIView.as_view(),name="update_department"),
    # path("department/delete/<int:pk>/",views.DeleteSubdepartmentAPIView.as_view(),name="delete_department"),
    
    path("office_shift/",views.ListOfficeShiftAPIView.as_view(),name="Office_shift_list"),
    path("office_shift/create/", views.CreateOfficeShiftAPIView.as_view(),name="Office_shift_create"),
    path("office_shift/update/<int:pk>/",views.UpdateOfficeShiftAPIView.as_view(),name="update_Office_shift"),
    path("office_shift/delete/<int:pk>/",views.DeleteOfficeShiftAPIView.as_view(),name="delete_Office_shift"),
    
    path("relation/",views.ListRelationAPIView.as_view(),name="Relation_list"),
    path("relation/create/", views.CreateRelationAPIView.as_view(),name="Relation_create"),
    path("relation/update/<int:pk>/",views.UpdateRelationAPIView.as_view(),name="update_Relation"),
    path("relation/delete/<int:pk>/",views.DeleteRelationAPIView.as_view(),name="delete_Relation"),
    
    path("emp-emergency-contacts/",views.ListEmpEmergencyContactsAPIView.as_view(),name="EmpEmergencyContacts_list"),
    path("emp-emergency-contacts/create/", views.CreateEmpEmergencyContactsAPIView.as_view(),name="EmpEmergencyContacts_create"),
    path("emp-emergency-contacts/update/<int:pk>/",views.UpdateEmpEmergencyContactsAPIView.as_view(),name="update_EmpEmergencyContacts"),
    path("emp-emergency-contacts/delete/<int:pk>/",views.DeleteEmpEmergencyContactsAPIView.as_view(),name="delete_EmpEmergencyContacts"),
    
    path("emp-social-network/",views.ListEmpSocialNetworkAPIView.as_view(),name="EmpSocialNetwork_list"),
    path("emp-social-network/create/", views.CreateEmpSocialNetworkAPIView.as_view(),name="EmpSocialNetwork_create"),
    path("emp-social-network/update/<int:pk>/",views.UpdateEmpSocialNetworkAPIView.as_view(),name="update_EmpSocialNetwork"),
    path("emp-social-network/delete/<int:pk>/",views.DeleteEmpSocialNetworkAPIView.as_view(),name="delete_EmpSocialNetwork"),
    
    
    
    
]