from django.views.generic.base import View
from braces.views import JsonRequestResponseMixin, CsrfExemptMixin
from courses.models.content import Content


class ContentOrderView(CsrfExemptMixin, JsonRequestResponseMixin, View):
    def post(self, request):
        for _id, order in self.request_json.items():
            Content.objects.filter(id=_id, module__course__owner=request.user).update(order=order)
        return self.render_json_response({'saved': 'OK'})
