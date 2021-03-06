from django.db import models


class MockTag(models.Model):

    name = models.CharField(max_length=6)


class MockModel(models.Model):

    name = models.CharField(max_length=6)
    tags = models.ManyToManyField(MockTag)
    ignored = models.CharField(max_length=6, null=True)
    snailtracker_exclude_fields = ('ignored',)


class ChildMockModel(models.Model):

    name = models.CharField(max_length=6)
    mock_model = models.ForeignKey(MockModel)
    snailtracker_child_of = 'mock_model'
