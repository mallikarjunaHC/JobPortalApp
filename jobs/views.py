from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Job
from .serializers import JobSerializer



# ViewSet for Read Operations

class JobViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Job.objects.filter(is_active=True)
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



# Add Job

@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def add_job(request):

    serializer = JobSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "Job added successfully"},
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Get All Jobs

@api_view(['GET'])
def job_list(request):

    jobs = Job.objects.filter(is_active=True)
    serializer = JobSerializer(jobs, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)



# Job Detail

@api_view(['GET'])
def job_detail(request, id):

    job = get_object_or_404(Job, id=id)

    serializer = JobSerializer(job)
    return Response(serializer.data, status=status.HTTP_200_OK)



# Update Job

@api_view(['PUT'])
@permission_classes([IsAuthenticatedOrReadOnly])
def update_job(request, id):

    job = get_object_or_404(Job, id=id)

    serializer = JobSerializer(job, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "Job updated successfully"},
            status=status.HTTP_200_OK
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Delete Job

@api_view(['DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def delete_job(request, id):

    job = get_object_or_404(Job, id=id)
    job.delete()

    return Response(
        {"message": "Job deleted successfully"},
        status=status.HTTP_204_NO_CONTENT
    )
