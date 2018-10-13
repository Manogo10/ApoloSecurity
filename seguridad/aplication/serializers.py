from aplication.models import Usuario
from django.contrib.auth.models import User
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True, source="user.username")
    password = serializers.CharField(write_only=True, source="user.password")
    nombre = serializers.CharField(required=False)
    apellido = serializers.CharField(required=False)
    cedula = serializers.CharField(required=False)    
    email = serializers.CharField(required=False)
   
    #category_name = serializers.RelatedField(source='category',read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'nombre', 'apellido', 'cedula', 'email')
    def create(self, validated_data, instance=None):
        print("Entramos//////////////////////////////////////")
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        user.set_password(user_data['password'])
        user.save()
        Usuario.objects.update_or_create(user=user,**validated_data)
        usuario = Usuario.objects.get(user=user)
        return usuario