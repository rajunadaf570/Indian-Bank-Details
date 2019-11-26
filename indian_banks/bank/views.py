#python imports.
import json
import ast
#django/rest_framework imports.
# from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
# from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

#app level imports.
from .models import(
    Banks,
    Branches,
)

from .serializer import(
    BranchesSerializer,
)

from libs.exceptions import(
    ParseException,
    ResourceConflictException,
)

from libs.constants import(
    BAD_ACTION,
    BAD_REQUEST,
)


class BanksViewSet(GenericViewSet):
    """
    """
    ordering_fields = ('id',)
    ordering = ('id',)
    lookup_field = 'id'
    http_method_names = ['get', 'post', 'put','delete']
    queryset = Branches.objects.all()

    def get_queryset(self, filterdata=None):

        if filterdata:
            self.queryset = Branches.objects.filter(**filterdata)
        return self.queryset

    serializers_dict = {
        "getbranchdetails" : BranchesSerializer,
    }

    def get_serializer_class(self):
        try:
            return self.serializers_dict[self.action]
        except KeyError as key:
            raise ParseException(BAD_ACTION, errors=key)



    @action(methods=['get'], detail=False, permission_classes=[IsAuthenticated, ])
    def getbranchdetails(self, request):
        """
        """
        json_data = ast.literal_eval(json.dumps(request.GET))
        if 'offset' in json_data:
            del json_data['offset']
        if 'limit' in json_data:
            del json_data['limit']

        if 'bank' in json_data:
            bank = Banks.objects.get(name=json_data['bank'])
            json_data['bank'] = bank

        try:       
            data = self.get_serializer(self.get_queryset(json_data), many=True).data 
            page = self.paginate_queryset(data)
            if page is not None:
                return self.get_paginated_response(page)

        except Exception as e:
            return Response({'status':'failure','methods':str(e)}, status=status.HTTP_404_NOT_FOUND)
