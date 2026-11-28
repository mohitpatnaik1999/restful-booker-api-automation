from jsonschema import validate
from schemas.booking_schema import booking_schema

def test_booking_schema(base_url, api_sessions):
    get_response=api_sessions.get(f'{base_url}/booking')
    assert get_response.status_code == 200
    get_data=get_response.json()

    assert len(get_data)>0

    get_booking_id=get_data[0]['bookingid']

    new_url=f'{base_url}/booking/{get_booking_id}'

    get_response_by_id=api_sessions.get(new_url)
    assert get_response_by_id.status_code == 200
    booking_data=get_response_by_id.json()

    validate(instance=booking_data,schema=booking_schema)