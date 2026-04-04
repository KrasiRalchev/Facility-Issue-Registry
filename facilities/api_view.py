from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from facilities.models import Facility
from facilities.serializers import FacilityListCreateSerializer, FacilitySerializer


class FacilityListCreateAPIView(ListCreateAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilityListCreateSerializer

class FacilityDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer

