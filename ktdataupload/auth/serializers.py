from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class AuthTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['idUser'] = user.id
        token['name'] = user.first_name + ', ' + user.last_name
        token['idRole'] = 1
        token['role'] = 'Ophthalmologist'
        # ...

        return token