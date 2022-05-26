from rest_framework import serializers 
from userCRUD.models import User
 
 
class UserSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = User
        fields = ('id',
                  'name',
                  'username',
                  'age',
                  'dob')