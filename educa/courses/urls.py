from django.urls import path
from .views.manage_course_list_view import ManageCourseListView
from .views.course_create_view import CourseCreateView
from .views.course_update_view import CourseUpdateView
from .views.course_delete_view import CourseDeleteView
from .views.course_module_update_view import CourseModuleUpdateView
from .views.content_create_update_view import ContentCreateUpdateView
from .views.content_delete_view import ContentDeleteView
from .views.module_content_list_view import ModuleContentListView
from .views.module_order_view import ModuleOrderView
from .views.content_order_view import ContentOrderView
from .views.course_list_view import CourseListView
from .views.course_detail_view import CourseDetailView

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
    path('module/<int:module_id>/', ModuleContentListView.as_view(), name='module_content_list'),
    path('module/order/', ModuleOrderView.as_view(), name='module_order'),
    path('content/order/', ContentOrderView.as_view(), name='content_order'),
    path('subject/<slug:subject>/', CourseListView.as_view(), name='course_list_subject'),
    path('<slug:slug>/', CourseDetailView.as_view(), name='course_detail'),
]
