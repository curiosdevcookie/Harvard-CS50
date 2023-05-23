-- Keep a log of any SQL queries you execute as you solve the mystery.
.tables
.schema crime_scene_reports

-- All you know is that the theft took place on July 28, 2021 and that it took place on Humphrey Street.

SELECT * 
  FROM crime_scene_reports 
  WHERE year = '2021' AND month = '7' AND day = '28' AND street = 'Humphrey Street';

-- => 295|2021|7|28|Humphrey Street|Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery.
-- => 297|2021|7|28|Humphrey Street|Littering took place at 16:36. No known witnesses.

.schema interviews

SELECT * 
  FROM interviews 
  WHERE year = '2021' AND month = '7' AND day = '28' 
  AND transcript LIKE '%bakery%';

-- => 161|Ruth|2021|7|28|Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.
-- => 162|Eugene|2021|7|28|I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.
-- => 163|Raymond|2021|7|28|As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of 

 tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket.

.tables

SELECT * 
  FROM bakery_security_logs
  WHERE year = '2021' AND month = '7' AND day = '28' 
  AND hour = '10' AND minute <= '25' 
  AND activity = 'exit';

-- => 260|2021|7|28|10|16|exit|5P2BI95
-- => 261|2021|7|28|10|18|exit|94KL13X
-- => 262|2021|7|28|10|18|exit|6P58WS2
-- => 263|2021|7|28|10|19|exit|4328GD8
-- => 264|2021|7|28|10|20|exit|G412CB7
-- => 265|2021|7|28|10|21|exit|L93JTIZ
-- => 266|2021|7|28|10|23|exit|322W7JE
-- => 267|2021|7|28|10|23|exit|0NTHK55

.tables

SELECT * 
  FROM atm_transactions
  WHERE year = '2021' AND month = '7' AND day = '28' 
  AND atm_location = 'Leggett Street'
  AND transaction_type = 'withdraw';

-- => 246|28500762|2021|7|28|Leggett Street|withdraw|48
-- => 264|28296815|2021|7|28|Leggett Street|withdraw|20
-- => 266|76054385|2021|7|28|Leggett Street|withdraw|60
-- => 267|49610011|2021|7|28|Leggett Street|withdraw|50
-- => 269|16153065|2021|7|28|Leggett Street|withdraw|80
-- => 288|25506511|2021|7|28|Leggett Street|withdraw|20
-- => 313|81061156|2021|7|28|Leggett Street|withdraw|30
-- => 336|26013199|2021|7|28|Leggett Street|withdraw|35

.tables

SELECT * 
  FROM phone_calls
  WHERE year = '2021' AND month = '7' AND day = '28' 
  AND duration < '60';


SELECT caller
  FROM phone_calls
  WHERE year = '2021' AND month = '7' AND day = '28' 
  AND duration < '60';

-- => (130) 555-0289
-- => (499) 555-9472
-- => (367) 555-5533
-- => (499) 555-9472
-- => (286) 555-6063
-- => (770) 555-1861
-- => (031) 555-6622
-- => (826) 555-1652
-- => (338) 555-6650

.tables

SELECT * 
  FROM flights
  WHERE year = '2021' AND month = '7' AND day = '28'; 

--

SELECT airports.id 
  FROM airports
  WHERE airports.city = 'Fiftyville';
-- => 8

SELECT airports.name
  FROM airports
  WHERE airports.id = flights.destination_airport_id

SELECT * 
  FROM flights
  WHERE year = '2021' AND month = '7' AND day = '29' AND origin_airport_id = '8'
  ORDER BY hour ASC
  LIMIT 1;

-- => 6|8|5|2021|7|28|13|49

SELECT id
  FROM flights
  WHERE year = '2021' AND month = '7' AND day = '29' AND origin_airport_id = '8'
  ORDER BY hour ASC
  LIMIT 1;

-- => 36

SELECT destination_airport_id
  FROM flights
  WHERE year = '2021' AND month = '7' AND day = '29' AND origin_airport_id = '8'
  ORDER BY hour ASC
  LIMIT 1;

-- => 4

SELECT city
  FROM airports
  WHERE id IN (SELECT destination_airport_id
  FROM flights
  WHERE year = '2021' AND month = '7' AND day = '29' AND origin_airport_id = '8'
  ORDER BY hour ASC
  LIMIT 1);

-- => New York City 😁

SELECT * 
  FROM passengers
  WHERE flight_id = '36';

-- => 6|3835860232|9A
-- => 6|1618186613|2C
-- => 6|7179245843|3B
-- => 6|1682575122|4B
-- => 6|7597790505|5D
-- => 6|6128131458|6B
-- => 6|6264773605|7D
-- => 6|3642612721|8A

SELECT passport_number 
  FROM passengers
  WHERE flight_id = '36';

-- => 3835860232
-- => 1618186613
-- => 7179245843
-- => 1682575122
-- => 7597790505
-- => 6128131458
-- => 6264773605
-- => 3642612721

