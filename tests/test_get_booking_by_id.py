import requests
def test_get_booking_by_id(base_url, api_sessions):
    response=api_sessions.get(f'{base_url}/booking')

    assert response.status_code == 200

    booking_data=response.json()
    assert isinstance(booking_data, list)

    booking_id=booking_data[1]['bookingid']

    #booking_id is a path parameter which helps to get booking_id as specified.
    response=api_sessions.get(f'{base_url}/booking/{booking_id}')

    assert "firstname" in response.json()
    assert "lastname" in response.json()
    assert isinstance(response.json(),dict)

    print(booking_id)

    assert response.status_code == 200