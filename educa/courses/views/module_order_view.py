from django.views.generic.base import View
from braces.views import CsrfExemptMixin, JsonRequestResponseMixin
from courses.models.module import Module


class ModuleOrderView(CsrfExemptMixin, JsonRequestResponseMixin, View):
    def post(self, request):
        for _id, order in self.request_json.items():
            Module.objects.filter(id=_id, course__owner=request.user).update(order=order)
        return self.render_json_response({'saved': 'OK'})
