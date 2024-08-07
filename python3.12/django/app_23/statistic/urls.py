
from django.urls import path
from .views import StatisticsViewSet

statistics_list = StatisticsViewSet.as_view({
    'get': 'get_daily_statistics',
})

statistics_weekly = StatisticsViewSet.as_view({
    'get': 'get_weekly_statistics',
})

statistics_monthly = StatisticsViewSet.as_view({
    'get': 'get_monthly_statistics',
})

urlpatterns = [
    path('daily/', statistics_list, name='daily-statistics'),
    path('weekly/', statistics_weekly, name='weekly-statistics'),
    path('monthly/', statistics_monthly, name='monthly-statistics'),
]