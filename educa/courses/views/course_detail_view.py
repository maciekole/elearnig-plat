from django.views.generic.detail import DetailView
from courses.models.course import Course


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/manage/course/detail.html'
