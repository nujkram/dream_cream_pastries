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

from cakes.models.cake_category.models import CakeCategory as Master
from admin_dashboard.controllers.views.admin_dashboard.cake_categories.forms import CakeCategoryForm as MasterForm

"""
URLS
# Cake Category

from admin_dashboard.controllers.views.admin_dashboard.cake_categories import main as cake_categories_views

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
"""


class AdminDashboardCakeCategoryListView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    List view for Cake Categories. 
    
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
            "page_title": f"Cake Categories",
            "menu_section": "admin_dashboard",
            "menu_subsection": "cake_category",
            "menu_action": "list",
            "paginator": paginator,
            "objects": objs
        }

        return render(request, "cake_categories/list.html", context)


class AdminDashboardCakeCategoryCreateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Cake Categories. 
    
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
            "page_title": "Create new Cake Category",
            "menu_section": "admin_dashboard",
            "menu_subsection": "cake_category",
            "menu_action": "create",
            "form": form
        }

        return render(request, "cake_categories/form.html", context)
    
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
                    'admin_dashboard_cake_categories_detail',
                    kwargs={
                        'cake_category': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Create new Cake Category",
                "menu_section": "admin_dashboard",
                "menu_subsection": "cake_category",
                "menu_action": "create",
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "cake_categories/form.html", context)


class AdminDashboardCakeCategoryDetailView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Cake Categories. 
    
    Allowed HTTP verbs: 
        - GET
    
    Restrictions:
        - LoginRequired
        - Admin user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('cake_category', None))
        context = {
            "page_title": f"Cake Category: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "cake_category",
            "menu_action": "detail",
            "obj": obj
        }

        return render(request, "cake_categories/detail.html", context)


class AdminDashboardCakeCategoryUpdateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Cake Categories. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('cake_category', None))
        form = MasterForm(instance=obj)

        context = {
            "page_title": f"Update Cake Category: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "cake_category",
            "menu_action": "update",
            "obj": obj,
            "form": form
        }

        return render(request, "cake_categories/form.html", context)
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('cake_category', None))
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
                    'admin_dashboard_cake_categories_detail',
                    kwargs={
                        'cake_category': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Update Cake Category: {obj}",
                "menu_section": "admin_dashboard",
                "menu_subsection": "cake_category",
                "menu_action": "update",
                "obj": obj,
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "cake_categories/form.html", context)


class AdminDashboardCakeCategoryDeleteView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Cake Categories. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('cake_category', None))
        context = {
            "page_title": "Delete Cake Category: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "cake_category",
            "menu_action": "delete",
            "obj": obj
        }

        return render(request, "cake_categories/delete.html", context)
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('cake_category', None))

        messages.success(
            request,
            f'{obj} deleted!',
            extra_tags='success'
        )

        obj.delete()

        return HttpResponseRedirect(
            reverse(
                'admin_dashboard_cake_categories_list'
            )
        )
