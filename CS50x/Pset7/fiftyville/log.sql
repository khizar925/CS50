-- Keep a log of any SQL queries you execute as you solve the mystery.
--Checking the description of the crime-report at given time and location
SELECT
    description
FROM
    crime_scene_reports
WHERE
    street = 'Humphrey Street'
    AND YEAR = 2023
    AND DAY = 28
    AND MONTH = 7;

-- 2 crimes happened and one is related to the given details, Check for 3 witnesses interviews
SELECT
    name,
    transcript
FROM
    interviews
WHERE
    MONTH = 7
    AND YEAR = 2023
    AND DAY = 28;

-- Witnesses are- Eugene, Raymond, and Ruth.(2 Eugene appears, so checking if they are same or not)
SELECT
    name
FROM
    people
WHERE
    name = 'Eugene';

--only one name appear
SELECT
    name,
    transcript
FROM
    interviews
WHERE
    YEAR = 2023
    AND MONTH = 7
    AND DAY = 28
    AND transcript LIKE '%bakery%'
ORDER BY
    name;

-- Eugene gave clues about theif withdrawing money from ATM on Legget Street
SELECT
    account_number,
    amount
FROM
    atm_transactions
WHERE
    YEAR = 2023
    AND MONTH = 7
    AND DAY = 28
    AND atm_location = 'Leggett Street'
    AND transaction_type = 'withdraw';

--names & amount for account_numbers
SELECT
    name,
    atm_transactions.amount
FROM
    people
    JOIN bank_accounts ON people.id = bank_accounts.person_id
    JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE
    atm_transactions.year = 2023
    AND atm_transactions.month = 7
    AND atm_transactions.day = 28
    AND atm_transactions.atm_location = 'Leggett Street'
    AND atm_transactions.transaction_type = 'withdraw';

-- Raymond (witness) says about taking earliest flight next day (29th July 2023)
SELECT
    *
FROM
    airports
WHERE
    city = 'Fiftyville';

-- Now, finding earlist flight on that day from Fiftyville airports (id = 8)
SELECT flights.id, full_name, city, flights.hour, flights.minute
  FROM airports
  JOIN flights
    ON airports.id = flights.destination_airport_id
 WHERE flights.origin_airport_id = 8
   AND flights.year = 2023
   AND flights.month = 7
   AND flights.day = 29
 ORDER BY flights.hour, flights.minute;


-- First flight is on 08:20 to New York City. Checking list
SELECT passengers.flight_id, name, passengers.passport_number, passengers.seat
  FROM people
  JOIN passengers
    ON people.passport_number = passengers.passport_number
  JOIN flights
    ON passengers.flight_id = flights.id
 WHERE flights.year = 2023
   AND flights.month = 7
   AND flights.day = 29
   AND flights.hour = 8
   AND flights.minute = 20
 ORDER BY passengers.passport_number;


--Anyone from these 8 can be theif.
--Witness tells that theif is one the phone so checking phone records

SELECT name, phone_calls.duration
  FROM people
  JOIN phone_calls
    ON people.phone_number = phone_calls.caller
 WHERE phone_calls.year = 2023
   AND phone_calls.month = 7
   AND phone_calls.day = 28
   AND phone_calls.duration <= 60
 ORDER BY phone_calls.duration;

-- Checking received call in order to find ACCOMPLICE
SELECT name, phone_calls.duration
  FROM people
  JOIN phone_calls
    ON people.phone_number = phone_calls.receiver
 WHERE phone_calls.year = 2023
   AND phone_calls.month = 7
   AND phone_calls.day = 28
   AND phone_calls.duration <= 60
   ORDER BY phone_calls.duration;

-- Ruth (witness) tells about the theif's runaway car within 10 minutes.
SELECT name, bakery_security_logs.hour, bakery_security_logs.minute
  FROM people
  JOIN bakery_security_logs
    ON people.license_plate = bakery_security_logs.license_plate
 WHERE bakery_security_logs.year = 2023
   AND bakery_security_logs.month = 7
   AND bakery_security_logs.day = 28
   AND bakery_security_logs.activity = 'exit'
   AND bakery_security_logs.hour = 10
   AND bakery_security_logs.minute >= 15
   AND bakery_security_logs.minute <= 25
 ORDER BY bakery_security_logs.minute;


-- Bruce must be the theif as he is present in every suspect list.
-- He must escaped to New York City
-- Robin must be the accomplice who purchased the flight ticket, and helped Bruce escape to the New York City.
