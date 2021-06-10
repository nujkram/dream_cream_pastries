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

from branches.models.branch.models import Branch as Master
from admin_dashboard.controllers.views.admin_dashboard.branches.forms import BranchForm as MasterForm

"""
URLS
# Branch

from admin_dashboard.controllers.views.admin_dashboard.branches import main as branches_views

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
"""


class AdminDashboardBranchListView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    List view for Branches. 
    
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
            "page_title": f"Branches",
            "menu_section": "admin_dashboard",
            "menu_subsection": "branch",
            "menu_action": "list",
            "paginator": paginator,
            "objects": objs
        }

        return render(request, "branches/list.html", context)


class AdminDashboardBranchCreateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Branches. 
    
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
            "page_title": "Create new Branch",
            "menu_section": "admin_dashboard",
            "menu_subsection": "branch",
            "menu_action": "create",
            "form": form
        }

        return render(request, "branches/form.html", context)
    
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
                    'admin_dashboard_branches_detail',
                    kwargs={
                        'branch': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Create new Branch",
                "menu_section": "admin_dashboard",
                "menu_subsection": "branch",
                "menu_action": "create",
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "branches/form.html", context)


class AdminDashboardBranchDetailView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Branches. 
    
    Allowed HTTP verbs: 
        - GET
    
    Restrictions:
        - LoginRequired
        - Admin user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('branch', None))
        context = {
            "page_title": f"Branch: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "branch",
            "menu_action": "detail",
            "obj": obj
        }

        return render(request, "branches/detail.html", context)


class AdminDashboardBranchUpdateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Branches. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('branch', None))
        form = MasterForm(instance=obj)

        context = {
            "page_title": f"Update Branch: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "branch",
            "menu_action": "update",
            "obj": obj,
            "form": form
        }

        return render(request, "branches/form.html", context)
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('branch', None))
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
                    'admin_dashboard_branches_detail',
                    kwargs={
                        'branch': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Update Branch: {obj}",
                "menu_section": "admin_dashboard",
                "menu_subsection": "branch",
                "menu_action": "update",
                "obj": obj,
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "branches/form.html", context)


class AdminDashboardBranchDeleteView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Branches. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('branch', None))
        context = {
            "page_title": "Delete Branch: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "branch",
            "menu_action": "delete",
            "obj": obj
        }

        return render(request, "branches/delete.html", context)
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('branch', None))

        messages.success(
            request,
            f'{obj} deleted!',
            extra_tags='success'
        )

        obj.delete()

        return HttpResponseRedirect(
            reverse(
                'admin_dashboard_branches_list'
            )
        )
