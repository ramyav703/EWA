# basic URL Configurations
from django.urls import include, path

# import everything from views
from chairsapp.views import AgentView, lounge, recliner, patio, allprods, gaming, office
from chairsapp.order import OrderView
from chairsapp.farud import FraudDetectionController


# specify URL Path for rest_framework
urlpatterns = [
    path('ask/', AgentView.as_view(), name="agent_view"),
    path('api/order/', OrderView.as_view(), name="order_view"),
    path('api/fraud-order/', FraudDetectionController.as_view(), name="fraud_order_view"),
    path('lounge/',lounge, name="lounge_view"),
    path('recliner/',recliner, name="recliner_view"),
    path('patio/',patio, name="patio_view"),
    path('gaming/',gaming, name="gaming_view"),
    path('allprods/',allprods, name="all"),
    path('office/',office, name="office_view"),
	path('api-auth/', include('rest_framework.urls'))
]
