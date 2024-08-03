from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("registration.urls", namespace="registration")),
    path("", include("sitepages.urls", namespace="sitepages")),
    path("", include("payments.urls", namespace="payments")),
    path("", include("withdrawal.urls", namespace="withdrawal")),
    path('',include("machine.urls",namespace="machine")),
    path('',include("income.urls",namespace="income")),
]
