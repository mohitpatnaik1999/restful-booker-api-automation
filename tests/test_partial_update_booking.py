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

def test_update_partial_booking():
    create_response=requests.post(base_url, json=payload)
    create_new_data=create_response.json()

    booking_id = create_new_data['bookingid']

    new_url = f'{base_url}/{booking_id}'

    new_payload = {
        "totalprice": 2000
    }

    update_partial_response=requests.patch(new_url,
                                           json=new_payload,
                                           headers={"Content-type":"application/json"},
                                           auth=("admin","password123"))

    updated_partial_data=update_partial_response.json()

    assert update_partial_response.status_code == 200
    assert updated_partial_data['totalprice'] == new_payload['totalprice']
    assert updated_partial_data['firstname'] == payload['firstname']
    assert updated_partial_data['lastname'] == payload['lastname']