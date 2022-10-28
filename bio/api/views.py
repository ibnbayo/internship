from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from bio.models import Bio
from . serializers import BioSerializer
from django.contrib.auth.models import User

@api_view(["GET"])
@renderer_classes([JSONRenderer])
def bio_api_view(request):
    try:
        bio = Bio.objects.get()
    except Bio.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = BioSerializer(bio)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
