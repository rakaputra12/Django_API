from rest_framework import serializers
from .models import Netbox


class NetboxSerializer(serializers.ModelSerializer):

    class Meta:
        model = Netbox
        fields = ['id', 'hostname', 'username', 'created_at', 'updated_at', 'pod_count']
        read_only_fields = ['created_at', 'updated_at']
