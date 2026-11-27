import requests, json
payload = {
    "firstname": "Mohit",
    "lastname": "Patnaik",
    "totalprice": 1500,
    "depositpaid": "true",
    "bookingdates": {
        "checkin": "2026-12-01",
        "checkout": "2026-12-05"
    },
    "additionalneeds": "Breakfast,Lunch and Dinner"
}

base_url = "https://restful-booker.herokuapp.com/booking"

def test_create_booking(base_url, api_sessions):
    response=api_sessions.post(f'{base_url}/booking', json=payload)
    data=response.json()

    print(data)
    print(response.headers)

    assert data['booking']['firstname'] == payload['firstname']
    assert response.status_code == 200
    assert data['booking']['bookingdates']['checkin'] == payload['bookingdates']['checkin']
    assert isinstance(data, dict)
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'

    get_response=api_sessions.get(f"{base_url}/booking/{data['bookingid']}")
    get_existing_data=get_response.json()
    print(get_existing_data)

    assert get_response.status_code == 200
    assert get_existing_data['totalprice'] == payload['totalprice']
    assert get_existing_data['additionalneeds'] == payload['additionalneeds']
    assert get_existing_data['firstname'] == payload['firstname']
    assert get_existing_data['lastname'] == payload['lastname']
