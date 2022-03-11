from rest_framework import viewsets, status
from rest_framework.response import Response
import requests
import json
from .serializers import *
# Create your views here.


class SkipTraceView(viewsets.ViewSet):

    def create(self, request, *args, **kwargs):
        serializer = SipTraceBodySerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            # print(response.text)
        except Exception as e:
            error = {"statusCode": 400, "error": True, "data": "", "message": "Bad Request, Please check request",
                     "errors": e.args[0]}
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
        url = "https://api.skipengine.com/v2/service"

        payload = json.dumps({
            "Key": serializer.data.get("Key"),
            # "FName": "Optional",
            # "LName": "Optional",
            "Address1": serializer.data.get("Address1"),
            "City": serializer.data.get("City"),
            "State": serializer.data.get("State"),
            # "Zip": "77001"
        })
        headers = {
            'Content-Type': 'application/json',
            'x-api-key': 'test-2a3d286e-10fc-44e6-8c5b-a0b92af4e4df'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        if SkipTraceData.objects.filter(skip_trace_detail__Input__Address1=serializer.data.get("Address1"),
                                        skip_trace_detail__Input__City=serializer.data.get("City"),
                                        skip_trace_detail__Input__State=serializer.data.get("State")).exists():
            data_list = SkipTraceData.objects.filter(skip_trace_detail__Input__Address1=serializer.data.get("Address1"),
                                        skip_trace_detail__Input__City=serializer.data.get("City"),
                                        skip_trace_detail__Input__State=serializer.data.get("State"))
            serializer = SipTraceSerializer(data_list, many=True)
            response = {"statusCode": 200, "error": False, "message": "Skip Trace Detail!",
                        "data": serializer.data}
            return Response(response, status=status.HTTP_200_OK)
        else:
            serializer = SipTraceSerializer(data=request.data)
            try:
                serializer.is_valid(raise_exception=True)
            except Exception as e:
                error = {"statusCode": 400, "error": True, "data": "", "message": "Bad Request, Please check request",
                         "errors": e.args[0]}
                return Response(error, status=status.HTTP_400_BAD_REQUEST)
            get_data = json.loads(response.text)
            serializer.save(skip_trace_detail=get_data)
            response = {"statusCode": 200, "error": False, "message": "Skip Trace Detail!",
                        "data": serializer.data}
            return Response(response, status=status.HTTP_200_OK)
