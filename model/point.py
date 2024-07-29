from typing import List, Dict, Any
import pandas as pd
from model.volatile import VolatileAspect
from datetime import datetime


class Point:
    def __init__(self, lat: float, lng: float, datetime: datetime, va: List[VolatileAspect]):
        self.lat = lat  # Latitude
        self.lng = lng  # Longitude
        self.datetime = datetime  # Time
        self.va = va  # List of Volatile Aspects