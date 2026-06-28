from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Project, Skill


class DeveloperHomepageTests(TestCase):
    def test_homepage_returns_200(self):
        response = self.client.get(reverse('developer_home'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_uses_correct_template(self):
        response = self.client.get(reverse('developer_home'))
        self.assertTemplateUsed(response, 'developer_portfolio/home.html')

    def test_homepage_context_has_top_projects(self):
        for i in range(5):
            Project.objects.create(
                name=f'Project {i}',
                image=SimpleUploadedFile('test.jpg', b'', content_type='image/jpeg'),
                description='Test',
                tech_stack='Python',
            )
        response = self.client.get(reverse('developer_home'))
        self.assertEqual(len(response.context['top_projects']), 3)


class DeveloperModelTests(TestCase):
    def test_project_str_returns_name(self):
        project = Project.objects.create(
            name='Test Project',
            image=SimpleUploadedFile('test.jpg', b'', content_type='image/jpeg'),
            description='Test description',
            tech_stack='Python, Django',
        )
        self.assertEqual(str(project), 'Test Project')

    def test_skill_str_returns_name(self):
        skill = Skill.objects.create(
            name='Python',
            category=Skill.Category.BACKEND,
            icon=SimpleUploadedFile('test.jpg', b'', content_type='image/jpeg'),
        )
        self.assertEqual(str(skill), 'Python')

    def test_project_creation_and_query(self):
        Project.objects.create(
            name='Project A',
            image=SimpleUploadedFile('test.jpg', b'', content_type='image/jpeg'),
            description='Desc A',
            tech_stack='Tech A',
        )
        Project.objects.create(
            name='Project B',
            image=SimpleUploadedFile('test.jpg', b'', content_type='image/jpeg'),
            description='Desc B',
            tech_stack='Tech B',
        )
        self.assertEqual(Project.objects.count(), 2)


class LanguageSwitchingTests(TestCase):
    def test_default_language_is_catalan(self):
        response = self.client.get(reverse('developer_home'))
        self.assertContains(response, 'Inici')
        self.assertContains(response, 'Projectes')
        self.assertContains(response, 'Sobre mi')

    def test_switch_to_spanish(self):
        self.client.post(
            reverse('set_language'),
            {'language': 'es'},
            HTTP_REFERER=reverse('developer_home'),
        )
        response = self.client.get(reverse('developer_home'))
        self.assertContains(response, 'Inicio')
        self.assertContains(response, 'Proyectos')

    def test_switch_to_english(self):
        self.client.post(
            reverse('set_language'),
            {'language': 'en'},
            HTTP_REFERER=reverse('developer_home'),
        )
        response = self.client.get(reverse('developer_home'))
        self.assertContains(response, 'Home')
        self.assertContains(response, 'Projects')

    def test_language_persists_across_requests(self):
        self.client.post(
            reverse('set_language'),
            {'language': 'en'},
            HTTP_REFERER=reverse('developer_home'),
        )
        response1 = self.client.get(reverse('developer_home'))
        self.assertContains(response1, 'Home')
        response2 = self.client.get(reverse('developer_home'))
        self.assertContains(response2, 'Home')
