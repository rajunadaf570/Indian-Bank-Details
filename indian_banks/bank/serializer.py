#django/rest_framework imports.
from rest_framework import serializers

#app level imports.
from .models import(
    Banks,
    Branches,
)


class BranchesSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = Branches
        fields = '__all__'
