from django.urls import reverse_lazy
from courses.models.course import Course
from .owner_mixin import OwnerMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class OwnerCourseMixin(OwnerMixin, LoginRequiredMixin, PermissionRequiredMixin):
    model = Course
    fields = ['subject', 'title', 'slug', 'overview']
    success_url = reverse_lazy('manage_course_list')
