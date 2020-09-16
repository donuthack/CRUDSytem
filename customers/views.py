from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Customer
from .serializers import CustomerSerializer

# @api_view(['GET', 'POST'])
# def customer_list(request):
#     if request.method == 'GET':
#         try:
#             customers = Customer.objects.all()
#             customers_serializer = CustomerSerializer(customers, many=True)
#
#             response = {
#                 'message': "Get all Customers infos Successfully",
#                 'customers': customers_serializer.data,
#             }
#             return JsonResponse(response, status=status.HTTP_200_OK)
#         except:
#             error = {
#                 'message': "Fail! You cant get all customers list:c Please check and try again!",
#                 'error': "Error"
#             }
#             return JsonResponse(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#     elif request.method == 'POST':
#         try:
#             customer_data = JSONParser().parse(request)
#             customer_serializer = CustomerSerializer(data=customer_data)
#
#             if customer_serializer.is_valid():
#                 customer_serializer.save()
#                 print(customer_serializer.data)
#                 response = {
#                     'message': "Successfully Upload a Customer with id = %d" % customer_serializer.data.get('id'),
#                     'customers': [customer_serializer.data],
#                 }
#                 return JsonResponse(response, status=status.HTTP_201_CREATED)
#             else:
#                 error = {
#                     'message': "Can Not upload successfully!",
#                     'error': customer_serializer.errors
#                 }
#                 return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST)
#         except:
#             exceptionError = {
#                 'message': "Can Not upload successfully!",
#                 'error': "Having an exception!"
#             }
#             return JsonResponse(exceptionError, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
# @api_view(['PUT', 'DELETE'])
# def customer_detail(request, pk):
#     try:
#         customer = Customer.objects.get(pk=pk)
#     except Customer.DoesNotExist:
#         exceptionError = {
#             'message': "Not found a Customer with id = %s!" % pk,
#             'error': "404 Code - Not Found!"
#         }
#         return JsonResponse(exceptionError, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'PUT':
#         try:
#             customer_data = JSONParser().parse(request)
#             customer_serializer = CustomerSerializer(customer, data=customer_data)
#
#             if customer_serializer.is_valid():
#                 customer_serializer.save()
#                 response = {
#                     'message': "Successfully Update a Customer with id = %s" % pk,
#                     'customers': [customer_serializer.data],
#                 }
#                 return JsonResponse(response)
#
#             response = {
#                 'message': "Fail to Update a Customer with id = %s" % pk,
#                 'customers': [customer_serializer.data],
#                 'error': customer_serializer.errors
#             }
#             return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST)
#         except:
#             exceptionError = {
#                 'message': "Fail to update a Customer with id = %s!" % pk,
#                 'customers': customer_serializer.data,
#                 'error': "Internal Error!"
#             }
#             return JsonResponse(exceptionError, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#     elif request.method == 'DELETE':
#         print("Deleting a Customer with id=%s" % pk)
#         customer.delete()
#         customer_serializer = CustomerSerializer(customer)
#         response = {
#             'message': "Successfully Delete a Customer with id = %s" % pk,
#             'customers': [customer_serializer.data],
#             'error': ""
#         }
#         return JsonResponse(response)


'''Info about all customers, Add new customer'''


@api_view(['GET', 'POST'])
def customer_list(request):
    if request.method == 'GET':
            customers = Customer.objects.all()
            customers_serializer = CustomerSerializer(customers, many=True)
            return JsonResponse({'info': customers_serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        customer_data = JSONParser().parse(request)
        customer_serializer = CustomerSerializer(data=customer_data)

        if customer_serializer.is_valid():
            customer_serializer.save()
            response = {
                'message': "Successfully Upload a Customer with id = %d" % customer_serializer.data.get('id'),
                'customers': [customer_serializer.data]
            }
            return JsonResponse(response, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({'info': customer_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


'''Info about , Update info , Delete info customer by id'''


@api_view(['GET', 'PUT', 'DELETE'])
def customer_detail(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return JsonResponse({'message': 'This customer does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        customer_serializer = CustomerSerializer(customer)
        return JsonResponse(customer_serializer.data)

    elif request.method == 'PUT':
        customer_data = JSONParser().parse(request)
        customer_serializer = CustomerSerializer(customer, data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse(customer_serializer.data)
        return JsonResponse(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        customer.delete()
        return JsonResponse({'message': 'Customer was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
