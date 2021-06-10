from django.urls import path
from admin_dashboard.controllers.views.admin_dashboard.home import main as home_views
from admin_dashboard.controllers.views.admin_dashboard.accounts import main as accounts_views
from admin_dashboard.controllers.views.admin_dashboard.branches import main as branches_views
from admin_dashboard.controllers.views.admin_dashboard.cakes import main as cakes_views
from admin_dashboard.controllers.views.admin_dashboard.cake_categories import main as cake_categories_views
from admin_dashboard.controllers.views.admin_dashboard.cake_images import main as cake_images_views
from admin_dashboard.controllers.views.admin_dashboard.employees import main as employees_views
from admin_dashboard.controllers.views.admin_dashboard.menus import main as menus_views
from admin_dashboard.controllers.views.admin_dashboard.menu_categories import main as menu_categories_views

version = 'api/v1'

READ_ONLY = {
    'get': 'list'
}

urlpatterns = [
    path(
        '',
        home_views.AdminDashboardHomeView.as_view(),
        name='admin_dashboard_home_view'
    ),
]

# Account

urlpatterns += [
    path(
        'account/list',
        accounts_views.AdminDashboardAccountListView.as_view(),
        name='admin_dashboard_accounts_list'
    ),
    path(
        'account/<account>/detail',
        accounts_views.AdminDashboardAccountDetailView.as_view(),
        name='admin_dashboard_accounts_detail'
    ),
    path(
        'account/create',
        accounts_views.AdminDashboardAccountCreateView.as_view(),
        name='admin_dashboard_accounts_create'
    ),
    path(
        'account/<account>/update',
        accounts_views.AdminDashboardAccountUpdateView.as_view(),
        name='admin_dashboard_accounts_update'
    ),
    path(
        'account/<account>/delete',
        accounts_views.AdminDashboardAccountDeleteView.as_view(),
        name='admin_dashboard_accounts_delete'
    )
]

# Branch

urlpatterns += [
    path(
        'branch/list',
        branches_views.AdminDashboardBranchListView.as_view(),
        name='admin_dashboard_branches_list'
    ),
    path(
        'branch/<branch>/detail',
        branches_views.AdminDashboardBranchDetailView.as_view(),
        name='admin_dashboard_branches_detail'
    ),
    path(
        'branch/create',
        branches_views.AdminDashboardBranchCreateView.as_view(),
        name='admin_dashboard_branches_create'
    ),
    path(
        'branch/<branch>/update',
        branches_views.AdminDashboardBranchUpdateView.as_view(),
        name='admin_dashboard_branches_update'
    ),
    path(
        'branch/<branch>/delete',
        branches_views.AdminDashboardBranchDeleteView.as_view(),
        name='admin_dashboard_branches_delete'
    )
]

# Cake

urlpatterns += [
    path(
        'cake/list',
        cakes_views.AdminDashboardCakeListView.as_view(),
        name='admin_dashboard_cakes_list'
    ),
    path(
        'cake/<cake>/detail',
        cakes_views.AdminDashboardCakeDetailView.as_view(),
        name='admin_dashboard_cakes_detail'
    ),
    path(
        'cake/create',
        cakes_views.AdminDashboardCakeCreateView.as_view(),
        name='admin_dashboard_cakes_create'
    ),
    path(
        'cake/<cake>/update',
        cakes_views.AdminDashboardCakeUpdateView.as_view(),
        name='admin_dashboard_cakes_update'
    ),
    path(
        'cake/<cake>/delete',
        cakes_views.AdminDashboardCakeDeleteView.as_view(),
        name='admin_dashboard_cakes_delete'
    )
]

# Cake Category

urlpatterns += [
    path(
        'cake_category/list',
        cake_categories_views.AdminDashboardCakeCategoryListView.as_view(),
        name='admin_dashboard_cake_categories_list'
    ),
    path(
        'cake_category/<cake_category>/detail',
        cake_categories_views.AdminDashboardCakeCategoryDetailView.as_view(),
        name='admin_dashboard_cake_categories_detail'
    ),
    path(
        'cake_category/create',
        cake_categories_views.AdminDashboardCakeCategoryCreateView.as_view(),
        name='admin_dashboard_cake_categories_create'
    ),
    path(
        'cake_category/<cake_category>/update',
        cake_categories_views.AdminDashboardCakeCategoryUpdateView.as_view(),
        name='admin_dashboard_cake_categories_update'
    ),
    path(
        'cake_category/<cake_category>/delete',
        cake_categories_views.AdminDashboardCakeCategoryDeleteView.as_view(),
        name='admin_dashboard_cake_categories_delete'
    )
]

