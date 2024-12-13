from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
#from .products import products
from .serializer import ProductSerializer
from .models import Products

@api_view(['GET'])
def getroutes(request):
    return Response("hi there")
# Create your views here.

@api_view(['GET'])
def  getproduct(request):
    products=Products.objects.all()
    serializer=ProductSerializer(products,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def  getproducts(request,pk):
    product=Products.objects.get(_id=pk)
    serializer=ProductSerializer(product,many=False)
    return Response(serializer.data)

