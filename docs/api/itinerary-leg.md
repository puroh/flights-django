# Itinerary Legs

Get al information about legs and itineraries.

## Fetch all relations between legs and itineraries.

**Request**:

`GET` `/itineraries/legs/`

**Response**:

```json
Content-Type application/json
200 OK

{
	"itineraries": [
		{
			"id": "19da2fe7-f133-42b4-ac19-0dfd56c59466",
			"price": "115.00",
			"currency": "£",
			"agent": "British Airways",
			"agent_rating": "9.3",
			"created_at": "2022-08-06T23:40:21+0000",
			"updated_at": "2022-08-06T23:40:21+0000",
			"legs": [
				"212e5f23-c0b6-44c4-b694-2b27b7f4ac33",
				"8a8c5181-eaf2-4b56-97dc-43b6ee29eeb1"
			]
		},
        ...
    ],
    "legs": [
		{
			"id": "8a8c5181-eaf2-4b56-97dc-43b6ee29eeb1",
			"created_at": "2022-08-07T00:21:35+0000",
			"updated_at": "2022-08-07T00:21:35+0000",
			"departure_airport": "BUD",
			"arrival_airport": "LTN",
			"departure_time": "2020-10-31T15:35:00+0000",
			"arrival_time": "2020-10-31T17:00:00+0000",
			"stops": 0,
			"airline_name": "Wizz Air",
			"airline_id": "WZ",
			"duration_mins": 145
		},
        ...
    ]
}

```
