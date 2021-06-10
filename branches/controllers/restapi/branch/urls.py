from django.urls import path
from dream_cream_pastries_project.urls import (
    URL_READ_ONLY,
    URL_DETAIL,
    URL_CREATE,
    URL_UPDATE,
    URL_DELETE
)

from .api import(
    ApiPublicBranchListDetail,
    ApiPrivateBranchViewSet
)

VERSION = 'v1'

urlpatterns = [
    # public
    path(
        f'{VERSION}/public/list',
        ApiPublicBranchListDetail.as_view(URL_READ_ONLY),
        name='api_public_branch_list_detail'
    ),

    # private
    path(
        f'{VERSION}/private/list',
        ApiPrivateBranchViewSet.as_view(URL_READ_ONLY),
        name='api_private_branch_list_detail'
    ),
    path(
        f'{VERSION}/private/create',
        ApiPrivateBranchViewSet.as_view(URL_CREATE),
        name='api_private_branch_create'
    ),
    path(
        f'{VERSION}/private/<pk>/update',
        ApiPrivateBranchViewSet.as_view(URL_UPDATE),
        name='api_private_branch_update'
    ),
    path(
        f'{VERSION}/private/<pk>/delete',
        ApiPrivateBranchViewSet.as_view(URL_DELETE),
        name='api_private_branch_delete'
    ),
]

"""
Add to urls.py urlpatterns:
    path('branch/api/', include('branches.controllers.restapi.branch.urls'))
