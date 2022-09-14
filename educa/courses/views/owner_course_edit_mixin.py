from .owner_course_mixin import OwnerCourseMixin
from .owner_edit_mixin import OwnerEditMixin


class OwnerCourseEditMixin(OwnerCourseMixin, OwnerEditMixin):
    template_name = 'courses/manage/course/form.html'
