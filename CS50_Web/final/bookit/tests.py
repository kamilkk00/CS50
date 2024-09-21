from django.test import TestCase
from .models import User, Professional_User, Service, Time_Slot, Availability
from datetime import datetime, timedelta

class UserModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword123'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertTrue(self.user.check_password('testpassword123'))
        self.assertFalse(self.user.if_professional)

    def test_user_string_representation(self):
        expected_str = f"ID: {self.user.id}, User: {self.user.username}, e-mail: {self.user.email}, password: {self.user.password}, if professional: {self.user.if_professional}"
        self.assertEqual(str(self.user), expected_str)


class ProfessionalUserModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='professionaluser',
            email='professionaluser@example.com',
            password='testpassword123'
        )
        self.professional_user = Professional_User.objects.create(
            user=self.user,
            company_name='Test Company',
            phone_number='123456789',
            address='123 Test Street',
            city='Test City',
            zip_code='12345',
            company_logo='http://testcompany.com/logo.png'
        )

    def test_professional_user_creation(self):
        self.assertEqual(self.professional_user.user.username, 'professionaluser')
        self.assertEqual(self.professional_user.company_name, 'Test Company')
        self.assertEqual(self.professional_user.phone_number, '123456789')
        self.assertEqual(self.professional_user.address, '123 Test Street')
        self.assertEqual(self.professional_user.city, 'Test City')
        self.assertEqual(self.professional_user.zip_code, '12345')
        self.assertEqual(self.professional_user.company_logo, 'http://testcompany.com/logo.png')

    def test_professional_user_string_representation(self):
        expected_str = f"ID: {self.professional_user.id}, Company name: {self.professional_user.company_name}, phone number: {self.professional_user.phone_number}, address: {self.professional_user.address}, city: {self.professional_user.city}, zip code: {self.professional_user.zip_code}, Company logo: {self.professional_user.company_logo}"
        self.assertEqual(str(self.professional_user), expected_str)

    def test_if_professional_updated_on_creation(self):
        self.assertTrue(self.professional_user.user.if_professional)


class ServiceModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='professionaluser',
            email='professionaluser@example.com',
            password='testpassword123'
        )
        self.professional_user = Professional_User.objects.create(
            user=self.user,
            company_name='Test Company',
            phone_number='123456789',
            address='123 Test Street',
            city='Test City',
            zip_code='12345',
            company_logo='http://testcompany.com/logo.png'
        )
        self.service = Service.objects.create(
            name='Haircut',
            description='A basic haircut service',
            price=20.00,
            created_by=self.professional_user,
            category='HAIRDRESSING',
            duration=60
        )

    def test_service_creation(self):
        self.assertEqual(self.service.name, 'Haircut')
        self.assertEqual(self.service.description, 'A basic haircut service')
        self.assertEqual(self.service.price, 20.00)
        self.assertEqual(self.service.created_by, self.professional_user)
        self.assertEqual(self.service.category, 'HAIRDRESSING')

    def test_service_string_representation(self):
        expected_str = f"Haircut - 20.0"
        self.assertEqual(str(self.service), expected_str)


class TimeSlotModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='professionaluser',
            email='professionaluser@example.com',
            password='testpassword123'
        )
        self.professional_user = Professional_User.objects.create(
            user=self.user,
            company_name='Test Company',
            phone_number='123456789',
            address='123 Test Street',
            city='Test City',
            zip_code='12345',
            company_logo='http://testcompany.com/logo.png'
        )
        self.service = Service.objects.create(
            name='Haircut',
            description='A basic haircut service',
            price=20.00,
            created_by=self.professional_user,
            category='HAIRDRESSING',
            duration=60
        )
        self.time_slot = Time_Slot.objects.create(
            service=self.service,
            date=datetime.today().date(),
            start_time=datetime.now(),
            end_time=datetime.now() + timedelta(hours=1)
        )

    def test_time_slot_creation(self):
        self.assertEqual(self.time_slot.service, self.service)
        self.assertEqual(self.time_slot.is_booked, False)
        self.assertIsNone(self.time_slot.booked_by)

    def test_time_slot_string_representation(self):
        expected_str = f'{self.service.name} - {self.time_slot.start_time} - {self.time_slot.end_time}'
        self.assertEqual(str(self.time_slot), expected_str)


class AvailabilityModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='professionaluser',
            email='professionaluser@example.com',
            password='testpassword123'
        )
        self.professional_user = Professional_User.objects.create(
            user=self.user,
            company_name='Test Company',
            phone_number='123456789',
            address='123 Test Street',
            city='Test City',
            zip_code='12345',
            company_logo='http://testcompany.com/logo.png'
        )
        self.service = Service.objects.create(
            name='Haircut',
            description='A basic haircut service',
            price=20.00,
            created_by=self.professional_user,
            category='HAIRDRESSING',
            duration=60
        )
        self.availability = Availability.objects.create(
            service=self.service,
            professional_user=self.professional_user,
            start_time=datetime.now().time(),
            end_time=(datetime.now() + timedelta(hours=2)).time(),
            frequency=60
        )

    def test_availability_creation(self):
        self.assertEqual(self.availability.service, self.service)
        self.assertEqual(self.availability.professional_user, self.professional_user)
        self.assertEqual(self.availability.frequency, 60)

    def test_availability_string_representation(self):
        expected_str = f"service: {self.service}, {self.professional_user.company_name}  from {self.availability.start_time} to {self.availability.end_time}"
        self.assertEqual(str(self.availability), expected_str)