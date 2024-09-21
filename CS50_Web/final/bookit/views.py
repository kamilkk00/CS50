from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import User, Professional_User, Service, Time_Slot, Availability
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.http import JsonResponse


# Function that returns the main page with a list of categories
def index(request):
    categories = Service.CATEGORY_CHOICES
    return render(request, 'bookit/index.html', {'categories': categories})

# Function that returns the page with a list of services in a given category
def category(request, category):
    services = Service.objects.filter(category=category)
    selected_category_value = next((label for value, label in Service.CATEGORY_CHOICES if value == category), None)

    return render(request, 'bookit/category.html', {
        'services': services, 
        'category': category,
        'selected_category_value': selected_category_value,
    })


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index') 
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'bookit/login.html')

def logout_view(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'You have been logged out successfully.')
    return redirect("index")

def register(request): 
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        if_professional = False
        
        if password != password_confirm:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'bookit/register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'bookit/register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return render(request, 'bookit/register.html')

        user = User.objects.create_user(username=username, email=email, password=password, if_professional=if_professional)
        user.save()
        login(request, user)
        return redirect('index') 

    return render(request, 'bookit/register.html')

# Function that returns a page where the user can become a service provider
def upgrade(request):
    if request.method == 'POST':
        company_name = request.POST['company_name']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        city = request.POST['city']
        zip_code = request.POST['zip_code']

        company_logo = request.POST['url']
        
        Professional_User.objects.create(
            user=request.user,
            company_name=company_name,
            phone_number=phone_number,
            address=address,
            city=city,
            zip_code=zip_code,
            company_logo = company_logo
        )
        return redirect('index') 
    return render(request, 'bookit/upgrade.html')

# Function that returns the page with the professional's profile
def professional(request, professional_username):
    professional_user = User.objects.get(username=professional_username)
    professional = Professional_User.objects.get(user=professional_user)
    services = Service.objects.filter(created_by=professional)
    return render(request, 'bookit/professional.html', {'professional': professional, 'services': services})

# Function that returns the page with a service
def service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    
    availabilities = Availability.objects.filter(service=service)
    
    # Get the date from the GET parameter
    selected_date_str = request.GET.get('date')
    if selected_date_str:
        selected_date = datetime.strptime(selected_date_str, '%Y-%m-%d').date()
    else:
        selected_date = datetime.today().date()

    available_slots = []

    # Check if the time slot is available
    for availability in availabilities:
        current_time = datetime.combine(selected_date, availability.start_time)
        end_time = datetime.combine(selected_date, availability.end_time)
        
        while current_time + timedelta(minutes=availability.frequency) <= end_time:
            slot_start = current_time.time().strftime('%H:%M')
            slot_end = (current_time + timedelta(minutes=availability.frequency)).time().strftime('%H:%M')

            if not Time_Slot.objects.filter(service=service, date=selected_date, start_time=slot_start).exists():
                available_slots.append({
                    'start_time': slot_start,
                    'end_time': slot_end
                })

            current_time += timedelta(minutes=availability.frequency)

    return render(request, 'bookit/service.html', {
        'service': service,
        'available_slots': available_slots,
        'selected_date': selected_date,
    })


# Function that returns the page with the service creation form
@login_required
def add_service(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category = request.POST.get('category')
        frequency = request.POST.get('frequency')  

        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')

        professional_user = Professional_User.objects.get(user=request.user)

        service = Service.objects.create(
            name=name,
            description=description,
            price=price,
            category=category,
            duration=frequency,  
            created_by=professional_user
        )

        Availability.objects.create(
            service=service,
            professional_user=professional_user,
            start_time=start_time,
            end_time=end_time,
            frequency=frequency
        )

        return redirect('professional', professional_username=request.user.username)

    categories = Service.CATEGORY_CHOICES
    return render(request, 'bookit/add_service.html', {'categories': categories})


# Function that allows the user to book a time slot for a service
@login_required
def book_slot(request, service_id):
    if request.method == "POST":
        service = Service.objects.get(id=service_id)
        start_time_str = request.POST.get('start_time')
        selected_date_str = request.POST.get('date')

        start_time = datetime.strptime(start_time_str, '%H:%M').time()
        selected_date = datetime.strptime(selected_date_str, '%Y-%m-%d').date()

        # Saving time slots is done using AJAX
        if not Time_Slot.objects.filter(service=service, date=selected_date, start_time=start_time).exists():
            Time_Slot.objects.create(
                service=service,
                date=selected_date,  
                start_time=start_time,
                end_time=(datetime.combine(selected_date, start_time) + timedelta(minutes=service.duration)).time(),
                is_booked=True,
                booked_by=request.user
            )
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False}, status=400)

        
# Function that returns a page with a list of booked time slots, useful for service providers
@login_required
def appointments(request, service_id):
    service = get_object_or_404(Service, id=service_id)

    selected_date_str = request.GET.get('date')
    if selected_date_str:
        selected_date = datetime.strptime(selected_date_str, '%Y-%m-%d').date()
    else:
        selected_date = datetime.today().date()  

    booked_slots = Time_Slot.objects.filter(service=service, date=selected_date, is_booked=True).order_by('start_time')

    return render(request, 'bookit/appointments.html', {
        'service': service,
        'booked_slots': booked_slots,
        'selected_date': selected_date
    })

# Function that returns a page showing the services that the user has booked
@login_required
def booked(request):
    booked_slots = Time_Slot.objects.filter(booked_by=request.user).order_by('date', 'start_time')

    return render(request, 'bookit/booked.html', {
        'booked_slots': booked_slots,
    })