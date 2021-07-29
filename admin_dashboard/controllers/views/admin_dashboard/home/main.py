"""
Dream Cream Pastries Project
Description for Dream Cream Pastries Project

Author: Mark Jun Gersaniva (markjungersaniva@gmail.com)
Version: 0.0.1
"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from accounts.mixins.user_type_mixins import IsAdminViewMixin
from accounts.models import Account
from accounts.models.account.constants import SUPERADMIN, ADMIN, USER
from branches.models import Branch


class AdminDashboardHomeView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Admin Dashboard Home.
    
    Allowed HTTP verbs: 
        - GET
    
    Restrictions:
        - LoginRequired
        - Admin user

    """

    def get(self, request, *args, **kwargs):
        users = Account.objects.all()
        user_count = users.count()
        user_count = users.count()
        active_users = users.filter(is_active=True).count()
        superadmin_type_count = users.filter(user_type=SUPERADMIN).count()
        admin_type_count = users.filter(user_type=ADMIN).count()
        user_type_count = users.filter(user_type=USER).count()
        branches = Branch.objects.all()

        context = {
            "page_title": f"Admin Dashboards",
            "menu_section": "admin_dashboard",
            "menu_subsection": "admin_dashboard",
            "menu_action": "home",
            "users": user_count,
            "active_users": active_users,
            "superadmin_type_count": superadmin_type_count,
            "admin_type_count": admin_type_count,
            "user_type_count": user_type_count,
            "branches": branches,

        }

        return render(request, "home/home.html", context)
