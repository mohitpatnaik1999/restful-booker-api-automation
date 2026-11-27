import pytest, requests

@pytest.fixture(scope="session")
def base_url():
    return "https://restful-booker.herokuapp.com"

#A requests.Session() allows you to reuse settings and maintain session-level state, such as cookies, across multiple API requests.

@pytest.fixture(scope="session")
def api_sessions():
    print("\nCreating API session")

    session=requests.Session()
    yield session

    print("\nClosing API session")
    session.close()

def user_data(requests):
    return requests.param