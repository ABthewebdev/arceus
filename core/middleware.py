from django.utils.deprecation import MiddlewareMixin


class SubdomainMiddleware(MiddlewareMixin):
    def process_request(self, request):
        host = request.get_host().split(':')[0].lower()
        parts = host.split('.')
        request.subdomain = None
        if len(parts) > 2:
            request.subdomain = parts[0]
