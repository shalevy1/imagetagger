from rest_framework import serializers

from imagetagger.annotations.models import Annotation, AnnotationType, ExportFormat, Export, Verification
from imagetagger.images.models import Image, ImageSet
from imagetagger.users.models import Team, User


class AnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annotation
        fields = ('id', 'concealed', 'blurred', 'closed', 'last_edit_time',
                  'vector', 'image', 'annotation_type', 'creator', 'last_editor')

    creator = serializers.PrimaryKeyRelatedField(source='user', read_only=True)


class AnnotationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnotationType
        fields = ('id', 'name', 'active', 'vector_type', 'node_count',
                  'enable_concealed', 'enable_blurred')


class ExportFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExportFormat
        fields = ('id', 'name', 'last_change_time', 'public', 'base_format', 'image_format',
                  'annotation_format', 'vector_format', 'not_in_image_format', 'name_format',
                  'min_verifications', 'image_aggregation', 'include_blurred', 'include_concealed')


class ExportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Export
        fields = ('id', 'time', 'annotation_count', 'url', 'deprecated',
                  'format', 'image_set', 'creator')

    creator = serializers.PrimaryKeyRelatedField(source='user', read_only=True)


class UserInImageSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name')

    name = serializers.CharField(source='username')


class TeamInImageSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name')


class ImageSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageSet
        fields = ('id', 'name', 'location', 'description', 'time', 'public',
                  'public_collaboration', 'image_lock', 'priority', 'zip_state',
                  'images', 'main_annotation_type', 'tags', 'team', 'creator')

    tags = serializers.ListField(source='tag_names')
    creator = UserInImageSetSerializer()
    team = TeamInImageSetSerializer()


class ImageSetInUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageSet
        fields = ('id', 'name', 'priority', 'tags', 'team')

    team = TeamInImageSetSerializer()


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'name', 'width', 'height')


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name', 'members', 'admins', 'website')

    members = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    admins = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


class ShortTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'points', 'pinned_sets', 'teams')

    teams = ShortTeamSerializer(many=True)
    pinned_sets = ImageSetInUserSerializer(many=True)


class VerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verification
        fields = ('id', 'time', 'verification_value', 'creator', 'annotation')

    verification_value = serializers.BooleanField(source='verified')
    creator = serializers.PrimaryKeyRelatedField(source='user', read_only=True)
