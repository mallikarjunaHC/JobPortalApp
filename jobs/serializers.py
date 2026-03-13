from rest_framework import serializers
from .models import Job


class JobSerializer(serializers.ModelSerializer):

    company_name = serializers.CharField(
        source="company.name",
        read_only=True
    )

    skills = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Job
        fields = [
            "id",
            "title",
            "company_name",
            "location",
            "employment_type",
            "salary_min",
            "salary_max",
            "status",
            "is_active",
            "created_at",
            "skills",
        ]

        read_only_fields = [
            "id",
            "created_at",
            "company_name",
            "skills"
        ]

    def get_skills(self, obj):
        """
        Return list of skill names for the job
        """
        return [js.skill.name for js in obj.jobskill_set.all()]