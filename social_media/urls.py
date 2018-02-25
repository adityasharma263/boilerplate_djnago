from django.contrib import admin
from django.conf import settings
from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
# from social_media.app.urls import api_urlpatterns as app_apis
from social_media.app.urls import urlpatterns as app_apis
# main_urlpatterns = patterns(
#     '',
#     (r'^app', include(app_apis)),
# )
#
# urlpatterns = [
#
#     url(r'^api/v1/', include(main_urlpatterns)),
#     url(r'^admin/', admin.site.urls)),
#
# ]

urlpatterns = [

    url(r'^app/', include(app_apis)),
    url(r'^admin/', admin.site.urls),

]