from django.urls import path
from dream_cream_pastries_project.urls import (
    URL_READ_ONLY,
    URL_DETAIL,
    URL_CREATE,
    URL_UPDATE,
    URL_DELETE
)

from .api import(
    ApiPublicBranchMenuListDetail,
    ApiPrivateBranchMenuViewSet
)

VERSION = 'v1'

urlpatterns = [
    # public
    path(
        f'{VERSION}/public/list',
        ApiPublicBranchMenuListDetail.as_view(URL_READ_ONLY),
        name='api_public_branch_menu_list_detail'
    ),

    # private
    path(
        f'{VERSION}/private/list',
        ApiPrivateBranchMenuViewSet.as_view(URL_READ_ONLY),
        name='api_private_branch_menu_list_detail'
    ),
    path(
        f'{VERSION}/private/create',
        ApiPrivateBranchMenuViewSet.as_view(URL_CREATE),
        name='api_private_branch_menu_create'
    ),
    path(
        f'{VERSION}/private/<pk>/update',
        ApiPrivateBranchMenuViewSet.as_view(URL_UPDATE),
        name='api_private_branch_menu_update'
    ),
    path(
        f'{VERSION}/private/<pk>/delete',
        ApiPrivateBranchMenuViewSet.as_view(URL_DELETE),
        name='api_private_branch_menu_delete'
    ),
]

"""
Add to urls.py urlpatterns:
    path('branch_menu/api/', include('branches.controllers.restapi.branch_menu.urls'))
