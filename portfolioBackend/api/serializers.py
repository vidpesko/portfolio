from rest_framework import serializers

from .models import Project, Tag, ProjectLink, ProjectStat, Experience


# Project related serializers
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name", "bg_color"]


class ProjectLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectLink
        fields = ["url", "icon"]


class ProjectStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectStat
        fields = ["header", "value", "label"]


class ProjectSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)
    links = ProjectLinkSerializer(read_only=True, many=True)
    stats = ProjectStatSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = ["name", "description", "highlighted", "background_gradient", "tags", "links", "stats", "cover_img"]


# Experience serializer
class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = [
            "company_name",
            "job_role",
            "employment_period",
            "description",
        ]
