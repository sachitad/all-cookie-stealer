from rest_framework import viewsets, serializers

from .models import Cookie


class CookieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cookie
        fields = ('firefox_cookie', 'chrome_cookie', 'name',)


class CookieViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Cookie.objects.all()
    serializer_class = CookieSerializer