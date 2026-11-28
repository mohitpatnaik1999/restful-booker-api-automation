def test_inavlid_booking_check(base_url, api_sessions):
    get_invalid_response=api_sessions.get(f'{base_url}/booking/123456677')
    print(get_invalid_response.text)

    assert get_invalid_response.text == 'Not Found'
    assert get_invalid_response.status_code == 404

def test_invalid_authentication(base_url, api_sessions):
    payload = {
        "firstname": "Mohit",
        "lastname": "Patnaik",
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
    assert isinstance(create_data,dict)

    booking_id=create_data['bookingid']

    new_url=f'{base_url}/booking/{booking_id}'

    update_invalid_authentication = api_sessions.put(new_url,
                                                     json=payload,
                                                     auth=("wrong_user", "wrong_password"))

    print(update_invalid_authentication.text)
    assert update_invalid_authentication.text == 'Forbidden'
    assert update_invalid_authentication.status_code == 403
