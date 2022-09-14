from .owner_course_edit_mixin import OwnerCourseEditMixin
from django.views.generic.edit import CreateView


class CourseCreateView(OwnerCourseEditMixin, CreateView):
    permission_required = 'courses/add_course'
