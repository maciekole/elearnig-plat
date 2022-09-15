from django.views.generic.base import TemplateResponseMixin, View
from django.shortcuts import get_object_or_404
from courses.models.module import Module


class ModuleContentListView(TemplateResponseMixin, View):
    template_name = 'courses/manage/module/content_list.html'

    def get(self, request, module_id):
        module = get_object_or_404(Module, id=module_id, course__owner=request.user)
        return self.render_to_response({'module': module})
