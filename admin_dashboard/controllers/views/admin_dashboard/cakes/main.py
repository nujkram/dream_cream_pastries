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

from cakes.models.cake.models import Cake as Master
from admin_dashboard.controllers.views.admin_dashboard.cakes.forms import CakeForm as MasterForm

"""
URLS
# Cake

from admin_dashboard.controllers.views.admin_dashboard.cakes import main as cakes_views

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
"""


class AdminDashboardCakeListView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    List view for Cakes. 
    
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
            "page_title": f"Cakes",
            "menu_section": "admin_dashboard",
            "menu_subsection": "cake",
            "menu_action": "list",
            "paginator": paginator,
            "objects": objs
        }

        return render(request, "cakes/list.html", context)


class AdminDashboardCakeCreateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Cakes. 
    
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
            "page_title": "Create new Cake",
            "menu_section": "admin_dashboard",
            "menu_subsection": "cake",
            "menu_action": "create",
            "form": form
        }

        return render(request, "cakes/form.html", context)
    
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
                    'admin_dashboard_cake_images_create',
                    kwargs={
                        'cake': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Create new Cake",
                "menu_section": "admin_dashboard",
                "menu_subsection": "cake",
                "menu_action": "create",
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "cakes/form.html", context)


class AdminDashboardCakeDetailView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Cakes. 
    
    Allowed HTTP verbs: 
        - GET
    
    Restrictions:
        - LoginRequired
        - Admin user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('cake', None))
        context = {
            "page_title": f"Cake: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "cake",
            "menu_action": "detail",
            "obj": obj
        }

        return render(request, "cakes/detail.html", context)


class AdminDashboardCakeUpdateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Cakes. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('cake', None))
        form = MasterForm(instance=obj)

        context = {
            "page_title": f"Update Cake: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "cake",
            "menu_action": "update",
            "obj": obj,
            "form": form
        }

        return render(request, "cakes/form.html", context)
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('cake', None))
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
                    'admin_dashboard_cakes_detail',
                    kwargs={
                        'cake': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Update Cake: {obj}",
                "menu_section": "admin_dashboard",
                "menu_subsection": "cake",
                "menu_action": "update",
                "obj": obj,
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "cakes/form.html", context)


class AdminDashboardCakeDeleteView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Cakes. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('cake', None))
        context = {
            "page_title": "Delete Cake: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "cake",
            "menu_action": "delete",
            "obj": obj
        }

        return render(request, "cakes/delete.html", context)
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('cake', None))

        messages.success(
            request,
            f'{obj} deleted!',
            extra_tags='success'
        )

        obj.delete()

        return HttpResponseRedirect(
            reverse(
                'admin_dashboard_cakes_list'
            )
        )
