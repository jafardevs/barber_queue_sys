from django.test import TestCase, Client
from django.urls import reverse
from .models import Customer

class QueueSystemTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_register_customer(self):
        response = self.client.post(reverse('register'), {
            'name': 'John Doe',
            'phone': '1234567890'
        })
        self.assertEqual(response.status_code, 302) # Redirects to list
        self.assertEqual(Customer.objects.count(), 1)
        customer = Customer.objects.first()
        self.assertEqual(customer.name, 'John Doe')
        self.assertEqual(customer.is_finished, False)

    def test_list_view(self):
        Customer.objects.create(name='Jane Doe', phone='9876543210')
        response = self.client.get(reverse('queue_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Jane Doe')
        self.assertContains(response, 'In Queue')

    def test_finish_customer(self):
        customer = Customer.objects.create(name='Bob', phone='5555555555')
        response = self.client.post(reverse('finish_customer', args=[customer.id]))
        self.assertEqual(response.status_code, 302)
        customer.refresh_from_db()
        self.assertTrue(customer.is_finished)
