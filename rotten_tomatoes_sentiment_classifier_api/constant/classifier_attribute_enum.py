from enum import Enum


class SentimentClassifierAttributeEnum(Enum):
    NEGATIVE = "0"
    SOMEWHAT_NEGATIVE = "1"
    NEUTRAL = "2"
    SOMEWHAT_POSITIVE = "3"
    POSITIVE = "4"


class SentimentAttributeEnum(Enum):
    NEGATIVE = "Negative"
    SOMEWHAT_NEGATIVE = "Somewhat Negative"
    NEUTRAL = "Neutral"
    SOMEWHAT_POSITIVE = "Somewhat Positive"
    POSITIVE = "Positive"
