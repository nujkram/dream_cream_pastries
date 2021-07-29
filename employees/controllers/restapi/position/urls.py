from django.urls import path
from dream_cream_pastries_project.urls import (
    URL_READ_ONLY,
    URL_DETAIL,
    URL_CREATE,
    URL_UPDATE,
    URL_DELETE
)

from .api import(
    ApiPublicPositionListDetail,
    ApiPrivatePositionViewSet
)

VERSION = 'v1'

urlpatterns = [
    # public
    path(
        f'{VERSION}/public/list',
        ApiPublicPositionListDetail.as_view(URL_READ_ONLY),
        name='api_public_position_list_detail'
    ),

    # private
    path(
        f'{VERSION}/private/list',
        ApiPrivatePositionViewSet.as_view(URL_READ_ONLY),
        name='api_private_position_list_detail'
    ),
    path(
        f'{VERSION}/private/create',
        ApiPrivatePositionViewSet.as_view(URL_CREATE),
        name='api_private_position_create'
    ),
    path(
        f'{VERSION}/private/<pk>/update',
        ApiPrivatePositionViewSet.as_view(URL_UPDATE),
        name='api_private_position_update'
    ),
    path(
        f'{VERSION}/private/<pk>/delete',
        ApiPrivatePositionViewSet.as_view(URL_DELETE),
        name='api_private_position_delete'
    ),
]

"""
Add to urls.py urlpatterns:
    path('position/api/', include('employees.controllers.restapi.position.urls'))
