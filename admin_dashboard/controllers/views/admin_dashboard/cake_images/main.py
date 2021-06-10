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
from django.forms import modelformset_factory

from accounts.mixins.user_type_mixins import IsAdminViewMixin

from cakes.models.cake_image.models import CakeImage as Master
from admin_dashboard.controllers.views.admin_dashboard.cake_images.forms import CakeImageForm as MasterForm

"""
URLS
# Cake Image

from admin_dashboard.controllers.views.admin_dashboard.cake_images import main as cake_images_views

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
        'cake_image/create',
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
"""

ImageFormSet = modelformset_factory(Master, form=MasterForm, extra=5)


class AdminDashboardCakeImageListView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    List view for Cake Images. 
    
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
            "page_title": f"Cake Images",
            "menu_section": "admin_dashboard",
            "menu_subsection": "cake_image",
            "menu_action": "list",
            "paginator": paginator,
            "objects": objs
        }

        return render(request, "cake_images/list.html", context)


class AdminDashboardCakeImageCreateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Cake Images. 
    
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
        form = ImageFormSet(queryset=Master.objects.none())

        context = {
            "page_title": "Create new Cake Image",
            "menu_section": "admin_dashboard",
            "menu_subsection": "cake_image",
            "menu_action": "create",
            "form": form,
        }

        return render(request, "cake_images/form.html", context)

    def post(self, request, *args, **kwargs):
        form = MasterForm(data=request.POST)
        form_set = ImageFormSet(request.POST, request.FILES, queryset=Master.objects.none())

        if form.is_valid():
            data = form.save(commit=False)
            data.created_by = request.user
            data.save()

            for image_data in form_set.cleaned_data:
                if image_data:
                    image = image_data['image']
                    name = image.name
                    cake_image = Master(name=name, image=image, cake=data.pk)
                    cake_image.save()

            messages.success(
                request,
                f'{data} saved!',
                extra_tags='success'
            )

            return HttpResponseRedirect(
                reverse(
                    'admin_dashboard_cake_images_detail',
                    kwargs={
                        'cake_image': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Create new Cake Image",
                "menu_section": "admin_dashboard",
                "menu_subsection": "cake_image",
                "menu_action": "create",
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "cake_images/form.html", context)


class AdminDashboardCakeImageDetailView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Cake Images. 
    
    Allowed HTTP verbs: 
        - GET
    
    Restrictions:
        - LoginRequired
        - Admin user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('cake_image', None))
        context = {
            "page_title": f"Cake Image: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "cake_image",
            "menu_action": "detail",
            "obj": obj
        }

        return render(request, "cake_images/detail.html", context)


class AdminDashboardCakeImageUpdateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Cake Images. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('cake_image', None))
        form = MasterForm(instance=obj)

        context = {
            "page_title": f"Update Cake Image: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "cake_image",
            "menu_action": "update",
            "obj": obj,
            "form": form
        }

        return render(request, "cake_images/form.html", context)

    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('cake_image', None))
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
                    'admin_dashboard_cake_images_detail',
                    kwargs={
                        'cake_image': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Update Cake Image: {obj}",
                "menu_section": "admin_dashboard",
                "menu_subsection": "cake_image",
                "menu_action": "update",
                "obj": obj,
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "cake_images/form.html", context)


class AdminDashboardCakeImageDeleteView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Cake Images. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('cake_image', None))
        context = {
            "page_title": "Delete Cake Image: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "cake_image",
            "menu_action": "delete",
            "obj": obj
        }

        return render(request, "cake_images/delete.html", context)

    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('cake_image', None))

        messages.success(
            request,
            f'{obj} deleted!',
            extra_tags='success'
        )

        obj.delete()

        return HttpResponseRedirect(
            reverse(
                'admin_dashboard_cake_images_list'
            )
        )
