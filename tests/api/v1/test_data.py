from app.schemas.quote import BoxesSchema

test_quotes_ok_data = [
    # From China #
    (
        {"starting_country": "China", "destination_country": "USA", "boxes": [{"count": 2, "weight_kg": 30, "length": 60, "width": 40, "height": 40}]},
        [
            {
                "shipping_channel": "air",
                "total_cost": 540,
                "cost_breakdown": {"shipping_cost": 240, "service_fee": 300, "oversized_fee": 0, "overweight_fee": 0},
                "shipping_time_range": {"min_days": 15, "max_days": 20},
            }
        ],
    ),
    # From China Overweight #
    (
        {"starting_country": "China", "destination_country": "USA", "boxes": [{"count": 2, "weight_kg": 40, "length": 60, "width": 40, "height": 40}]},
        [
            {
                "shipping_channel": "air",
                "total_cost": 780,
                "cost_breakdown": {"shipping_cost": 320, "service_fee": 300, "oversized_fee": 0, "overweight_fee": 160},
                "shipping_time_range": {"min_days": 15, "max_days": 20},
            }
        ],
    ),
    # From China Oversized #
    (
        {"starting_country": "China", "destination_country": "USA", "boxes": [{"count": 2, "weight_kg": 30, "length": 60, "width": 121, "height": 40}]},
        [
            {
                "shipping_channel": "air",
                "total_cost": 887.2,
                "cost_breakdown": {"shipping_cost": 387.2, "service_fee": 300, "oversized_fee": 200, "overweight_fee": 0},
                "shipping_time_range": {"min_days": 15, "max_days": 20},
            }
        ],
    ),
    # From China Oversized and Overweight #
    (
        {"starting_country": "China", "destination_country": "USA", "boxes": [{"count": 2, "weight_kg": 31, "length": 60, "width": 121, "height": 40}]},
        [
            {
                "shipping_channel": "air",
                "total_cost": 1047.2,
                "cost_breakdown": {"shipping_cost": 387.2, "service_fee": 300, "oversized_fee": 200, "overweight_fee": 160},
                "shipping_time_range": {"min_days": 15, "max_days": 20},
            }
        ],
    ),
    # From China with Air and ocean #
    (
        {
            "starting_country": "China",
            "destination_country": "USA",
            "boxes": [{"count": 2, "weight_kg": 31, "length": 60, "width": 121, "height": 40}, {"count": 4, "weight_kg": 30, "length": 60, "width": 40, "height": 40}],
        },
        [
            {
                "shipping_channel": "air",
                "total_cost": 1297,
                "cost_breakdown": {"shipping_cost": 637, "service_fee": 300, "oversized_fee": 200, "overweight_fee": 160},
                "shipping_time_range": {"min_days": 15, "max_days": 20},
            },
            {
                "shipping_channel": "ocean",
                "total_cost": 842,
                "cost_breakdown": {"shipping_cost": 182, "service_fee": 300, "oversized_fee": 200, "overweight_fee": 160},
                "shipping_time_range": {"min_days": 45, "max_days": 50},
            },
        ],
    ),
    # From India #
    (
        {"starting_country": "India", "destination_country": "USA", "boxes": [{"count": 2, "weight_kg": 14, "length": 60, "width": 40, "height": 40}]},
        [
            {
                "shipping_channel": "air",
                "total_cost": 272,
                "cost_breakdown": {"shipping_cost": 272, "service_fee": 0, "oversized_fee": 0, "overweight_fee": 0},
                "shipping_time_range": {"min_days": 10, "max_days": 15},
            }
        ],
    ),
    # From India Overweight #
    (
        {"starting_country": "India", "destination_country": "USA", "boxes": [{"count": 2, "weight_kg": 30, "length": 60, "width": 40, "height": 40}]},
        [
            {
                "shipping_channel": "air",
                "total_cost": 520,
                "cost_breakdown": {"shipping_cost": 360, "service_fee": 0, "oversized_fee": 0, "overweight_fee": 160},
                "shipping_time_range": {"min_days": 10, "max_days": 15},
            }
        ],
    ),
    # From India Oversized #
    (
        {"starting_country": "India", "destination_country": "USA", "boxes": [{"count": 2, "weight_kg": 14, "length": 60, "width": 121, "height": 40}]},
        [
            {
                "shipping_channel": "air",
                "total_cost": 780.8,
                "cost_breakdown": {"shipping_cost": 580.8, "service_fee": 0, "oversized_fee": 200, "overweight_fee": 0},
                "shipping_time_range": {"min_days": 10, "max_days": 15},
            }
        ],
    ),
    # From India Oversized and Overweight #
    (
        {"starting_country": "India", "destination_country": "USA", "boxes": [{"count": 2, "weight_kg": 30, "length": 60, "width": 121, "height": 40}]},
        [
            {
                "shipping_channel": "air",
                "total_cost": 940.8,
                "cost_breakdown": {"shipping_cost": 580.8, "service_fee": 0, "oversized_fee": 200, "overweight_fee": 160},
                "shipping_time_range": {"min_days": 10, "max_days": 15},
            }
        ],
    ),
    # From India with Air and ocean #
    (
        {
            "starting_country": "India",
            "destination_country": "USA",
            "boxes": [{"count": 2, "weight_kg": 31, "length": 60, "width": 121, "height": 40}, {"count": 4, "weight_kg": 30, "length": 60, "width": 40, "height": 40}],
        },
        [
            {
                "shipping_channel": "air",
                "total_cost": 1772,
                "cost_breakdown": {"shipping_cost": 1092, "service_fee": 0, "oversized_fee": 200, "overweight_fee": 480},
                "shipping_time_range": {"min_days": 10, "max_days": 15},
            },
            {
                "shipping_channel": "ocean",
                "total_cost": 953,
                "cost_breakdown": {"shipping_cost": 273, "service_fee": 0, "oversized_fee": 200, "overweight_fee": 480},
                "shipping_time_range": {"min_days": 40, "max_days": 50},
            },
        ],
    ),
    # From Vietnam #
    (
        {"starting_country": "Vietnam", "destination_country": "USA", "boxes": [{"count": 2, "weight_kg": 14, "length": 60, "width": 40, "height": 40}]},
        [
            {
                "shipping_channel": "air",
                "total_cost": 160,
                "cost_breakdown": {"shipping_cost": 160, "service_fee": 0, "oversized_fee": 0, "overweight_fee": 0},
                "shipping_time_range": {"min_days": 0, "max_days": 100},
            }
        ],
    ),
    # From Vietnam Overweight #
    (
        {"starting_country": "Vietnam", "destination_country": "USA", "boxes": [{"count": 2, "weight_kg": 31, "length": 60, "width": 40, "height": 40}]},
        [
            {
                "shipping_channel": "air",
                "total_cost": 470,
                "cost_breakdown": {"shipping_cost": 310, "service_fee": 0, "oversized_fee": 0, "overweight_fee": 160},
                "shipping_time_range": {"min_days": 0, "max_days": 100},
            }
        ],
    ),
    # From Vietnam Oversized #
    (
        {"starting_country": "Vietnam", "destination_country": "USA", "boxes": [{"count": 2, "weight_kg": 14, "length": 60, "width": 71, "height": 40}]},
        [
            {
                "shipping_channel": "air",
                "total_cost": 484,
                "cost_breakdown": {"shipping_cost": 284, "service_fee": 0, "oversized_fee": 200, "overweight_fee": 0},
                "shipping_time_range": {"min_days": 0, "max_days": 100},
            }
        ],
    ),
    # From Vietnam Oversized and Overweight #
    (
        {"starting_country": "Vietnam", "destination_country": "USA", "boxes": [{"count": 2, "weight_kg": 31, "length": 60, "width": 71, "height": 40}]},
        [
            {
                "shipping_channel": "air",
                "total_cost": 670,
                "cost_breakdown": {"shipping_cost": 310, "service_fee": 0, "oversized_fee": 200, "overweight_fee": 160},
                "shipping_time_range": {"min_days": 0, "max_days": 100},
            }
        ],
    ),
]

