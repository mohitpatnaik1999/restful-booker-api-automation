import requests

def test_get_booking():
     url = "https://restful-booker.herokuapp.com/booking"
     response=requests.get(url)

     data=response.json()
     print(response.status_code)
     print(data)

     print(response.headers)

     total_bookings = len(response.json())

     print(data[0]['bookingid'])

     assert response.status_code == 200
     assert response.headers["Content-Type"] == 'application/json; charset=utf-8'
     assert isinstance(data, list)
     assert len(data) > 0
     assert 'bookingid' in data[0]