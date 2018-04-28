from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from todos.views import index,form,session,get_session
from todos.views import delete_rec,update,update_data,file_upload
from access.views import (
    register_view,
)
from join.views import test,one

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index),
    url(r'^index$',index),
    url(r'^form$',form),
    url(r'^delete/(\d+)$',delete_rec),
    url(r'^update/(\d+)$',update),
    url(r'^update_data/(\d+)$',update_data),
    url(r'^set_session$',session),
    url(r'^get_session$',get_session),
    url(r'^upload$',file_upload),
    url(r'^register$',register_view),
    url(r'^test$',test),
    url(r'^one$',one),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
