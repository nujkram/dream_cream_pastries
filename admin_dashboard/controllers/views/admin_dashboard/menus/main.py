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

from menus.models.menu.models import Menu as Master
from admin_dashboard.controllers.views.admin_dashboard.menus.forms import MenuForm as MasterForm

"""
URLS
# Menu

from admin_dashboard.controllers.views.admin_dashboard.menus import main as menus_views

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
"""


class AdminDashboardMenuListView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    List view for Menus. 
    
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
            "page_title": f"Menus",
            "menu_section": "admin_dashboard",
            "menu_subsection": "menu",
            "menu_action": "list",
            "paginator": paginator,
            "objects": objs
        }

        return render(request, "menus/list.html", context)


class AdminDashboardMenuCreateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Menus. 
    
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
            "page_title": "Create new Menu",
            "menu_section": "admin_dashboard",
            "menu_subsection": "menu",
            "menu_action": "create",
            "form": form
        }

        return render(request, "menus/form.html", context)
    
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
                    'admin_dashboard_menus_detail',
                    kwargs={
                        'menu': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Create new Menu",
                "menu_section": "admin_dashboard",
                "menu_subsection": "menu",
                "menu_action": "create",
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "menus/form.html", context)


class AdminDashboardMenuDetailView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Menus. 
    
    Allowed HTTP verbs: 
        - GET
    
    Restrictions:
        - LoginRequired
        - Admin user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('menu', None))
        context = {
            "page_title": f"Menu: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "menu",
            "menu_action": "detail",
            "obj": obj
        }

        return render(request, "menus/detail.html", context)


class AdminDashboardMenuUpdateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Menus. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('menu', None))
        form = MasterForm(instance=obj)

        context = {
            "page_title": f"Update Menu: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "menu",
            "menu_action": "update",
            "obj": obj,
            "form": form
        }

        return render(request, "menus/form.html", context)
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('menu', None))
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
                    'admin_dashboard_menus_detail',
                    kwargs={
                        'menu': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Update Menu: {obj}",
                "menu_section": "admin_dashboard",
                "menu_subsection": "menu",
                "menu_action": "update",
                "obj": obj,
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "menus/form.html", context)


class AdminDashboardMenuDeleteView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Menus. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('menu', None))
        context = {
            "page_title": "Delete Menu: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "menu",
            "menu_action": "delete",
            "obj": obj
        }

        return render(request, "menus/delete.html", context)
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('menu', None))

        messages.success(
            request,
            f'{obj} deleted!',
            extra_tags='success'
        )

        obj.delete()

        return HttpResponseRedirect(
            reverse(
                'admin_dashboard_menus_list'
            )
        )
