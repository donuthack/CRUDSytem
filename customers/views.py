from django.shortcuts import render, get_object_or_404
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.decorators import api_view, action
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from django.contrib import messages

from .models import Customer
from .serializers import CustomerSerializer

# '''Info about all customers, Add new customer'''
#
#
# @api_view(['GET', 'POST'])
# def customer_list(request):
#     if request.method == 'GET':
#             customers = Customer.objects.all()
#             customers_serializer = CustomerSerializer(customers, many=True)
#             return JsonResponse({'info': customers_serializer.data}, status=status.HTTP_200_OK)
#
#     elif request.method == 'POST':
#         customer_data = JSONParser().parse(request)
#         customer_serializer = CustomerSerializer(data=customer_data)
#
#         if customer_serializer.is_valid():
#             customer_serializer.save()
#             response = {
#                 'message': "Successfully Upload a Customer with id = %d" % customer_serializer.data.get('id'),
#                 'customers': [customer_serializer.data]
#             }
#             return JsonResponse(response, status=status.HTTP_201_CREATED)
#         else:
#             return JsonResponse({'info': customer_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
#
#
# '''Info about , Update info , Delete info customer by id'''
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def customer_detail(request, pk):
#     try:
#         customer = Customer.objects.get(pk=pk)
#     except Customer.DoesNotExist:
#         return JsonResponse({'message': 'This customer does not exist'}, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         customer_serializer = CustomerSerializer(customer)
#         return JsonResponse(customer_serializer.data)
#
#     elif request.method == 'PUT':
#         customer_data = JSONParser().parse(request)
#         customer_serializer = CustomerSerializer(customer, data=customer_data)
#         if customer_serializer.is_valid():
#             customer_serializer.save()
#             return JsonResponse(customer_serializer.data)
#         return JsonResponse(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         customer.delete()
#         return JsonResponse({'message': 'Customer was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)



class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


@action(methods=['delete'], detail=False)
def deleteById(self, request, id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return messages.success("You`ve made it!!")
    # return super(CustomerViewSet, self).deleteById(request, *args, **kwargs)

@action(methods=['put'], detail=False)
def update(self, request, id):
    customer = Customer.objects.all()
    customer_serializer = CustomerSerializer(data=customer)

    if customer.is_valid():
        customer_serializer.save()
        return Response({'info': "Customer updated successfuly"}, customer_serializer)
