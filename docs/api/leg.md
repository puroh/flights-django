# Legs
Flights

# Resgiter a new Leg

**Request**:

`POST` `/legs/`

Parameters:

Name                | Type      | Required | Description
--------------------|-----------|----------|------------
departure_airport   | string    | Yes      | The departure airport.
arrival_airport     | string    | Yes      | The arrival airport.
departure_time      | timestamp | yes      | The departure time.
arrival_time        | timestamp | yes      | The arrival time.
stops               | integer   | No       | Stops.
airline_name        | string    | yes      | The airline name.
airline_id          | string    | yes      | The airline id.
duration_mins       | integer   | No       | Duration in minutes.

*Note:*

- Not Authorization Protected

**Response**: