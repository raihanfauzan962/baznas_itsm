from django.urls import path

from .views import HomePageView, UserDashboardView, AgentDashboardView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("user-dashboard", UserDashboardView.as_view(), name="user-dashboard"),
    path("agent-dashboard", AgentDashboardView.as_view(), name="agent-dashboard"),
]