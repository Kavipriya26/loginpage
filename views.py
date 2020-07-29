from django.shortcuts import render

# Create your views here.

class loginpageview(viewone):
	def post(self,request):
		res=response.data
		token=request.get("token")
		token=request.get("token")
		token=reuest.get("token")
		return response("login successfully")