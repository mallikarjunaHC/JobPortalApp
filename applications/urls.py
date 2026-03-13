from django.urls import path
from .views import recruiter_view_applicants, update_application_status

urlpatterns = [
    # Recruiter View Applicants for a Job
    path('recruiter/job/<int:job_id>/applicants/', recruiter_view_applicants),
    path('recruiter/application/<int:application_id>/status/', update_application_status),
]