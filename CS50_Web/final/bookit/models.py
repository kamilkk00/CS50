from django.db import models
from django.contrib.auth.models import AbstractUser

# Creating SQL table for User, with reference to whether they are professional (becomes true after creating a professional profile)
class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=128)
    if_professional = models.BooleanField(default=False)
    
    def __str__(self):
        return f"ID: {self.id}, User: {self.username}, e-mail: {self.email}, password: {self.password}, if professional: {self.if_professional}"

# Creating SQL table for Professional User, with reference to User and additional data
class Professional_User(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Professional_User")
    company_name = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    company_logo = models.CharField(max_length=10000, blank=True, null=True)
    

    def __str__(self):
        return f"ID: {self.id}, Company name: {self.company_name}, phone number: {self.phone_number}, address: {self.address}, city: {self.city}, zip code: {self.zip_code}, Company logo: {self.company_logo}"
    
    def save(self, *args, **kwargs):
        self.user.if_professional = True
        self.user.save()
        super().save(*args, **kwargs)

# Creating SQL table for Service, with reference to Professional User
class Service(models.Model):
    CATEGORY_CHOICES = [
        ('HAIRDRESSING', 'Hairdressing'),
        ('BARBER', 'Barber'),
        ('COSMETOLOGY', 'Cosmetology'),
        ('MANICURE_PEDICURE', 'Manicure and Pedicure'),
        ('MASSAGES', 'Massages'),
        ('HAIR_REMOVAL', 'Hair Removal'),
        ('MAKEUP', 'Makeup'),
        ('AESTHETIC_MEDICINE', 'Aesthetic Medicine'),
        ('PERSONAL_TRAINING', 'Personal Training'),
        ('PHYSIOTHERAPY', 'Physiotherapy'),
        ('TATTOOS_PIERCING', 'Tattoos and Piercing'),
        ('SPRAY_TANNING', 'Spray Tanning'),
        ('EYELASH_STYLING', 'Eyelash Styling'),
        ('EYEBROW_STYLING', 'Eyebrow Styling'),
        ('DIETETICS', 'Dietetics'),
        ('SPA_RELAXATION', 'Spa and Relaxation'),
        ('FACIAL_TREATMENTS', 'Facial Treatments'),
        ('OTHER', 'Other'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_by = models.ForeignKey(Professional_User, on_delete=models.CASCADE, related_name="service_created_by")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='OTHER')
    duration = models.IntegerField(help_text="Duration in minutes")


    def __str__(self):
        return f"{self.name} - {self.price} - {self.category} - {self.created_by.company_name}"
    
# Creating SQL table for Time_Slot, where users can book time slots for services
class Time_Slot(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_booked = models.BooleanField(default=False)
    booked_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.service.name} - {self.date} - {self.start_time} - {self.end_time} - {self.booked_by.username}'
    
# Creating SQL table for Availability, where professional users can add their availabilities based on which customers can book time slots
class Availability(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="availabilities")
    professional_user = models.ForeignKey(Professional_User, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    frequency = models.IntegerField(default=60) 

    def __str__(self):
        return f"service: {self.service}, {self.professional_user.company_name}  from {self.start_time} to {self.end_time}"