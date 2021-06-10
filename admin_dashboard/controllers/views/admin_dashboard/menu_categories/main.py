"""
Dream Cream Pastries Project
Description for Dream Cream Pastries Project

Author: Mark Jun Gersaniva (markjungersaniva@gmail.com)
Version: 0.0.1
"""
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.core.paginator import Paginator

from accounts.mixins.user_type_mixins import IsAdminViewMixin

from menus.models.menu_category.models import MenuCategory as Master
from admin_dashboard.controllers.views.admin_dashboard.menu_categories.forms import MenuCategoryForm as MasterForm

"""
URLS
# Menu Category

from admin_dashboard.controllers.views.admin_dashboard.menu_categories import main as menu_categories_views

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
"""


class AdminDashboardMenuCategoryListView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    List view for Menu Categories. 
    
    Allowed HTTP verbs: 
        - GET
    
    Restrictions:
        - LoginRequired
        - Admin user

    Filters:
        - Optionally used more multi-user/multi-tenant apps to separate ownership
        - ex: company=kwargs.get('company')
    """

    def get(self, request, *args, **kwargs):
        obj_list = Master.objects.actives()
        paginator = Paginator(obj_list, 50)
        page = request.GET.get('page')
        objs = paginator.get_page(page)

        context = {
            "page_title": f"Menu Categories",
            "menu_section": "admin_dashboard",
            "menu_subsection": "menu_category",
            "menu_action": "list",
            "paginator": paginator,
            "objects": objs
        }

        return render(request, "menu_categories/list.html", context)


class AdminDashboardMenuCategoryCreateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Menu Categories. 
    
    Allowed HTTP verbs: 
        - GET
        - POST
    
    Restrictions:
        - LoginRequired
        - Admin user

    Filters:
        - Optionally used more multi-user/multi-tenant apps to separate ownership
        - ex: company=kwargs.get('company')
    """

    def get(self, request, *args, **kwargs):
        form = MasterForm
        context = {
            "page_title": "Create new Menu Category",
            "menu_section": "admin_dashboard",
            "menu_subsection": "menu_category",
            "menu_action": "create",
            "form": form
        }

        return render(request, "menu_categories/form.html", context)
    
    def post(self, request, *args, **kwargs):
        form = MasterForm(data=request.POST)

        if form.is_valid():
            data = form.save(commit=False)
            data.created_by = request.user
            data.save()
            messages.success(
                request,
                f'{data} saved!',
                extra_tags='success'
            )

            return HttpResponseRedirect(
                reverse(
                    'admin_dashboard_menu_categories_detail',
                    kwargs={
                        'menu_category': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Create new Menu Category",
                "menu_section": "admin_dashboard",
                "menu_subsection": "menu_category",
                "menu_action": "create",
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "menu_categories/form.html", context)


class AdminDashboardMenuCategoryDetailView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Menu Categories. 
    
    Allowed HTTP verbs: 
        - GET
    
    Restrictions:
        - LoginRequired
        - Admin user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('menu_category', None))
        context = {
            "page_title": f"Menu Category: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "menu_category",
            "menu_action": "detail",
            "obj": obj
        }

        return render(request, "menu_categories/detail.html", context)


class AdminDashboardMenuCategoryUpdateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Menu Categories. 
    
    Allowed HTTP verbs: 
        - GET
        - POST
    
    Restrictions:
        - LoginRequired
        - Admin user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('menu_category', None))
        form = MasterForm(instance=obj)

        context = {
            "page_title": f"Update Menu Category: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "menu_category",
            "menu_action": "update",
            "obj": obj,
            "form": form
        }

        return render(request, "menu_categories/form.html", context)
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('menu_category', None))
        form = MasterForm(instance=obj, data=request.POST)

        if form.is_valid():
            data = form.save(commit=False)
            data.updated_by = request.user
            data = form.save()
            messages.success(
                request,
                f'{data} saved!',
                extra_tags='success'
            )

            return HttpResponseRedirect(
                reverse(
                    'admin_dashboard_menu_categories_detail',
                    kwargs={
                        'menu_category': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Update Menu Category: {obj}",
                "menu_section": "admin_dashboard",
                "menu_subsection": "menu_category",
                "menu_action": "update",
                "obj": obj,
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "menu_categories/form.html", context)


class AdminDashboardMenuCategoryDeleteView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Menu Categories. 
    
    Allowed HTTP verbs: 
        - GET
        - POST
    
    Restrictions:
        - LoginRequired
        - Admin user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('menu_category', None))
        context = {
            "page_title": "Delete Menu Category: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "menu_category",
            "menu_action": "delete",
            "obj": obj
        }

        return render(request, "menu_categories/delete.html", context)
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('menu_category', None))

        messages.success(
            request,
            f'{obj} deleted!',
            extra_tags='success'
        )

        obj.delete()

        return HttpResponseRedirect(
            reverse(
                'admin_dashboard_menu_categories_list'
            )
        )
