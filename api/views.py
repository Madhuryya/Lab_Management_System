from django.shortcuts import render
from rest_framework import status
from .models import Item
from .serializer import ItemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class getItem(APIView):
    # queryset=Item.objects.all()
    # serializer_class=ItemSerializer
    def get(self, request, *args, **kwargs):  
        # result = Item.objects.all()
        # serializer=ItemSerializer(result,many=True)
        return Response({'status': 'success'}, status=200)
# class getItem(APIView):
#     # queryset=Item.objects.all()
#     # serializer_class=ItemSerializer
#     def get(self, request, *args, **kwargs):  
#         result = Item.objects.all()
#         serializer=ItemSerializer(result,many=True)
#         return Response({'status': 'success', "items":serializer.data}, status=200)
# class postItem(APIView): 
#     # permission_classes = (IsAuthenticated,)
#     def post(self, request):  
#         serializer = ItemSerializer(data=request.data)  
#         if serializer.is_valid():   
#             return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
#             # return Response({"location": location})  
#         else:  
#             return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)