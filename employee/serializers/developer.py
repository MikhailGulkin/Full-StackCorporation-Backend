from rest_framework import serializers

from employee.models.employees import Developer
from employee.models.technologies import Technologies
from employee.serializers.baseSerializers import BaseManagerDeveloperSerializer
from employee.serializers.technologies import TechnologiesSerializer
from employee.serializers.mixins import (
    ProfileUpdateSerializerMixin,
    StaffCreateSerializerMixin
)
from user.models.consts import StaffRole
from user.serializers.mixins import CreateCustomUserSerializerMixin


class DeveloperSerializer(
    BaseManagerDeveloperSerializer,
    ProfileUpdateSerializerMixin,
    CreateCustomUserSerializerMixin,
    StaffCreateSerializerMixin
):
    stack = TechnologiesSerializer(
        many=True,
        required=False,
        read_only=True
    )
    specialty = serializers.CharField(source='get_specialty_display')

    class Meta(BaseManagerDeveloperSerializer.Meta):
        model = Developer
        fields = (
            *BaseManagerDeveloperSerializer.Meta.fields,
            'specialty',
            'stack',
        )

    def create(self, validated_data):
        specialty = validated_data.pop('get_specialty_display')
        return self._staff_create(
            validated_data,
            StaffRole.DEVELOPER,
            specialty=specialty
        )

    def update(self, instance, validated_data):
        self._profile_update(instance, validated_data)
        return super().update(instance, validated_data)


class DeveloperChangeTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = (
            'pk',
            'team',
        )


class DeveloperStackTechnologiesSerializer(serializers.Serializer):
    technology_names = serializers.ListField(
        child=serializers.CharField()
    )

    class Meta:
        fields = (
            'technology_names',
        )
