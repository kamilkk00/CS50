-- Keep a log of any SQL queries you execute as you solve the mystery.
-- sprawdzanie raportu
SELECT * FROM crime_scene_reports WHERE year = 2023 AND month = 7 AND day = 28 AND  street = 'Humphrey Street';
-- sprawdzanie przesłychań świadków
SELECT * FROM interviews  WHERE year = 2023 AND month = 7 AND day >= 28;
-- sprawdzanie kto wypłacał pieniądze tego dnia bo przestępcy to robili
SELECT * FROM atm_transactions JOIN bank_accounts ON atm_transactions.account_number = bank_accounts.account_number JOIN people ON bank_accounts.person_id = people.id WHERE atm_transactions.atm_location = 'Leggett Street' AND atm_transactions.year = 2023 AND month = 7 AND atm_transactions.day = 28 AND atm_transactions.transaction_type = 'withdraw';
-- Pokazuje numery tablic rejestracyjnych podejrzanych
SELECT * FROM bakery_security_logs WHERE bakery_security_logs.year = 2023 AND bakery_security_logs.month = 7 AND bakery_security_logs.day = 28 AND bakery_security_logs.hour = 10 AND bakery_security_logs.minute > 15 AND bakery_security_logs.minute < 25;
-- Pokazuje czyje jest to auto
SELECT * FROM bakery_security_logs JOIN people ON bakery_security_logs.license_plate = people.license_plate WHERE bakery_security_logs.year = 2023 AND bakery_security_logs.month = 7 AND bakery_security_logs.day = 28 AND bakery_security_logs.hour = 10 AND bakery_security_logs.minute > 15 AND bakery_security_logs.minute < 25;
-- Lista podejrzanych na podstawie (Bruce, Diana, Iman, Luca)
SELECT name FROM bakery_security_logs JOIN people ON bakery_security_logs.license_plate = people.license_plate WHERE bakery_security_logs.year = 2023 AND bakery_security_logs.month = 7 AND bakery_security_logs.day = 28 AND bakery_security_logs.hour = 10 AND bakery_security_logs.minute > 15 AND bakery_security_logs.minute < 25 ORDER BY people.name;
SELECT name FROM atm_transactions JOIN bank_accounts ON atm_transactions.account_number = bank_accounts.account_number JOIN people ON bank_accounts.person_id = people.id WHERE atm_transactions.atm_location = 'Leggett Street' AND atm_transactions.year = 2023 AND month = 7 AND atm_transactions.day = 28 AND atm_transactions.transaction_type = 'withdraw' ORDER BY people.name;
-- Sprawdzenie kto rozmawiał wtedy przez tefelon
SELECT * FROM phone_calls WHERE phone_calls.year = 2023 AND phone_calls.month = 7 AND phone_calls.day = 28 AND phone_calls.duration <= 60;
-- Dane tych podejrzanych
SELECT * FROM phone_calls JOIN people ON phone_calls.caller = people.phone_number WHERE phone_calls.year = 2023 AND phone_calls.month = 7 AND phone_calls.day = 28 AND phone_calls.duration <= 60;
-- Podejrzani Diana i Bruce
SELECT name FROM phone_calls JOIN people ON phone_calls.caller = people.phone_number WHERE phone_calls.year = 2023 AND phone_calls.month = 7 AND phone_calls.day = 28 AND phone_calls.duration <= 60 ORDER BY people.name;
-- Sprawdzenie jakie były wyloty następnego dnia
SELECT * FROM airports JOIN flights ON airports.id = flights.origin_airport_id WHERE airports.city = 'Fiftyville' AND day = 29 ORDER BY hour;
-- Lista podejrzanych pasazerów -> Bruce napadł na piekarnie
SELECT * FROM passengers JOIN people ON passengers.passport_number = people.passport_number WHERE passengers.flight_id = 36 ORDER BY people.name;
-- Sprawdzenie dokąd wylecieli -> LaGuardia Airport City New York City
SELECT * FROM airports JOIN flights ON airports.id = flights.origin_airport_id WHERE airports.id = 4;
-- Sprawdzenie z jakim numere rozmawiał Bruce
SELECT * FROM phone_calls JOIN people ON phone_calls.caller = people.phone_number WHERE phone_calls.year = 2023 AND phone_calls.month = 7 AND phone_calls.day = 28 AND phone_calls.duration <= 60 AND people.name = 'B
ruce';
-- Sprawdzenie do kogo nalezy numer telefonu czyli kto się współsprawcą -> Robin
SELECT * FROM phone_calls JOIN people ON phone_calls.caller = people.phone_number  WHERE people.phone_number = '(375) 555-8161';
