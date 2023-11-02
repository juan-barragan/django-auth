from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 

# Create your views here.
class HelloView(APIView):
    permission_classes = (IsAuthenticated,)  

    def get(self, request):
        content = { 'message': 'Not a ping-pong game!'}
        if 'status' in request.data:
            if request.data['status'] == 'ping':
                content['message'] = 'pong'
            elif request.data['status'] == 'pong':
                content['message'] = 'ping'
        return Response(content)
