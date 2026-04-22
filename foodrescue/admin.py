from django.contrib.admin import AdminSite
from django.http import HttpResponseRedirect
from django.urls import path

class DirectLoginAdminSite(AdminSite):
    def login(self, request, extra_context=None):
        if request.user.is_authenticated and request.user.is_staff:
            return HttpResponseRedirect('/admin/')
        return HttpResponseRedirect('/accounts/login/?next=/admin/')
    
    def get_urls(self):
        urls = super().get_urls()
        return [path('login/', self.login, name='login')] + urls

public_admin_site = DirectLoginAdminSite(name='public_admin')