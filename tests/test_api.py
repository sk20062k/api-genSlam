import requests

# Change this to your laptop’s local IP (visible by phone on same Wi-Fi)
BASE_URL = "http://192.168.1.16:8000/"  # or "http://192.168.x.x:8000"


# 1. Test GET endpoint
def test_root():
    response = requests.get(f"{BASE_URL}/")
    print("GET / Response:")
    print(response.status_code, response.json())
    return None


# 2. Test POST endpoint
def test_move():
    payload = {"command": "move_forward", "speed": 1000}
    response = requests.post(f"{BASE_URL}/move", json=payload)
    print("\nPOST /move Response:")
    print(response.status_code, response.json())
    return None


if __name__ == "__main__":
    assert test_root() is None
    assert test_move() is None
