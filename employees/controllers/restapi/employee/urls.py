from django.urls import path
from dream_cream_pastries_project.urls import (
    URL_READ_ONLY,
    URL_DETAIL,
    URL_CREATE,
    URL_UPDATE,
    URL_DELETE
)

from .api import(
    ApiPublicEmployeeListDetail,
    ApiPrivateEmployeeViewSet
)

VERSION = 'v1'

urlpatterns = [
    # public
    path(
        f'{VERSION}/public/list',
        ApiPublicEmployeeListDetail.as_view(URL_READ_ONLY),
        name='api_public_employee_list_detail'
    ),

    # private
    path(
        f'{VERSION}/private/list',
        ApiPrivateEmployeeViewSet.as_view(URL_READ_ONLY),
        name='api_private_employee_list_detail'
    ),
    path(
        f'{VERSION}/private/create',
        ApiPrivateEmployeeViewSet.as_view(URL_CREATE),
        name='api_private_employee_create'
    ),
    path(
        f'{VERSION}/private/<pk>/update',
        ApiPrivateEmployeeViewSet.as_view(URL_UPDATE),
        name='api_private_employee_update'
    ),
    path(
        f'{VERSION}/private/<pk>/delete',
        ApiPrivateEmployeeViewSet.as_view(URL_DELETE),
        name='api_private_employee_delete'
    ),
]

"""
Add to urls.py urlpatterns:
    path('employee/api/', include('employees.controllers.restapi.employee.urls'))
