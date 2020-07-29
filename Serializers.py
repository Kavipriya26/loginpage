from rest_framework import Serializers
from.models import register,authentication,deposit,withdraw

class loginSerializer(Serializers.ModelSerializer):
class meta:
	 model=login
         field='_all_'