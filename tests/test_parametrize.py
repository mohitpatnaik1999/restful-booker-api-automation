import pytest, json

with open('test_data/data.json') as f:
    test_data=json.load(f)
    user_data=test_data['users']

@pytest.mark.parametrize('user_data',user_data)
def test_paramterize_booking(user_data, base_url, api_sessions):
    
    payload = {
        "firstname": user_data['firstname'],
        "lastname": user_data['lastname'],
        "totalprice": 1500,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-12-01",
            "checkout": "2026-12-05"
        },
        "additionalneeds": "Breakfast"
    }

    create_response=api_sessions.post(f'{base_url}/booking',json=payload)
    create_data=create_response.json()
    assert create_response.status_code == 200
    assert 'bookingid' in create_data
    assert create_data['booking']['totalprice'] == payload['totalprice']
    assert create_data['booking']['bookingdates']['checkin'] == payload['bookingdates']['checkin']
    assert create_data['booking']['bookingdates']['checkout'] == payload['bookingdates']['checkout']
    assert create_data['booking']['firstname'] == payload['firstname']
    assert create_data['booking']['lastname'] == payload['lastname']