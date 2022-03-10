from rest_framework import serializers
from .models import *

class SipTraceBodySerializer(serializers.ModelSerializer):
    Key = serializers.CharField(required=True)
    Address1 = serializers.CharField(required=True)
    City = serializers.CharField(required=True)
    State = serializers.CharField(required=True)

    class Meta:
        model = SkipTraceData
        fields = ['Key', 'Address1', 'City', 'State']

class SipTraceSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    skip_trace_detail = serializers.JSONField(required=False)


    class Meta:
        model = SkipTraceData
        fields = ['id', 'skip_trace_detail']
