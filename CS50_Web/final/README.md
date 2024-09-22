# BookIT – Platform for booking services

## Video Demo:  
[BookIT](https://www.youtube.com/watch?v=57OIJV4FecQ)

## Distincitveness:

BookIT is an interactive platform that allows users to book local services (such as a barber or manicure) without the presence of a third party and does not require direct contact with the service provider. 
The platform is particularly unique because it has an interactive form for creating services and automatically creates a calendar for a given service. Users can register for selected time slots at a time specified by the service provider.

## Complexity:  

The project consists of many functionalities, but the most important is the ability to register for the selected service without the intermediation of third parties and direct telephone contact with the service provider.

Each user can create their own service, all they need to do is upgrade their profile to a professional profile on a specially prepared form, then they can add the service they want to provide, the price of the service as well as the working hours in which the service provider provides the service and the duration of the service. Based on this information, BookIT creates both a website for the service provider and a page for a specific service with time slots where consumers can sign up.

Users have the option to find a specific service based on specific categories. Once they find the right service, they can check the available dates directly on the website and can also sign up for the service themselves. If users decide on a selected time slot on a given day, it disappears from the available ones, and the user can check all the services for which they have signed up with one click, and the service provider can check the dates for which customers have signed up together with the user's nickname.

BookIT allows to automatically create new slots for each day, so that the service provider does not have to reintroduce the service.

Dynamic appointment generation and automatic information about enrolled customers are the basis for the operation of the entire application.

BookIT uses a number of models such as user, Professional_User, service along with the time frame of work, on the basis of which the next model, i.e. avaliability, is created, along with information on the hours at which the service provider accepts for a given service and with information on how long the service lasts. On this basis, an interface for the user is created, and after signing up, the data is transferred to the platform using the Time_slot model.

BookIT also uses JavaScript when subscribing to the service in an interactive way along with feedback to the user, as well as JS is used to display messages that disappear after a certain period of time.

## Project Files

Models.py - There are models that record information about users and services, the hours of their offering, or the dates booked for a specific service.

Test.py - This file contains unit tests

Urls.py - The file contains the extracted URL

Views.py

* The file contains a number of functions that allow the application to work properly, i.e.:

* Displaying categories on the home page,

* Displaying specific services in a given category,

* View for registration, login and logout,

* A function that allows users to improve their profile to the service provider

* Displaying with the help of html, the profile of a given service provider,

* Function responsible for displaying html, information about the service as well as available time slots for specific days that can be set using the calendar,

* Function responsible for creating a new service along with information about working hours and the amount of time necessary to serve a given customer. With this feature, slots can be created automatically

* A function that allows to book slots by specific users and automatically (using JS) delete busy dates.

* A function responsible for displaying the booked dates for a given service, which are available to the service provider,

* A function that allows to pass information to HTML about the currently booked services by a given user

All HTML pages are directly linked to the functions presented,

In the static file there is css along with JS, but the presented functions have already been described above.

## How to run application

Starting the migration with creating a superuser and starting the server

I.e.

Python3 manage.py makemigration

Python3 manage.py migrate

Python3 manage.py createsuperuser

Python3 manage.py runserver
