from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])  
def apiOverview_accounts(request):
	if request.user.is_superuser and request.user.is_authenticated:
		api_urls = {
			'auth':'auth',
			'auth/register':'auth/register',
			'auth/login':'auth/login',
			'auth/user':'auth/user',
			'auth/logout':'auth/logout',
			
			}
		return Response(api_urls)
	else:
		return Response("API Access Denied!")