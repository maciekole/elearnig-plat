from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from students+.forms.course_enroll_form import CourseEnrollForm


class StudentEnrollCourseView(LoginRequiredMixin, FormView):
    course = None
    form_class = CourseEnrollForm

    def form_valid(self, form):
        self.course = form.cleaned_data['course']
        self.course.students.add(self.request.user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('student_course_detail', args=[self.course.id])
