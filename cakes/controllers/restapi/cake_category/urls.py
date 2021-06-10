from django.urls import path
from dream_cream_pastries_project.urls import (
    URL_READ_ONLY,
    URL_DETAIL,
    URL_CREATE,
    URL_UPDATE,
    URL_DELETE
)

from .api import(
    ApiPublicCakeCategoryListDetail,
    ApiPrivateCakeCategoryViewSet
)

VERSION = 'v1'

urlpatterns = [
    # public
    path(
        f'{VERSION}/public/list',
        ApiPublicCakeCategoryListDetail.as_view(URL_READ_ONLY),
        name='api_public_cake_category_list_detail'
    ),

    # private
    path(
        f'{VERSION}/private/list',
        ApiPrivateCakeCategoryViewSet.as_view(URL_READ_ONLY),
        name='api_private_cake_category_list_detail'
    ),
    path(
        f'{VERSION}/private/create',
        ApiPrivateCakeCategoryViewSet.as_view(URL_CREATE),
        name='api_private_cake_category_create'
    ),
    path(
        f'{VERSION}/private/<pk>/update',
        ApiPrivateCakeCategoryViewSet.as_view(URL_UPDATE),
        name='api_private_cake_category_update'
    ),
    path(
        f'{VERSION}/private/<pk>/delete',
        ApiPrivateCakeCategoryViewSet.as_view(URL_DELETE),
        name='api_private_cake_category_delete'
    ),
]

"""
Add to urls.py urlpatterns:
    path('cake_category/api/', include('cakes.controllers.restapi.cake_category.urls'))
