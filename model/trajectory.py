from typing import List, Dict, Any
import pandas as pd
from model.point import Point
from model.longterm import LongTermAspect


class Trajectory:
    def __init__(self, identifier: str, points: List[Point], long_term_aspects: List[LongTermAspect]):
        self.identifier = identifier  # Identifier for the trajectory
        self.points = points
        self.long_term_aspects = long_term_aspects  # List of long-term aspects
