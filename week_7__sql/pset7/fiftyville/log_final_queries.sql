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


-- ESCAPE to:
SELECT city
  FROM airports
  WHERE id IN (SELECT destination_airport_id
  FROM flights
  WHERE year = '2021' AND month = '7' AND day = '29' AND origin_airport_id = '8'
  ORDER BY hour ASC
  LIMIT 1);

-- => New York City 😁


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

