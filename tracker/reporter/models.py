from django.db import models
from django.contrib.auth.models import User, Group


class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=30)
    parent_location_id = models.IntegerField(blank=True, null=True,)
    # location_user_group = models.ManyToManyField(Group)
    # location_admin = models.ManyToManyField(User)
    # parent_location = models.ForeignKey('self', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('location_name', 'parent_location_id',)

    def __str__(self):
        return self.location_name


class MediaFile(models.Model):
    media_file = models.FileField(upload_to='media_files/')
    media_type = models.CharField(max_length=200)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.media_file


class Defect(models.Model):
    class DefectStatus(models.TextChoices):
        UNREPAIRED = 0
        REPAIRED = 1

    defect_id = models.AutoField(primary_key=True)
    defect_name = models.CharField(max_length=30)
    defect_description = models.CharField(max_length=30)
    defect_status = models.CharField(max_length=10, choices=DefectStatus.choices, default=DefectStatus.UNREPAIRED)
    defect_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    defect_respondent = models.ManyToManyField(Group)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    media_files = models.ManyToManyField(MediaFile, blank=True)
    reporter = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)

#
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username',)
#
#
# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('id', 'name',)
#
#
# class LocationSerializer(serializers.HyperlinkedModelSerializer):
#     parent_location = serializers.PrimaryKeyRelatedField(read_only=True)
#     location_admin = UserSerializer(many=True, read_only=True)
#     location_user_group = GroupSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Location
#         fields = ['id', 'location_name', 'parent_location', 'location_admin', 'location_user_group']
#
#
# class DefectSerializer(serializers.HyperlinkedModelSerializer):
#     defect_location = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all())
#     defect_respondent = GroupSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Defect
#         fields = ['id', 'defect_respondent', 'defect_status', 'defect_location', 'defect_name', 'defect_description',
#                   'defect_respondent', ]