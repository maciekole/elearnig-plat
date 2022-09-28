from django.urls import path
from .views.student_registration_view import StudentRegistrationView
from .views.student_enroll_course_view import StudentEnrollCourseView
from .views.student_course_list_view import StudentCourseListView
from .views.student_course_detail_view import StudentCourseDetailView

urlpatterns = [
    path('register/', StudentRegistrationView.as_view(), name='student_registration'),
    path('enroll-course/', StudentEnrollCourseView.as_view(), name='student_enroll_course'),
    path('courses/', StudentCourseListView.as_view(), name='student_course_list'),
    path('course/<pk>/', StudentCourseDetailView.as_view(), name='student_course_detail'),
    path('course/<pk>/<module_id>', StudentCourseDetailView.as_view(),
         name='student_course_detail_module'),
]
