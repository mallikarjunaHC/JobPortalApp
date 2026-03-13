from rest_framework import serializers
from .models import JobApplication


class JobApplicationSerializer(serializers.ModelSerializer):

    candidate_name = serializers.CharField(source="candidate.user.username", read_only=True)

    class Meta:
        model = JobApplication
        fields = [
            "id",
            "candidate",
            "candidate_name",
            "status",
            "cover_letter",
            "applied_at"
        ]
        
        
        