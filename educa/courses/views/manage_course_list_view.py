from .owner_course_mixin import OwnerCourseMixin
from django.views.generic.list import ListView


class ManageCourseListView(OwnerCourseMixin, ListView):
    template_name = 'courses/manage/course/list.html'
    permission_required = 'courses.view_course'
