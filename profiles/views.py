from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])  
def Overview(request):
	if request.user.is_superuser and request.user.is_authenticated:
		api_urls = {
			'':'overview',
			'list':'/serviceprovider/profiles',
			}
		return Response(api_urls)
	else:
		return Response("API Access Denied!")