# Cake Image

urlpatterns += [
    path(
        'cake_image/list',
        cake_images_views.AdminDashboardCakeImageListView.as_view(),
        name='admin_dashboard_cake_images_list'
    ),
    path(
        'cake_image/<cake_image>/detail',
        cake_images_views.AdminDashboardCakeImageDetailView.as_view(),
        name='admin_dashboard_cake_images_detail'
    ),
    path(
        'cake_image/<cake>/create',
        cake_images_views.AdminDashboardCakeImageCreateView.as_view(),
        name='admin_dashboard_cake_images_create'
    ),
    path(
        'cake_image/<cake_image>/update',
        cake_images_views.AdminDashboardCakeImageUpdateView.as_view(),
        name='admin_dashboard_cake_images_update'
    ),
    path(
        'cake_image/<cake_image>/delete',
        cake_images_views.AdminDashboardCakeImageDeleteView.as_view(),
        name='admin_dashboard_cake_images_delete'
    )
]

# Employee

urlpatterns += [
    path(
        'employee/list',
        employees_views.AdminDashboardEmployeeListView.as_view(),
        name='admin_dashboard_employees_list'
    ),
    path(
        'employee/<employee>/detail',
        employees_views.AdminDashboardEmployeeDetailView.as_view(),
        name='admin_dashboard_employees_detail'
    ),
    path(
        'employee/create',
        employees_views.AdminDashboardEmployeeCreateView.as_view(),
        name='admin_dashboard_employees_create'
    ),
    path(
        'employee/<employee>/update',
        employees_views.AdminDashboardEmployeeUpdateView.as_view(),
        name='admin_dashboard_employees_update'
    ),
    path(
        'employee/<employee>/delete',
        employees_views.AdminDashboardEmployeeDeleteView.as_view(),
        name='admin_dashboard_employees_delete'
    )
]

# Menu

urlpatterns += [
    path(
        'menu/list',
        menus_views.AdminDashboardMenuListView.as_view(),
        name='admin_dashboard_menus_list'
    ),
    path(
        'menu/<menu>/detail',
        menus_views.AdminDashboardMenuDetailView.as_view(),
        name='admin_dashboard_menus_detail'
    ),
    path(
        'menu/create',
        menus_views.AdminDashboardMenuCreateView.as_view(),
        name='admin_dashboard_menus_create'
    ),
    path(
        'menu/<menu>/update',
        menus_views.AdminDashboardMenuUpdateView.as_view(),
        name='admin_dashboard_menus_update'
    ),
    path(
        'menu/<menu>/delete',
        menus_views.AdminDashboardMenuDeleteView.as_view(),
        name='admin_dashboard_menus_delete'
    )
]

# Menu Category

urlpatterns += [
    path(
        'menu_category/list',
        menu_categories_views.AdminDashboardMenuCategoryListView.as_view(),
        name='admin_dashboard_menu_categories_list'
    ),
    path(
        'menu_category/<menu_category>/detail',
        menu_categories_views.AdminDashboardMenuCategoryDetailView.as_view(),
        name='admin_dashboard_menu_categories_detail'
    ),
    path(
        'menu_category/create',
        menu_categories_views.AdminDashboardMenuCategoryCreateView.as_view(),
        name='admin_dashboard_menu_categories_create'
    ),
    path(
        'menu_category/<menu_category>/update',
        menu_categories_views.AdminDashboardMenuCategoryUpdateView.as_view(),
        name='admin_dashboard_menu_categories_update'
    ),
    path(
        'menu_category/<menu_category>/delete',
        menu_categories_views.AdminDashboardMenuCategoryDeleteView.as_view(),
        name='admin_dashboard_menu_categories_delete'
    )
]
