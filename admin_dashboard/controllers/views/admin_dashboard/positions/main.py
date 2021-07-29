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

from employees.models.position.models import Position as Master
from admin_dashboard.controllers.views.admin_dashboard.positions.forms import PositionForm as MasterForm

"""
URLS
# Position

from admin_dashboard.controllers.views.admin_dashboard.positions import main as positions_views

urlpatterns += [
    path(
        'position/list',
        positions_views.AdminDashboardPositionListView.as_view(),
        name='admin_dashboard_positions_list'
    ),
    path(
        'position/<position>/detail',
        positions_views.AdminDashboardPositionDetailView.as_view(),
        name='admin_dashboard_positions_detail'
    ),
    path(
        'position/create',
        positions_views.AdminDashboardPositionCreateView.as_view(),
        name='admin_dashboard_positions_create'
    ),
    path(
        'position/<position>/update',
        positions_views.AdminDashboardPositionUpdateView.as_view(),
        name='admin_dashboard_positions_update'
    ),
    path(
        'position/<position>/delete',
        positions_views.AdminDashboardPositionDeleteView.as_view(),
        name='admin_dashboard_positions_delete'
    )
]
"""


class AdminDashboardPositionListView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    List view for Positions. 
    
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
            "page_title": f"Positions",
            "menu_section": "admin_dashboard",
            "menu_subsection": "position",
            "menu_action": "list",
            "paginator": paginator,
            "objects": objs
        }

        return render(request, "positions/list.html", context)


class AdminDashboardPositionCreateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Positions. 
    
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
            "page_title": "Create new Position",
            "menu_section": "admin_dashboard",
            "menu_subsection": "position",
            "menu_action": "create",
            "form": form
        }

        return render(request, "positions/form.html", context)
    
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
                    'admin_dashboard_positions_detail',
                    kwargs={
                        'position': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Create new Position",
                "menu_section": "admin_dashboard",
                "menu_subsection": "position",
                "menu_action": "create",
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "positions/form.html", context)


class AdminDashboardPositionDetailView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Positions. 
    
    Allowed HTTP verbs: 
        - GET
    
    Restrictions:
        - LoginRequired
        - Admin user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('position', None))
        context = {
            "page_title": f"Position: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "position",
            "menu_action": "detail",
            "obj": obj
        }

        return render(request, "positions/detail.html", context)


class AdminDashboardPositionUpdateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Positions. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('position', None))
        form = MasterForm(instance=obj)

        context = {
            "page_title": f"Update Position: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "position",
            "menu_action": "update",
            "obj": obj,
            "form": form
        }

        return render(request, "positions/form.html", context)
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('position', None))
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
                    'admin_dashboard_positions_detail',
                    kwargs={
                        'position': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Update Position: {obj}",
                "menu_section": "admin_dashboard",
                "menu_subsection": "position",
                "menu_action": "update",
                "obj": obj,
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "positions/form.html", context)


class AdminDashboardPositionDeleteView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Positions. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('position', None))
        context = {
            "page_title": "Delete Position: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "position",
            "menu_action": "delete",
            "obj": obj
        }

        return render(request, "positions/delete.html", context)
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('position', None))

        messages.success(
            request,
            f'{obj} deleted!',
            extra_tags='success'
        )

        obj.delete()

        return HttpResponseRedirect(
            reverse(
                'admin_dashboard_positions_list'
            )
        )
