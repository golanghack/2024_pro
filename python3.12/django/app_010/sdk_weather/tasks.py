import datetime
import logging

from celery import shared_task

from sdk_weather.models import Weather
from sdk_weather.services import get_weather

logger = logging.getLogger(__name__)


@shared_task
def create_or_update_weather():
    """Create weather and update weather data on background task"""

    # format time 
    current_time = datetime.datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
    print(f'Time of server: {current_time}')

    logger.info(f"Update weather")

    all_cities = Weather.objects.all()

    for weather in all_cities:
        get_weather(weather.name)
        logger.info(f"Weather ->  {weather.name} update")

    logger.info(f"Data was updated")
