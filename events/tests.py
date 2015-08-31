from django.test import TestCase
from .models import Event

# Create your tests here.
class EventTestCase(TestCase):
    def setUp(self):
        Event.objects.create(
            title="test event",
            slug="test-event",
            all_day=True
        )

    def test_is_single_day_event(self):
        event = Event.objects.get(title="test event")
        print event.from_datetime, event.to_datetime
        self.assertEqual(event.is_single_day, True)


