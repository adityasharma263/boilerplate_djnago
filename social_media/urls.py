from django.contrib import admin
from django.conf import settings
from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from social_media.app.urls import api_urlpatterns as app_apis


main_urlpatterns = patterns(
    '',
    (r'^app', include(app_apis)),
)

urlpatterns = [

    url(r'^api/v1/', include(main_urlpatterns)),
    url(r'^admin/', include(admin.site.urls)),

]