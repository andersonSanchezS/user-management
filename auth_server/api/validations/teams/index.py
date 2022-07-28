from rest_framework import serializers


class TeamValidation:
    @staticmethod
    def validate_title(value):
        if len(value['description']) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long")
        return value
