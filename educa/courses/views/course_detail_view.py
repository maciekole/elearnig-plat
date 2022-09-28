from django.views.generic.detail import DetailView
from courses.models.course import Course
from students.forms.course_enroll_form import CourseEnrollForm


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/manage/course/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['enroll_form'] = CourseEnrollForm(initial={'course': self.object})
        return context
