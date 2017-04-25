from django.contrib.auth.models import *
from rest_framework import viewsets
from API.serializers import *
from API.models import *

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    '''
    Author: Educated Camels
    Purpose: Queries database for Customer data and sets up view for Customer Class (ordered by last name)
    Methods: none (yet)
    '''    
    queryset = Customer.objects.all().order_by('last_name')
    serializer_class = CustomerSerializer


class ProductTypeViewSet(viewsets.ModelViewSet):
    '''
    Author: Dara Thomas
    Purpose: Queries database for Product Type data and sets up view for Product Type
    Methods: none (yet)
    '''    
    queryset = ProductType.objects.all()   
    serializer_class = ProductTypeSerializer


class Payment_TypeViewSet(viewsets.ModelViewSet):
    '''
    Author: Harry Epstein
    Purpose: Queries database for Payment Type data and sets up view for Payment Type
    Methods: none (yet)
    '''
    queryset = PaymentType.objects.all().order_by('account_number')
    serializer_class = PaymentTypeSerializer