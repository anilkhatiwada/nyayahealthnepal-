from django.conf.urls import url
from practitioner.views import PractitionerView

urlpatterns = [
    url(r'^practitioners/$', PractitionerView.as_view()),
]