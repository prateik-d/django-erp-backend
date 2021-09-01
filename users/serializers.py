from rest_framework import serializers
from . import models
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('id', 'email', 'username', 'phone')

# class UserSerializer(serializers.ModelSerializer):
    
#     password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

#     class Meta:
#         phone = serializers.CharField()
#         model = models.CustomUser
#         fields = ['username', 'email', 'first_name','last_name', 'password', 'password2', 'phone']
        
#         extra_kwargs = {
#             'password': {
#                 'write_only':True
#             }
#         }

#     def save(self):
#         user = User(
#             email=self.validated_data['email'],
#             username=self.validated_data['username'],
#             first_name=self.validated_data['first_name'],
#             last_name=self.validated_data['last_name'],
#             # is_tutor=self.validated_data['is_tutor'],
#             # is_student=self.validated_data['is_student'],
#         )

#         password = self.validated_data['password']
#         password2 = self.validated_data['password2']

#         if password != password2:
#             raise serializers.ValidationError({'password':'Passwords must match.'})
#         user.set_password(password)
#         user.save()

#         return user