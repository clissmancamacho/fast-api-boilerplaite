from functools import reduce

from app.database.enums import Countries
from app.schemas.quote import (
    BoxesSchema,
    CostBreakdownSchema,
    QuoteSchema,
    ShippingTimeRangeSchema,
)


def calculate_gross_weight(boxes: BoxesSchema):
    return round(reduce(lambda x, y: x + y, [box.weight_kg * box.count for box in boxes], 0), 2)


def calculate_volumetric_weight(boxes: BoxesSchema):
    return round(reduce(lambda x, y: x + y, [(box.width * box.height * box.length * box.count) / 6000 for box in boxes], 0), 2)


def overweighed_boxes_fee(origin_country: str, boxes: BoxesSchema):
    overweight = 15 if origin_country.upper() == str(Countries.INDIA.value).upper() else 31
    boxes_overweighed = filter(lambda box: box.weight_kg >= overweight, boxes)
    return round(reduce(lambda x, y: x + y, [box.count * 80 for box in boxes_overweighed], 0), 2)


def oversized_boxes_fee(origin_country: str, boxes: BoxesSchema):
    oversize = 70 if origin_country.upper() == str(Countries.VIETNAM.value).upper() else 120
    boxes_oversized = filter(lambda box: box.width > oversize or box.height > oversize or box.length > oversize, boxes)
    return round(reduce(lambda x, y: x + y, [box.count * 100 for box in boxes_oversized], 0), 2)


def calculate_service_fee(origin_country: str):
    return 300 if origin_country.upper() == str(Countries.CHINA.value).upper() else 0


def calculate_final_quotes(routes, chargeable_weight, overweight_fee, oversized_fee, service_fee):
    response_list = []
    for route in routes:
        quote_dict = {}
        quote_dict["shipping_channel"] = route.shipping_channel
        quote_dict["cost_breakdown"] = calculate_cost_breakdown(route, chargeable_weight, overweight_fee, oversized_fee, service_fee)
        if not quote_dict["cost_breakdown"]:
            continue
        quote_dict["total_cost"] = (
            quote_dict["cost_breakdown"]["shipping_cost"] + quote_dict["cost_breakdown"]["service_fee"] + quote_dict["cost_breakdown"]["oversized_fee"] + quote_dict["cost_breakdown"]["overweight_fee"]
        )
        quote_dict["shipping_time_range"] = {"min_days": route.min_shipping_range, "max_days": route.max_shipping_range}
        quote = QuoteSchema(
            shipping_channel=quote_dict["shipping_channel"],
            total_cost=quote_dict["total_cost"],
            cost_breakdown=CostBreakdownSchema(**quote_dict["cost_breakdown"]),
            shipping_time_range=ShippingTimeRangeSchema(**quote_dict["shipping_time_range"]),
        )
        response_list.append(quote)
    return response_list


def calculate_cost_breakdown(route, chargeable_weight, overweight_fee, oversized_fee, service_fee):
    cost_breakdown_dict = {}
    shipping_cost = 0
    for rate in route.rates:
        if chargeable_weight >= rate.min_weight_kg and chargeable_weight <= rate.max_weight_kg:
            shipping_cost = chargeable_weight * rate.per_kg_rate
            break
    if shipping_cost == 0:
        return False
    cost_breakdown_dict["shipping_cost"] = shipping_cost
    cost_breakdown_dict["service_fee"] = service_fee
    cost_breakdown_dict["oversized_fee"] = oversized_fee
    cost_breakdown_dict["overweight_fee"] = overweight_fee
    return cost_breakdown_dict
