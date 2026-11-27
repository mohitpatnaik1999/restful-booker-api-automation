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

def test_update_booking():
    create_response=requests.post(base_url, json=payload)
    create_data=create_response.json()

    assert create_response.status_code == 200
    assert isinstance(create_data, dict)

    booking_id = create_data['bookingid']

    new_url = f'{base_url}/{booking_id}'

    new_payload = {
        "firstname": "Rahul",
        "lastname": "Kumar",
        "totalprice": 1500,
        "depositpaid": "true",
        "bookingdates": {
        "checkin": "2026-12-01",
        "checkout": "2026-12-05"
        },
        "additionalneeds": "Breakfast"
    }

    update_response=requests.put(new_url, 
                                 json=new_payload,
                                 headers={"Content-Type":"application/json"},
                                 auth=("admin","password123"))

    updated_data=update_response.json()

    assert update_response.status_code == 200
    assert updated_data['firstname'] == new_payload['firstname']
    assert updated_data['lastname'] == new_payload['lastname']
    assert isinstance(updated_data, dict)
    assert updated_data['additionalneeds'] == new_payload['additionalneeds']
    