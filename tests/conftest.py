import pytest

@pytest.fixture
def test_ip():
    return "192.168.1.5"

@pytest.fixture
def url(test_ip):
    return f"http://{test_ip}/data.json"

@pytest.fixture
def json_data():
    return {
        "software_version": "R_2025-03",
        "sensor_id": "5366960e8b18",
        "sensordatavalues": [
            {"value_type": "signal", "value": "-48"},
            {"value_type": "SDS_P1", "value": "1.55"},
            {"value_type": "SDS_P2", "value": "0.508333"},
            {"value_type": "BME280_humidity", "value": "40.03418"},
            {"value_type": "BME280_temperature", "value": "21.34277"},
            {"value_type": "BME280_pressure", "value": "101636.6"},
            {"value_type": "PCBA_noiseMax", "value": "59"},
            {"value_type": "PCBA_noiseAvg", "value": "53"},
        ],
    }
