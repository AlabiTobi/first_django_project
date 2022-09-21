from django.contrib.admin.apps import AdminConfig
from .admin import FirstDjangoProjectAdminSite


class FirstDjangoProjectAdminConfig(AdminConfig):
    default_site = 'first_django_project.admin.FirstDjangoProjectAdminSite'
