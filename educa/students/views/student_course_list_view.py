from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from courses.models.course import Course


class StudentCourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'students/course/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in=[self.request.user])
