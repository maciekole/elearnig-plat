from django.shortcuts import redirect, get_object_or_404
from django.views.generic.base import View
from courses.models.content import Content


class ContentDeleteView(View):
    def post(self, request, _id):
        content = get_object_or_404(Content, id=_id, module__course__owner=request.user)
        module = content.module
        content.item.delete()
        content.delete()
        return redirect('module_content_list', module.id)
