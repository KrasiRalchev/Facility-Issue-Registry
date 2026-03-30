from django.http import Http404
from django.shortcuts import redirect


class NotFoundRedirectMixin:
    error_url = ''

    def dispatch(self, request, *args, **kwargs):
        try:
            if hasattr(self, 'get_object'):
                self.object = self.get_object()
        except Http404:
            return redirect(self.error_url)

        return super().dispatch(request, *args, **kwargs)