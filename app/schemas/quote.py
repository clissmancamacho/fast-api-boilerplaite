from typing import List

from pydantic import BaseModel


class CostBreakdownSchema(BaseModel):
    shipping_cost: float
    service_fee: float
    oversized_fee: float
    overweight_fee: float


class ShippingTimeRangeSchema(BaseModel):
    min_days: int
    max_days: int


class BoxesSchema(BaseModel):
    count: int
    weight_kg: float
    length: float
    width: float
    height: float


class QuoteSchema(BaseModel):
    shipping_channel: str
    total_cost: float
    cost_breakdown: CostBreakdownSchema
    shipping_time_range: ShippingTimeRangeSchema


class QuoteRequest(BaseModel):
    starting_country: str
    destination_country: str
    boxes: List[BoxesSchema]


class QuotesResponse(BaseModel):
    quotes: List[QuoteSchema]
