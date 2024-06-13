import logging
import time
from django.core.management.base import BaseCommand
from django.db import IntegrityError
from sdk_weather.models import Weather
from sdk_weather.services import get_weather

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    A command for into database a data
    """

    def handle(self, *args, **options):
        """Standart function for database handler"""

        # set a cityes
        cities = ["Барселона",
                  "Bures-sur-Yvette", 
                  "Vancouver",
                    "Paris",
                      "Санкт-Петербург",
                        "London",
                          "Rostov-on-Don", 
                          ]
        # cross cityes
        for city in cities:
            # data generate
            data = get_weather(city)
            try:
                weather, created = Weather.objects.update_or_create(
                    name=data['name'],
                    defaults=data
                )
            except IntegrityError:
                weather = Weather.objects.create(**data)
            print(f'Weaher in city =>  {data.get("name")} wrote in db')
            time.sleep(1)

        logger.info(f"Info for cityes {' '.join(cities)} saved in db")
        print(f"Info for cityes {', '.join(cities)} saved in db")