SELECT people.license_plate
  FROM people
  WHERE people.passport_number 
    IN (SELECT passengers.passport_number FROM passengers WHERE flight_id = '6'); 

-- => 81MNC9R
-- => JN7K44M
-- => RS7I6A0
-- => 13FNH73
-- => FLFN3W0
-- => 91S1K32
-- => 594IBK6

SELECT bakery_security_logs.license_plate 
  FROM bakery_security_logs
  WHERE year = '2021' AND month = '7' AND day = '28' 
  AND hour = '10' AND minute <= '25' 
  AND activity = 'exit';
  
-- => 5P2BI95
-- => 94KL13X
-- => 6P58WS2
-- => 4328GD8
-- => G412CB7
-- => L93JTIZ
-- => 322W7JE
-- => 0NTHK55

  -- SELECT people.name
  -- FROM people
  -- WHERE people.passport_number 
  --   IN (SELECT passengers.passport_number FROM passengers WHERE flight_id = '6')
  -- AND people.license_plate IN (SELECT bakery_security_logs.license_plate 
  -- FROM bakery_security_logs
  -- WHERE year = '2021' AND month = '7' AND day = '28' 
  -- AND hour = '10' AND minute <= '25' 
  -- AND activity = 'exit'); 


SELECT name
  FROM people
  INNER JOIN (
    SELECT passport_number
    FROM passengers
    WHERE flight_id = '36'
  ) p ON people.passport_number = p.passport_number
  INNER JOIN (
    SELECT caller
    FROM phone_calls
    WHERE year = '2021' AND month = '7' AND day = '28' 
    AND duration < '60'
  ) c ON people.phone_number = c.caller
  INNER JOIN (
    SELECT license_plate
    FROM bakery_security_logs
    WHERE year = '2021' AND month = '7' AND day = '28' 
    AND hour = '10' AND minute <= '25' 
    AND activity = 'exit'
  ) b ON people.license_plate = b.license_plate;

-- Sofia
-- Bruce
-- Kelsey
-- Kelsey


SELECT atm_transactions.id
  FROM atm_transactions
  WHERE year = '2021' AND month = '7' AND day = '28' 
  AND atm_location = 'Leggett Street'
  AND transaction_type = 'withdraw';
-- => 246
-- => 264
-- => 266
-- => 267
-- => 269
-- => 288
-- => 313
-- => 336


SELECT atm_transactions.account_number
  FROM atm_transactions
  WHERE year = '2021' AND month = '7' AND day = '28' 
  AND atm_location = 'Leggett Street'
  AND transaction_type = 'withdraw';



  SELECT bank_accounts.person_id
  FROM bank_accounts
  WHERE bank_accounts.account_number IN (SELECT atm_transactions.account_number
  FROM atm_transactions
  WHERE year = '2021' AND month = '7' AND day = '28' 
  AND atm_location = 'Leggett Street'
  AND transaction_type = 'withdraw');

-- THIEF is:
SELECT name
  FROM people
  INNER JOIN (
    SELECT passport_number
    FROM passengers
    WHERE flight_id = '36'
  ) p ON people.passport_number = p.passport_number
  INNER JOIN (
    SELECT caller
    FROM phone_calls
    WHERE year = '2021' AND month = '7' AND day = '28' 
    AND duration < '60'
  ) c ON people.phone_number = c.caller
  INNER JOIN (
    SELECT license_plate
    FROM bakery_security_logs
    WHERE year = '2021' AND month = '7' AND day = '28' 
    AND hour = '10' AND minute <= '25' 
    AND activity = 'exit'
  ) b ON people.license_plate = b.license_plate
  INNER JOIN (
    SELECT person_id
    FROM bank_accounts
    WHERE bank_accounts.account_number IN (SELECT atm_transactions.account_number
    FROM atm_transactions
    WHERE year = '2021' AND month = '7' AND day = '28' 
    AND atm_location = 'Leggett Street'
    AND transaction_type = 'withdraw')
  ) a ON people.id = a.person_id;

-- => Bruce 😁


SELECT people.phone_number
  FROM people
  WHERE people.name = 'Bruce';

-- => (367) 555-5533

SELECT phone_calls.receiver
  FROM phone_calls
  WHERE phone_calls.caller 
  IN (
    SELECT people.phone_number
    FROM people
    WHERE people.name = 'Bruce'
    )
  AND phone_calls.day = '28'
  AND duration < '60';

-- => (375) 555-8161


-- ACCOMPLICE is:
SELECT name
  FROM people
  INNER JOIN (
    SELECT phone_calls.receiver
      FROM phone_calls
      WHERE phone_calls.caller 
      IN (
        SELECT people.phone_number
        FROM people
        WHERE people.name = 'Bruce'
        )
      AND phone_calls.day = '28'
      AND duration < '60'
  ) c ON people.phone_number = c.receiver;

-- => Robin 😁