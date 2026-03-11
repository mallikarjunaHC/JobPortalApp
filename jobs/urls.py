from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    JobViewSet,
    add_job,
    job_list,
    job_detail,
    update_job,
    delete_job
)

# Router for ViewSet
router = DefaultRouter()
router.register(r'jobs', JobViewSet, basename='jobs')

urlpatterns = [

    
    # Router APIs
  
    path('', include(router.urls)),

   
    # Custom Job APIs
    
    path('jobs/add/', add_job, name='add-job'),
    path('jobs/list/', job_list, name='job-list'),
    path('jobs/<int:id>/', job_detail, name='job-detail'),
    path('jobs/update/<int:id>/', update_job, name='update-job'),
    path('jobs/delete/<int:id>/', delete_job, name='delete-job'),

]

