from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"
    
class UserDashboardView(TemplateView):
    template_name = "user_dashboard.html"
    
class AgentDashboardView(TemplateView):
    template_name = "agent_dashboard.html"