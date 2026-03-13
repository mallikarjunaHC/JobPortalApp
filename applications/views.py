from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import JobApplication
from .serializers import JobApplicationSerializer
from jobs.models import Job


# Recruiter View Applicants for a Job
@api_view(['GET'])
def recruiter_view_applicants(request, job_id):
    try:
        job = Job.objects.get(id=job_id)
    except Job.DoesNotExist:
        return Response(
            {"error": "Job not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    applications = JobApplication.objects.filter(job=job)
    serializer = JobApplicationSerializer(applications, many=True)

    return Response({
        "job_id": job.id,
        "job_title": job.title,
        "total_applicants": applications.count(),
        "applicants": serializer.data
    })


# Recruiter Update Candidate Status
@api_view(['PATCH'])
def update_application_status(request, application_id):
    try:
        application = JobApplication.objects.get(id=application_id)
    except JobApplication.DoesNotExist:
        return Response(
            {"error": "Application not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    status_value = request.data.get("status")

    valid_status = ['shortlisted', 'rejected', 'hired']

    if status_value not in valid_status:
        return Response(
            {"error": "Invalid status"},
            status=status.HTTP_400_BAD_REQUEST
        )

    application.status = status_value
    application.save()

    return Response({
        "message": "Application status updated successfully",
        "application_id": application.id,
        "new_status": application.status
    })