from django.urls import path
from dream_cream_pastries_project.urls import (
    URL_READ_ONLY,
    URL_DETAIL,
    URL_CREATE,
    URL_UPDATE,
    URL_DELETE
)

from .api import(
    ApiPublicMenuImageListDetail,
    ApiPrivateMenuImageViewSet
)

VERSION = 'v1'

urlpatterns = [
    # public
    path(
        f'{VERSION}/public/list',
        ApiPublicMenuImageListDetail.as_view(URL_READ_ONLY),
        name='api_public_menu_image_list_detail'
    ),

    # private
    path(
        f'{VERSION}/private/list',
        ApiPrivateMenuImageViewSet.as_view(URL_READ_ONLY),
        name='api_private_menu_image_list_detail'
    ),
    path(
        f'{VERSION}/private/create',
        ApiPrivateMenuImageViewSet.as_view(URL_CREATE),
        name='api_private_menu_image_create'
    ),
    path(
        f'{VERSION}/private/<pk>/update',
        ApiPrivateMenuImageViewSet.as_view(URL_UPDATE),
        name='api_private_menu_image_update'
    ),
    path(
        f'{VERSION}/private/<pk>/delete',
        ApiPrivateMenuImageViewSet.as_view(URL_DELETE),
        name='api_private_menu_image_delete'
    ),
]

"""
Add to urls.py urlpatterns:
    path('menu_image/api/', include('menus.controllers.restapi.menu_image.urls'))
