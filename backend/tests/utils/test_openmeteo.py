from tredf.intranet.services.clima import openmeteo

import pytest


@pytest.mark.parametrize(
    "value,expected",
    [
        [0, "sun"],
        [51, "cloud"],
        [99, "sun"],
    ],
)
def test_formata_weather_code(value, expected):
    assert openmeteo.formata_weather_code(value) == expected


@pytest.mark.parametrize(
    "value,expected",
    [
        ["2024-10-17T00:00", "00:00"],
        ["2024-10-17T05:00", "05:00"],
        ["2024-10-17T08:00", "08:00"],
        ["2024-10-17T23:59", "23:59"],
    ],
)
def test_formata_hora(value, expected):
    assert openmeteo.formata_hora(value) == expected
