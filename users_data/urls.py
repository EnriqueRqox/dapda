# -*- coding: utf-8 -*-
from django.conf.urls import url

from users_data.views import CreateView


urlpatterns = [
    # photos URLs
    url(r'^promocion$', CreateView.as_view(), name='create_user_data'),
]
