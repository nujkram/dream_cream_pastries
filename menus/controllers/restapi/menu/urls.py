from django.urls import path
from dream_cream_pastries_project.urls import (
    URL_READ_ONLY,
    URL_DETAIL,
    URL_CREATE,
    URL_UPDATE,
    URL_DELETE
)

from .api import(
    ApiPublicMenuListDetail,
    ApiPrivateMenuViewSet
)

VERSION = 'v1'

urlpatterns = [
    # public
    path(
        f'{VERSION}/public/list',
        ApiPublicMenuListDetail.as_view(URL_READ_ONLY),
        name='api_public_menu_list_detail'
    ),

    # private
    path(
        f'{VERSION}/private/list',
        ApiPrivateMenuViewSet.as_view(URL_READ_ONLY),
        name='api_private_menu_list_detail'
    ),
    path(
        f'{VERSION}/private/create',
        ApiPrivateMenuViewSet.as_view(URL_CREATE),
        name='api_private_menu_create'
    ),
    path(
        f'{VERSION}/private/<pk>/update',
        ApiPrivateMenuViewSet.as_view(URL_UPDATE),
        name='api_private_menu_update'
    ),
    path(
        f'{VERSION}/private/<pk>/delete',
        ApiPrivateMenuViewSet.as_view(URL_DELETE),
        name='api_private_menu_delete'
    ),
]

"""
Add to urls.py urlpatterns:
    path('menu/api/', include('menus.controllers.restapi.menu.urls'))
