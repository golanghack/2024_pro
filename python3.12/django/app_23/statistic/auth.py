from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from models import UserProfile 

def get_user_id_from_token(token):
    try:
        validated_token = JWTAuthentication().get_validated_token(token)
        user_id = validated_token['user_id']  
        return user_id
    except Exception as e:
        raise AuthenticationFailed('Invalid token')
    
def save_user_id(user_id):
       user, created = UserProfile.objects.get_or_create(user_id=user_id)
       return user    
   
def check_user_id(token):
       user_id = get_user_id_from_token(token)
       user = UserProfile.objects.filter(user_id=user_id).first()
       if user:
           return user 
       else:
           return None  