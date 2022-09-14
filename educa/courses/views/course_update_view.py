from .owner_course_edit_mixin import OwnerCourseEditMixin
from django.views.generic.edit import UpdateView


class CourseUpdateView(OwnerCourseEditMixin, UpdateView):
    permission_required = 'courses.change_course'
