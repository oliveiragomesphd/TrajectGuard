from typing import List, Dict, Any
import pandas as pd


class PermanentAspect:
    def __init__(self, name: str, aspect: str):
        self.name = name
        self.aspect = aspect