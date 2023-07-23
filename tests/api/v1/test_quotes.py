from os import environ

import pytest
from fastapi import FastAPI
from httpx import AsyncClient

# from fastapi.testclient import TestClient
from starlette.status import HTTP_200_OK, HTTP_422_UNPROCESSABLE_ENTITY

from app.utils import (
    calculate_gross_weight,
    calculate_service_fee,
    calculate_volumetric_weight,
    oversized_boxes_fee,
    overweighed_boxes_fee,
)

from .test_data import (
    test_calculate_gross_weight_data,
    test_calculate_service_fee_data,
    test_calculate_volumetric_weight_data,
    test_oversized_boxes_fee_data,
    test_overweighed_boxes_fee_data,
    test_quotes_bad_json,
    test_quotes_ok_data,
)

environ["APP_ENV"] = "test"

pytestmark = pytest.mark.asyncio


@pytest.mark.parametrize("entry,expected", test_quotes_ok_data)
async def test_quotes_ok(*, entry, expected, app: FastAPI, client: AsyncClient) -> None:
    response = await client.post(app.url_path_for("quotes"), json=entry)
    result = response.json()
    quotes = result.get("quotes")
    assert response.status_code == HTTP_200_OK
    assert len(quotes) == len(expected)
    assert quotes == expected


async def test_quotes_bad_json_entry(app: FastAPI, client: AsyncClient) -> None:
    response = await client.post(app.url_path_for("quotes"), json=test_quotes_bad_json)
    assert response.status_code == HTTP_422_UNPROCESSABLE_ENTITY


@pytest.mark.parametrize("entry,expected", test_calculate_gross_weight_data)
async def test_calculate_gross_weight(*, entry, expected) -> None:
    assert calculate_gross_weight(entry) == expected


@pytest.mark.parametrize("entry,expected", test_calculate_volumetric_weight_data)
async def test_calculate_volumetric_weight(*, entry, expected) -> None:
    assert calculate_volumetric_weight(entry) == expected


@pytest.mark.parametrize("entry1, entry2, expected", test_overweighed_boxes_fee_data)
async def test_overweighed_boxes_fee(*, entry1, entry2, expected) -> None:
    assert overweighed_boxes_fee(entry1, entry2) == expected


@pytest.mark.parametrize("entry1, entry2, expected", test_oversized_boxes_fee_data)
async def test_oversized_boxes_fee(*, entry1, entry2, expected) -> None:
    assert oversized_boxes_fee(entry1, entry2) == expected


@pytest.mark.parametrize("entry, expected", test_calculate_service_fee_data)
async def test_calculate_service_fee(*, entry, expected) -> None:
    assert calculate_service_fee(entry) == expected
