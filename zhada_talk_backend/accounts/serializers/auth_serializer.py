from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            request = self.context.get('request')
            user = authenticate(request=request, email=email, password=password)

        if not user:
            raise serializers.ValidationError("Invalid email or password.")

        if getattr(user, "is_locked", False):
            raise serializers.ValidationError("Your account is locked due to too many failed attempts.")

        # Return a dict containing the user
        return {"user": user}


# -----------------------------------------
# Registration Serializer — extending dj-rest-auth
# -----------------------------------------
class CustomRegisterSerializer(RegisterSerializer):
    username = None 
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    middle_name = serializers.CharField(required=False, allow_blank=True)
    gender = serializers.ChoiceField(choices=(("M", "Male"), ("F", "Female"), ("O", "Other")))
    age = serializers.IntegerField(required=True)

    def get_cleaned_data(self):
        cleaned = super().get_cleaned_data()
        cleaned.update({
            "first_name": self.validated_data.get("first_name"),
            "last_name": self.validated_data.get("last_name"),
            "middle_name": self.validated_data.get("middle_name", ""),
            "gender": self.validated_data.get("gender"),
            "age": self.validated_data.get("age"),
        })
        return cleaned


# -----------------------------------------
# Password Change
# -----------------------------------------
class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value