test_quotes_bad_json = {"starting_country": "Vietnam", "destination_country": "USA", "boxes": [{"weight_kg": 31, "length": 60, "width": 71, "height": 40}]}

test_calculate_gross_weight_data = [
    ([BoxesSchema(**{"count": 2, "weight_kg": 30, "length": 60, "width": 40, "height": 40})], 60),
    ([BoxesSchema(**{"count": 5, "weight_kg": 15, "length": 100, "width": 80, "height": 23})], 75),
]

test_calculate_volumetric_weight_data = [
    ([BoxesSchema(**{"count": 2, "weight_kg": 30, "length": 60, "width": 40, "height": 40})], 32),
    ([BoxesSchema(**{"count": 5, "weight_kg": 15, "length": 100, "width": 80, "height": 23})], 153.33),
]

test_overweighed_boxes_fee_data = [
    ("China", [BoxesSchema(**{"count": 2, "weight_kg": 30, "length": 60, "width": 40, "height": 40})], 0),
    ("India", [BoxesSchema(**{"count": 5, "weight_kg": 15, "length": 100, "width": 80, "height": 23})], 400),
    ("Vietnam", [BoxesSchema(**{"count": 5, "weight_kg": 15, "length": 100, "width": 80, "height": 23})], 0),
]

test_oversized_boxes_fee_data = [
    ("China", [BoxesSchema(**{"count": 2, "weight_kg": 30, "length": 60, "width": 121, "height": 40})], 200),
    ("Vietnam", [BoxesSchema(**{"count": 5, "weight_kg": 15, "length": 71, "width": 20, "height": 23})], 500),
    ("India", [BoxesSchema(**{"count": 5, "weight_kg": 15, "length": 71, "width": 20, "height": 23})], 0),
]

test_calculate_service_fee_data = [
    ("China", 300),
    ("Vietnam", 0),
    ("India", 0),
]
