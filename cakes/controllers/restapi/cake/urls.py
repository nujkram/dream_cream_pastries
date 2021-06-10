from django.urls import path
from dream_cream_pastries_project.urls import (
    URL_READ_ONLY,
    URL_DETAIL,
    URL_CREATE,
    URL_UPDATE,
    URL_DELETE
)

from .api import(
    ApiPublicCakeListDetail,
    ApiPrivateCakeViewSet
)

VERSION = 'v1'

urlpatterns = [
    # public
    path(
        f'{VERSION}/public/list',
        ApiPublicCakeListDetail.as_view(URL_READ_ONLY),
        name='api_public_cake_list_detail'
    ),

    # private
    path(
        f'{VERSION}/private/list',
        ApiPrivateCakeViewSet.as_view(URL_READ_ONLY),
        name='api_private_cake_list_detail'
    ),
    path(
        f'{VERSION}/private/create',
        ApiPrivateCakeViewSet.as_view(URL_CREATE),
        name='api_private_cake_create'
    ),
    path(
        f'{VERSION}/private/<pk>/update',
        ApiPrivateCakeViewSet.as_view(URL_UPDATE),
        name='api_private_cake_update'
    ),
    path(
        f'{VERSION}/private/<pk>/delete',
        ApiPrivateCakeViewSet.as_view(URL_DELETE),
        name='api_private_cake_delete'
    ),
]

"""
Add to urls.py urlpatterns:
    path('cake/api/', include('cakes.controllers.restapi.cake.urls'))
