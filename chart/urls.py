from django.urls import path, include
from .views import dashboard , pizzaChart, barMonth, charts

urlpatterns = [
    path('dashboard/', dashboard , name="dashboard"),
    path('pizzaChart/', pizzaChart, name="pizzaChart"),
    path('<int:id_portfolio>/barMonth/', barMonth, name="barMonth"),
    path('charts/', charts, name="charts")
]


