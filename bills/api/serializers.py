from rest_framework import serializers

from service.models import Bills


class BillsSerializer(serializers.ModelSerializer):
    client_name = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    date = serializers.DateField(
        input_formats=['%d.%m.%Y', ],
        format='%d.%m.%Y',
    )

    class Meta:
        fields = '__all__'
        model = Bills


    def validate_service(self, service):
        if service == '-':
            raise serializers.ValidationError(
                'Нельзя оставлять пустым и "-"'
            )
        return service