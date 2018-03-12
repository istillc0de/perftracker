from perftracker.models.project import ProjectModel
from perftracker.models.job import JobModel
from perftracker.models.test_group import TestGroupModel
from perftracker.models.env_node import EnvNodeModel, EnvNodeTypeModel, HwChassisModel
from django.contrib import admin

admin.site.register(ProjectModel)
admin.site.register(JobModel)
admin.site.register(TestGroupModel)
admin.site.register(EnvNodeModel)
admin.site.register(EnvNodeTypeModel)
admin.site.register(HwChassisModel)