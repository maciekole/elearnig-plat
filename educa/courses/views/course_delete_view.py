from .owner_course_edit_mixin import OwnerCourseEditMixin
from django.views.generic.edit import DeleteView


class CourseDeleteView(OwnerCourseEditMixin, DeleteView):
    template_name = 'courses/manage/course/delete.html'
    permission_required = 'courses.delete_course'
