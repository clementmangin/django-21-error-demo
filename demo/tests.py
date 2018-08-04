from django.test import TestCase
from django.test.client import Client
from django.urls import reverse


class AdminTest(TestCase):

    fixtures = ['tests', ]

    def test_admin_success_with_add_permissions(self):
        c = Client()
        c.login(username="success_user", password="django_unchained")
        r = c.get(reverse('admin:demo_parent_change', kwargs={'object_id': 1}))
        self.assertEqual(r.status_code, 200)

    def test_admin_failure_without_add_permissions(self):
        c = Client()
        c.login(username="failure_user", password="django_unchained")
        try:
            r = c.get(reverse('admin:demo_parent_change', kwargs={'object_id': 1}))
            self.assertEqual(r.status_code, 200)
        except KeyError as e:
            self.fail('Unexpected crash when accessing parent edit form: {}'.format(e))
