import requests
import sys

BASE_URL = "http://127.0.0.1:8000"

def test_sum():
    resp = requests.get(f"{BASE_URL}/sum?a=10&b=5")
    assert resp.status_code == 200
    assert resp.json() == {"result": 15}
    print("Sum test passed")

def test_mul():
    resp = requests.get(f"{BASE_URL}/mul?a=10&b=5")
    assert resp.status_code == 200
    assert resp.json() == {"result": 50}
    print("Mul test passed")

def test_div():
    resp = requests.get(f"{BASE_URL}/div?a=10&b=2")
    assert resp.status_code == 200
    assert resp.json() == {"result": 5.0}
    print("Div test passed")

def test_index():
    resp = requests.get(BASE_URL)
    assert resp.status_code == 200
    assert "Calculator" in resp.text
    print("Index page load passed")

if __name__ == "__main__":
    try:
        test_sum()
        test_mul()
        test_div()
        test_index()
        print("All tests passed!")
    except Exception as e:
        print(f"Test failed: {e}")
        sys.exit(1)
