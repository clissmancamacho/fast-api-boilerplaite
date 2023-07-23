from enum import Enum


class Countries(Enum):
    USA = "USA"
    CHINA = "China"
    INDIA = "India"
    VIETNAM = "Vietnam"


class ShippingChanels(Enum):
    AIR = "air"
    OCEAN = "ocean"
