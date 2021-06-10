from django.urls import path
from dream_cream_pastries_project.urls import (
    URL_READ_ONLY,
    URL_DETAIL,
    URL_CREATE,
    URL_UPDATE,
    URL_DELETE
)

from .api import(
    ApiPublicMenuCategoryListDetail,
    ApiPrivateMenuCategoryViewSet
)

VERSION = 'v1'

urlpatterns = [
    # public
    path(
        f'{VERSION}/public/list',
        ApiPublicMenuCategoryListDetail.as_view(URL_READ_ONLY),
        name='api_public_menu_category_list_detail'
    ),

    # private
    path(
        f'{VERSION}/private/list',
        ApiPrivateMenuCategoryViewSet.as_view(URL_READ_ONLY),
        name='api_private_menu_category_list_detail'
    ),
    path(
        f'{VERSION}/private/create',
        ApiPrivateMenuCategoryViewSet.as_view(URL_CREATE),
        name='api_private_menu_category_create'
    ),
    path(
        f'{VERSION}/private/<pk>/update',
        ApiPrivateMenuCategoryViewSet.as_view(URL_UPDATE),
        name='api_private_menu_category_update'
    ),
    path(
        f'{VERSION}/private/<pk>/delete',
        ApiPrivateMenuCategoryViewSet.as_view(URL_DELETE),
        name='api_private_menu_category_delete'
    ),
]

"""
Add to urls.py urlpatterns:
    path('menu_category/api/', include('menus.controllers.restapi.menu_category.urls'))
