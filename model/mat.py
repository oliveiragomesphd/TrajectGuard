from typing import List, Dict, Any
import pandas as pd
from model.volatile import VolatileAspect
from model.point import Point
from model.trajectory import Trajectory
from model.longterm import LongTermAspect
from model.permanent import PermanentAspect
import pandas as pd

class MultipleAspectTrajectory:
    def __init__(self, trajectories: List[Trajectory], permanent_aspects: List[PermanentAspect], user_id: str):
        self.trajectories = trajectories  # List of trajectories
        self.permanent_aspects = permanent_aspects  # List of permanent aspects
        self.user_id = user_id  # Moving object identifier

    def get_permanent_aspects(self) -> Dict[str, str]:
        return {lta.name: lta.aspect for lta in self.permanent_aspects}

    def get_volatile_aspects(self, point: Point) -> Dict[str, str]:
        return {va.name: va.aspect for va in point.va}

    def get_long_term_aspects(self, trajectory: Trajectory) -> Dict[str, str]:
        return {lta.name: lta.aspect for lta in trajectory.long_term_aspects}

    def location_sequence_attack_long_term_aspects(self) -> pd.DataFrame:
        data = []
        for trajectory in self.trajectories:
            long_term_aspects = self.get_long_term_aspects(trajectory)
            for point in trajectory.points:
                record = {
                    "user": self.user_id,
                    "trajectory_id": trajectory.identifier,
                    "lat": point.lat,
                    "lng": point.lng,
                }
                record.update(long_term_aspects)
                data.append(record)
        return pd.DataFrame(data)

    def visit_attack_long_term_aspects(self) -> pd.DataFrame:
        data = []
        for trajectory in self.trajectories:
            long_term_aspects = self.get_long_term_aspects(trajectory)
            for point in trajectory.points:
                record = {
                    "user": self.user_id,
                    "trajectory_id": trajectory.identifier,
                    "lat": point.lat,
                    "lng": point.lng,
                    "datetime": point.datetime,
                }
                record.update(long_term_aspects)
                data.append(record)
        return pd.DataFrame(data)

    def location_sequence_attack_permanent_aspects(self) -> pd.DataFrame:
        data = []
        permanent_aspects = self.get_permanent_aspects()
        for trajectory in self.trajectories:
            for point in trajectory.points:
                record = {
                    "user": self.user_id,
                    "trajectory_id": trajectory.identifier,
                    "lat": point.lat,
                    "lng": point.lng,
                }
                record.update(permanent_aspects)
                data.append(record)
        return pd.DataFrame(data)

    def location_sequence_attack_volatile_aspects(self) -> pd.DataFrame:
        data = []
        for trajectory in self.trajectories:
            for point in trajectory.points:
                volatile_aspects = self.get_volatile_aspects(point)
                record = {
                    "user": self.user_id,
                    "trajectory_id": trajectory.identifier,
                    "lat": point.lat,
                    "lng": point.lng,
                }
                record.update(volatile_aspects)
                data.append(record)
        return pd.DataFrame(data)

    def location_sequence_attack_permanent_long_term_aspects(self) -> pd.DataFrame:
        data = []
        permanent_aspects = self.get_permanent_aspects()
        for trajectory in self.trajectories:
            long_term_aspects = self.get_long_term_aspects(trajectory)
            for point in trajectory.points:
                record = {
                    "user": self.user_id,
                    "trajectory_id": trajectory.identifier,
                    "lat": point.lat,
                    "lng": point.lng,
                }
                record.update(permanent_aspects)
                record.update(long_term_aspects)
                data.append(record)
        return pd.DataFrame(data)

    def location_sequence_attack_permanent_volatile_aspects(self) -> pd.DataFrame:
        data = []
        permanent_aspects = self.get_permanent_aspects()
        for trajectory in self.trajectories:
            for point in trajectory.points:
                volatile_aspects = self.get_volatile_aspects(point)
                record = {
                    "user": self.user_id,
                    "trajectory_id": trajectory.identifier,
                    "lat": point.lat,
                    "lng": point.lng,
                }
                record.update(permanent_aspects)
                record.update(volatile_aspects)
                data.append(record)
        return pd.DataFrame(data)

    def location_sequence_attack_long_term_volatile_aspects(self) -> pd.DataFrame:
        data = []
        for trajectory in self.trajectories:
            long_term_aspects = self.get_long_term_aspects(trajectory)
            for point in trajectory.points:
                volatile_aspects = self.get_volatile_aspects(point)
                record = {
                    "user": self.user_id,
                    "trajectory_id": trajectory.identifier,
                    "lat": point.lat,
                    "lng": point.lng,
                }
                record.update(long_term_aspects)
                record.update(volatile_aspects)
                data.append(record)
        return pd.DataFrame(data)

    def location_sequence_attack_permanent_long_term_volatile_aspects(self) -> pd.DataFrame:
        data = []
        permanent_aspects = self.get_permanent_aspects()
        for trajectory in self.trajectories:
            long_term_aspects = self.get_long_term_aspects(trajectory)
            for point in trajectory.points:
                volatile_aspects = self.get_volatile_aspects(point)
                record = {
                    "user": self.user_id,
                    "trajectory_id": trajectory.identifier,
                    "lat": point.lat,
                    "lng": point.lng,
                }
                record.update(permanent_aspects)
                record.update(long_term_aspects)
                record.update(volatile_aspects)
                data.append(record)
        return pd.DataFrame(data)

    def visit_attack_permanent_aspects(self) -> pd.DataFrame:
        data = []
        permanent_aspects = self.get_permanent_aspects()
        for trajectory in self.trajectories:
            for point in trajectory.points:
                record = {
                    "user": self.user_id,
                    "trajectory_id": trajectory.identifier,
                    "lat": point.lat,
                    "lng": point.lng,
                    "datetime": point.datetime,
                }
                record.update(permanent_aspects)
                data.append(record)
        return pd.DataFrame(data)

    def visit_attack_volatile_aspects(self) -> pd.DataFrame:
        data = []
        for trajectory in self.trajectories:
            for point in trajectory.points:
                volatile_aspects = self.get_volatile_aspects(point)
                record = {
                    "user": self.user_id,
                    "trajectory_id": trajectory.identifier,
                    "lat": point.lat,
                    "lng": point.lng,
                    "datetime": point.datetime,
                }
                record.update(volatile_aspects)
                data.append(record)
        return pd.DataFrame(data)

    def visit_attack_permanent_long_term_aspects(self) -> pd.DataFrame:
        data = []
        permanent_aspects = self.get_permanent_aspects()
        for trajectory in self.trajectories:
            long_term_aspects = self.get_long_term_aspects(trajectory)
            for point in trajectory.points:
                record = {
                    "user": self.user_id,
                    "trajectory_id": trajectory.identifier,
                    "lat": point.lat,
                    "lng": point.lng,
                    "datetime": point.datetime,
                }
                record.update(permanent_aspects)
                record.update(long_term_aspects)
                data.append(record)
        return pd.DataFrame(data)

    def visit_attack_permanent_volatile_aspects(self) -> pd.DataFrame:
        data = []
        permanent_aspects = self.get_permanent_aspects()
        for trajectory in self.trajectories:
            for point in trajectory.points:
                volatile_aspects = self.get_volatile_aspects(point)
                record = {
                    "user": self.user_id,
                    "trajectory_id": trajectory.identifier,
                    "lat": point.lat,
                    "lng": point.lng,
                    "datetime": point.datetime,
                }
                record.update(permanent_aspects)
                record.update(volatile_aspects)
                data.append(record)
        return pd.DataFrame(data)

    def visit_attack_long_term_volatile_aspects(self) -> pd.DataFrame:
        data = []
        for trajectory in self.trajectories:
            long_term_aspects = self.get_long_term_aspects(trajectory)
            for point in trajectory.points:
                volatile_aspects = self.get_volatile_aspects(point)
                record = {
                    "user": self.user_id,
                    "trajectory_id": trajectory.identifier,
                    "lat": point.lat,
                    "lng": point.lng,
                    "datetime": point.datetime,
                }
                record.update(long_term_aspects)
                record.update(volatile_aspects)
                data.append(record)
        return pd.DataFrame(data)

    def visit_attack_permanent_long_term_volatile_aspects(self) -> pd.DataFrame:
        data = []
        permanent_aspects = self.get_permanent_aspects()
        for trajectory in self.trajectories:
            long_term_aspects = self.get_long_term_aspects(trajectory)
            for point in trajectory.points:
                volatile_aspects = self.get_volatile_aspects(point)
                record = {
                    "user": self.user_id,
                    "trajectory_id": trajectory.identifier,
                    "lat": point.lat,
                    "lng": point.lng,
                    "datetime": point.datetime,
                }
                record.update(permanent_aspects)
                record.update(long_term_aspects)
                record.update(volatile_aspects)
                data.append(record)
        return pd.DataFrame(data)

    @staticmethod
    def from_dataframe(df: pd.DataFrame, lat_col: str, lng_col: str, datetime_col: str,
                       permanent_aspect_cols: List[str], long_term_aspect_cols: List[str],
                       volatile_aspect_cols: List[str], user_id: str) -> 'MultipleAspectTrajectory':
        # Enforce column types
        df[lat_col] = pd.to_numeric(df[lat_col])
        df[lng_col] = pd.to_numeric(df[lng_col])
        df[datetime_col] = pd.to_datetime(df[datetime_col])

        trajectories = []
        permanent_aspects = [LongTermAspect(name=col, aspect=str(df[col].iloc[0])) for col in permanent_aspect_cols]

        for trajectory_id, group in df.groupby('trajectory_id'):
            points = []
            long_term_aspects = [LongTermAspect(name=col, aspect=str(group[col].iloc[0])) for col in
                                 long_term_aspect_cols]

            for _, row in group.iterrows():
                volatile_aspects = [VolatileAspect(name=col, aspect=row[col]) for col in volatile_aspect_cols]
                point = Point(lat=row[lat_col], lng=row[lng_col], datetime=row[datetime_col].isoformat(),
                              va=volatile_aspects)
                points.append(point)

            trajectory = Trajectory(identifier=trajectory_id, points=points, long_term_aspects=long_term_aspects)
            trajectories.append(trajectory)

        return MultipleAspectTrajectory(trajectories=trajectories, permanent_aspects=permanent_aspects, u=user_id)