"""
Dream Cream Pastries
Description for Dream Cream Pastries

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

from employees.models.employee.models import Employee as Master
from admin_dashboard.controllers.views.admin_dashboard.employees.forms import EmployeeForm as MasterForm

"""
URLS
# Employee

from admin_dashboard.controllers.views.admin_dashboard.employees import main as employees_views

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
"""


class AdminDashboardEmployeeListView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    List view for Employees. 
    
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
            "page_title": f"Employees",
            "menu_section": "admin_dashboard",
            "menu_subsection": "employee",
            "menu_action": "list",
            "paginator": paginator,
            "objects": objs
        }

        return render(request, "employees/list.html", context)


class AdminDashboardEmployeeCreateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Employees. 
    
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
            "page_title": "Create new Employee",
            "menu_section": "admin_dashboard",
            "menu_subsection": "employee",
            "menu_action": "create",
            "form": form
        }

        return render(request, "employees/form.html", context)
    
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
                    'admin_dashboard_employees_detail',
                    kwargs={
                        'employee': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Create new Employee",
                "menu_section": "admin_dashboard",
                "menu_subsection": "employee",
                "menu_action": "create",
                "form": form
            }

            messages.error(
                request,
                form.errors,
                extra_tags='danger'
            )
            return render(request, "employees/form.html", context)


class AdminDashboardEmployeeDetailView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Employees. 
    
    Allowed HTTP verbs: 
        - GET
    
    Restrictions:
        - LoginRequired
        - Admin user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('employee', None))
        context = {
            "page_title": f"Employee: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "employee",
            "menu_action": "detail",
            "obj": obj
        }

        return render(request, "employees/detail.html", context)


class AdminDashboardEmployeeUpdateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Employees. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('employee', None))
        form = MasterForm(instance=obj)

        context = {
            "page_title": f"Update Employee: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "employee",
            "menu_action": "update",
            "obj": obj,
            "form": form
        }

        return render(request, "employees/form.html", context)
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('employee', None))
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
                    'admin_dashboard_employees_detail',
                    kwargs={
                        'employee': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Update Employee: {obj}",
                "menu_section": "admin_dashboard",
                "menu_subsection": "employee",
                "menu_action": "update",
                "obj": obj,
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "employees/form.html", context)


class AdminDashboardEmployeeDeleteView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Employees. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('employee', None))
        context = {
            "page_title": "Delete Employee: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "employee",
            "menu_action": "delete",
            "obj": obj
        }

        return render(request, "employees/delete.html", context)
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('employee', None))

        messages.success(
            request,
            f'{obj} deleted!',
            extra_tags='success'
        )

        obj.delete()

        return HttpResponseRedirect(
            reverse(
                'admin_dashboard_employees_list'
            )
        )
