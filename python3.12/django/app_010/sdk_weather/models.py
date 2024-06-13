from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.search import SearchRank
from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.search import SearchVector
from django.contrib.postgres.search import SearchQuery
from base.models import BaseModel


class Weather(BaseModel):
    """"Weather model
    
    >>>attrs:
    
    main -> main weather parameters
    description -> main description for condition of weather
    temp -> temperature
    feels_like -> feel like a weather 
    visibility -> visibility data
    speed -> speed for wind
    datetime -> date and time for weather data 
    sunrise -> sinrise time
    sunset -> sunset time 
    timezone -> time zone for weather
    name -> name of city
    search_vector -> a vector for full text search
    objects -> all objects in database
    """
    
    main = models.CharField(_('Weather parameters'), max_length=50,
                            help_text='Group of weather parameters (Rain, Snow etc.)')
    description = models.TextField(_('Description'), help_text='Weather condition within the group')

    temp = models.DecimalField(_('Temperature'), max_digits=10, decimal_places=2,
                               help_text='Temperature. Units – default: kelvin, metric: Celsius, imperial: Fahrenheit')
    feels_like = models.DecimalField(_('Human perception of weather'), max_digits=10, decimal_places=2,
                                     help_text='Temperature. This accounts for the human perception of weather. '
                                               'Units – default: kelvin, metric: Celsius, imperial: Fahrenheit')

    visibility = models.PositiveIntegerField(_('Visibility'),
                                             help_text='Average visibility, metres. '
                                                       'The maximum value of the visibility is 10 km')

    speed = models.DecimalField(_('Wind speed'), max_length=50, max_digits=10, decimal_places=2,
                                help_text='Wind speed. '
                                          'Units – default: metre/sec, metric: metre/sec, imperial: miles/hour')

    datetime = models.DateTimeField(_('DateTime'), help_text='Time of the forecasted data, Unix, UTC')

    sunrise = models.DateTimeField(_('Sunrise time'),
                                   help_text='Sunrise time, Unix, UTC. '
                                             'For polar areas in midnight sun and polar night periods '
                                             'this parameter is not returned in the response')
    sunset = models.DateTimeField(_('Sunset time'),
                                  help_text='Sunset time, Unix, UTC. '
                                            'For polar areas in midnight sun and polar night periods '
                                            'this parameter is not returned in the response')

    timezone = models.IntegerField(_('Timezone'), default=0, help_text='Shift in seconds from UTC')

    name = models.CharField(_('City name'), max_length=50, unique=True,
                            help_text='City name. '
                                      'Please note that built-in geocoder functionality has been deprecated.')
    search_vector = SearchVectorField(null=True, editable=False)
    objects = None

    def __str__(self):
        return f'{self.datetime} - {self.name}: {self.temp}, {self.main}'

    class Meta:
        verbose_name = _('Weather')
        verbose_name_plural = _('Weather')
        ordering = ('datetime', 'name',)
        
    def save(self, *args, **kwargs):
        self.search_vector = SearchVector('main', 'description', 'name')
        super().save(*args, **kwargs)    
        
    @classmethod
    def search(cls, query):
        vector = SearchVector('main', 'description', 'name')
        search_query = SearchQuery(query)
        return cls.objects.annotate(rank=SearchRank(vector, search_query)).filter(rank__gt=0.1).order_by('-rank')    
