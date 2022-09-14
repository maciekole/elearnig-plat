from django.urls import path
from .views.manage_course_list_view import ManageCourseListView
from .views.course_create_view import CourseCreateView
from .views.course_update_view import CourseUpdateView
from .views.course_delete_view import CourseDeleteView
from .views.course_module_update_view import CourseModuleUpdateView
from .views.content_create_update_view import ContentCreateUpdateView
from .views.content_delete_view import ContentDeleteView

urlpatterns = [
    path('mine/', ManageCourseListView.as_view(), name='manage_course_list'),
    path('create/', CourseCreateView.as_view(), name='course_create'),
    path('<pk>/edit/', CourseUpdateView.as_view(), name='course_edit'),
    path('<pk>/delete/', CourseDeleteView.as_view(), name='course_delete'),
    path('<pk>/module/', CourseModuleUpdateView.as_view(), name='course_module_update'),
    path('module/<int:module_id>/content/<model_name>/create/', ContentCreateUpdateView.as_view(),
         name='module_content_create'),
    path('module/<int:module_id>/content/<model_name>/<id>/', ContentCreateUpdateView.as_view(),
         name='module_content_update'),
    path('content/<int:id>/delete/', ContentDeleteView.as_view(), name='module_content_delete'),
]
