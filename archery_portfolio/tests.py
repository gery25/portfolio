from django.test import TestCase
from django.urls import reverse
from datetime import date
from .models import Competitions


class ArcheryHomepageTests(TestCase):
    def test_homepage_returns_200(self):
        response = self.client.get(reverse('archery_home'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_uses_correct_template(self):
        response = self.client.get(reverse('archery_home'))
        self.assertTemplateUsed(response, 'archery_portfolio/home.html')

    def test_homepage_context_has_last_competitions(self):
        for i in range(5):
            Competitions.objects.create(
                name=f'Comp {i}',
                description='Test',
                type=Competitions.Type.Outdoor,
                date=date.today(),
            )
        response = self.client.get(reverse('archery_home'))
        self.assertEqual(len(response.context['last_competitions']), 3)


class ArcheryModelTests(TestCase):
    def test_competitions_str_returns_name(self):
        comp = Competitions.objects.create(
            name='Test Competition',
            description='Test description',
            type=Competitions.Type.Indoor,
            date=date.today(),
        )
        self.assertEqual(str(comp), 'Test Competition')

    def test_competitions_creation_and_query(self):
        Competitions.objects.create(
            name='Comp A',
            description='Desc A',
            type=Competitions.Type.Outdoor,
            date=date.today(),
        )
        Competitions.objects.create(
            name='Comp B',
            description='Desc B',
            type=Competitions.Type.Indoor,
            date=date.today(),
        )
        self.assertEqual(Competitions.objects.count(), 2)

    def test_competitions_filter_by_type(self):
        Competitions.objects.create(
            name='Outdoor Comp',
            description='Desc',
            type=Competitions.Type.Outdoor,
            date=date.today(),
        )
        Competitions.objects.create(
            name='Indoor Comp',
            description='Desc',
            type=Competitions.Type.Indoor,
            date=date.today(),
        )
        outdoor_comps = Competitions.objects.filter(type=Competitions.Type.Outdoor)
        self.assertEqual(outdoor_comps.count(), 1)
        self.assertEqual(outdoor_comps.first().name, 'Outdoor Comp')
