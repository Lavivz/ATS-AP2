from main import app

def test_get_produtos():

    client = app.test_client()

    response = client.get("/produtos")

    assert response.status_code == 200

    data = response.get_json()

    assert type(data) == list