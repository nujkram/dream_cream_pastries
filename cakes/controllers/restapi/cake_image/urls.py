from django.urls import path
from dream_cream_pastries_project.urls import (
    URL_READ_ONLY,
    URL_DETAIL,
    URL_CREATE,
    URL_UPDATE,
    URL_DELETE
)

from .api import(
    ApiPublicCakeImageListDetail,
    ApiPrivateCakeImageViewSet
)

VERSION = 'v1'

urlpatterns = [
    # public
    path(
        f'{VERSION}/public/list',
        ApiPublicCakeImageListDetail.as_view(URL_READ_ONLY),
        name='api_public_cake_image_list_detail'
    ),

    # private
    path(
        f'{VERSION}/private/list',
        ApiPrivateCakeImageViewSet.as_view(URL_READ_ONLY),
        name='api_private_cake_image_list_detail'
    ),
    path(
        f'{VERSION}/private/create',
        ApiPrivateCakeImageViewSet.as_view(URL_CREATE),
        name='api_private_cake_image_create'
    ),
    path(
        f'{VERSION}/private/<pk>/update',
        ApiPrivateCakeImageViewSet.as_view(URL_UPDATE),
        name='api_private_cake_image_update'
    ),
    path(
        f'{VERSION}/private/<pk>/delete',
        ApiPrivateCakeImageViewSet.as_view(URL_DELETE),
        name='api_private_cake_image_delete'
    ),
]

"""
Add to urls.py urlpatterns:
    path('cake_image/api/', include('cakes.controllers.restapi.cake_image.urls'))
