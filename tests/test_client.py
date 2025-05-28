import pytest
from aiohttp import ClientSession
from aioresponses import aioresponses
from altruistclient.client import AltruistClient
from altruistclient.model import AltruistDeviceModel


@pytest.mark.asyncio
async def test_from_ip(test_ip, url, json_data):
    device = AltruistDeviceModel(id="5366960e8b18", ip_address=test_ip)
    async with ClientSession() as session:
        with aioresponses() as mocked:
            mocked.get(url, payload=json_data)
            client = await AltruistClient.from_ip_address(session, test_ip)
            assert client.device.id == "5366960e8b18"
            assert client.device.ip_address == test_ip
            assert client.fw_version == "R_2025-03"


@pytest.mark.asyncio
async def test_fetch_data(test_ip, url, json_data):
    device = AltruistDeviceModel(id="5366960e8b18", ip_address=test_ip)
    async with ClientSession() as session:
        with aioresponses() as mocked:
            mocked.get(url, payload=json_data)
            client = AltruistClient(session, device)
            data = await client.fetch_data()
            assert "SDS_P1" in client.sensor_names
            assert "SDS_P2" in client.sensor_names
            assert "BME280_humidity" in client.sensor_names
            assert "BME280_temperature" in client.sensor_names
            assert "BME280_pressure" in client.sensor_names
            assert "PCBA_noiseMax" in client.sensor_names
            assert "PCBA_noiseAvg" in client.sensor_names
            assert "signal" in client.sensor_names
            assert client.fw_version == "R_2025-03"
            assert len(data) == 8
