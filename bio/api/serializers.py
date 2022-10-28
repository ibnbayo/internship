from rest_framework import serializers

from bio.models import Bio


class BioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bio
        fields = ['slackUsername', 'backend', 'age', 'bio']
