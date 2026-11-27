import requests
payload = {
    "firstname": "Mohit",
    "lastname": "Patnaik",
    "totalprice": 1500,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2026-12-01",
        "checkout": "2026-12-05"
    },
    "additionalneeds": "Breakfast,Lunch and Dinner"
}

base_url = "https://restful-booker.herokuapp.com/booking"

def test_delete_booking(base_url, api_sessions):
    create_response=api_sessions.post(f'{base_url}/booking', json=payload)
    new_data=create_response.json()

    booking_id = new_data['bookingid']

    assert create_response.status_code == 200
    assert isinstance(new_data, dict)

    new_url = f'{base_url}/booking/{booking_id}'

    delete_booking=api_sessions.delete(new_url,
                                   auth=("admin","password123"))

    assert delete_booking.status_code == 201

    get_response=api_sessions.get(new_url)
    assert get_response.status_code == 404