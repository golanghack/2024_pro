from django.core.management.base import BaseCommand
from statistics.kafka_consumer import consume_food_messages

class Command(BaseCommand):
    help = 'Consume food messages from Kafka'

    def handle(self, args, *kwargs):
        consume_food_messages()