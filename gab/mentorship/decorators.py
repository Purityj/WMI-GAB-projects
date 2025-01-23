from django.http import HttpResponseForbidden
from django.shortcuts import redirect

def mentor_required(view_func):
    """allow access only to mentors"""
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == 'mentor':
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("You do not have permission to access this page. Please request Mentorship committee for access.")
    return _wrapped_view

def mentee_required(view_func):
    """allow access only to mentees"""
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == 'mentee':
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("You do not have permission to access this page. Please request Mentorship committee for access.")
    return _wrapped_view

def wmi_required(view_func):
    """allow access only to users with emails from wellsmountaininitiative.org"""
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_wmi_domain():
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("You do not have permission to access this page. Please urequest Mentorship committee for access.")
    return _wrapped_view
