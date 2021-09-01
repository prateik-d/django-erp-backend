from django.db import models

# Create your models here.

class Designation(models.Model):
    title = models.CharField(max_length = 100)
    desc = models.TextField()
    active = models.BooleanField(default=True)
    date_created = models.DateField(auto_created=True)
    last_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

class Country(models.Model):
    name = models.CharField(max_length = 255, unique=True)
    active = models.BooleanField(default=True)
    date_created = models.DateField(auto_created=True)
    last_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    city = models.CharField(max_length = 100)
    # country = models.CharField(max_length = 100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country',  null=True,  blank=True)
    desc = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    date_created = models.DateField(auto_created=True)
    last_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.city
        
class Company(models.Model):
    name = models.CharField(max_length = 255)
    active = models.BooleanField(default=True)
    date_created = models.DateField(auto_created=True)
    last_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
        
class Department(models.Model):
    title = models.CharField(max_length = 100)
    desc = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    date_created = models.DateField(auto_created=True)
    last_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

        
# class Subdepartment(models.Model):
#     department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department',  null=True,  blank=True)
#     title = models.CharField(max_length = 100)
#     desc = models.TextField(null=True, blank=True)
#     active = models.BooleanField(default=True)
#     date_created = models.DateField(auto_created=True)
#     last_modified = models.DateField(auto_now=True)

#     def __str__(self):
#         return self.title

class Office_shift(models.Model):
    name = models.CharField(max_length = 255)
    starting_time = models.TimeField(auto_now=False, auto_now_add=False)
    closing_time = models.TimeField(auto_now=False, auto_now_add=False)
    active = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    def __str__(self):
        # return self.name + ' - ' + self.starting_time  + ' - ' + self.closing_time
        # return {self.name} - {self.starting_time} - {self.closing_time}
        return self.name 


   
class Employee(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length = 100)
    gender  = models.CharField(max_length = 100)
    marital_status  = models.CharField(max_length = 100, null=True)
    
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE, related_name='designations',  null=True,  blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='location',  null=True,  blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company',  null=True,  blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department',  null=True,  blank=True)
    # subdepartment = models.ForeignKey(Subdepartment, on_delete=models.CASCADE, related_name='subdepartment',  null=True,  blank=True)
    office_shift = models.ForeignKey(Office_shift, on_delete=models.CASCADE, related_name='office_shift',  null=True,  blank=True)
    # reports_to = models.ForeignKey("self", on_delete=models.PROTECT,  null=True, blank=True)

    # designation = models.CharField(max_length = 100, null=True)
    # location = models.CharField(max_length = 100, null=True)
    # company = models.CharField(max_length = 100, null=True)
    # department = models.CharField(max_length = 100, null=True)

    sub_department = models.CharField(max_length = 100, null=True, blank=True)
    # office_shift = models.CharField(max_length = 100, null=True)
    # reports_to = models.CharField(max_length = 100, null=True)


    active = models.BooleanField(default=True)
    
    doj = models.DateField(null=True)
    dob = models.DateField(null=True)
    
    date_created = models.DateField(auto_now=True)
    last_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.name



class Relation(models.Model):
    title = models.CharField(max_length = 255, unique=True)
    desc = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    date_created = models.DateField(auto_now=True)
    last_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

# emp_emergency_contacts	

class EmpEmergencyContacts(models.Model):
    emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employees',  null=True,  blank=True)
    relation = models.ForeignKey(Relation, on_delete=models.CASCADE, related_name='relation',  null=True,  blank=True)
    name = models.CharField(max_length = 100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length = 100)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, related_name='countries',  null=True,  blank=True)
    zip = models.CharField(max_length = 100)
    date_created = models.DateField(auto_now=True)
    last_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

# emp_social_networking

class EmpSocialNetwork(models.Model):
    emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee_social_network',  null=True,  blank=True)
    fb = models.TextField(null=True, blank=True)
    twitter = models.TextField(null=True, blank=True)
    linkedin = models.TextField(null=True, blank=True)
    insta = models.TextField(null=True, blank=True)
    youtube = models.TextField(null=True, blank=True)
    date_created = models.DateField(auto_now=True)
    last_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.emp_id

