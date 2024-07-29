from model.volatile import VolatileAspect
from model.point import Point
from model.trajectory import Trajectory
from model.longterm import LongTermAspect
from model.permanent import PermanentAspect
from model.mat import MultipleAspectTrajectory
import pandas as pd
from risk.riskassesment import LocationRisk
from risk.aspectguard import aspect_guard
from risk.permanentrisk import PermanentAspectRiskCalculator
from risk.longtermrisk import LongTermAspectRiskCalculator

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Mock data for MAT
    mat = MultipleAspectTrajectory(
        [Trajectory("T1", [Point(10, 20, '2021-01-01', [VolatileAspect('v1', 'V1')])], [LongTermAspect('lt1', 'L1')]),
         Trajectory("T2", [Point(10.5, 20.5, '2021-01-02', [VolatileAspect('v1', 'V2')])], [LongTermAspect('lt1', 'L1')]),
         Trajectory("T3", [Point(11, 21, '2021-01-03', [VolatileAspect('v1', 'V3')])], [LongTermAspect('lt1', 'L2')]),
         Trajectory("T4", [Point(11.5, 21.5, '2021-01-04', [VolatileAspect('v1', 'V4')])], [LongTermAspect('lt1', 'L2')]),
         Trajectory("T5", [Point(12, 22, '2021-01-05', [VolatileAspect('v1', 'V5')])], [LongTermAspect('lt1', 'L3')])],
        [PermanentAspect('aspect1', 'A'), PermanentAspect('aspect2', 'X'), PermanentAspect('aspect3', 'M')],
        '1'
    )

    # Convert MAT to DataFrame using location_sequence_attack_permanent_aspects method
    df = mat.location_sequence_attack_permanent_aspects()

    # Define columns for LocationRisk
    columns = ['lat', 'lng', 'aspect1', 'aspect2', 'aspect3']
    df['uid'] = df['user']
    # Create LocationRisk object and run the methods
    lr = LocationRisk(knowledge=2, dataset=df, columns=columns, operation='combinations', title='Location Sequence Attack with Permanent Aspects')
    lr.create_user_location()
    lr.create_counts()
    lr.evaluate_error()

    # Print risk DataFrame
    print(lr.risk)

    # Aggregate and print the error
    error_agg = lr.error_aggregate()
    print(error_agg)

    # Create and save chart
    lr.create_chart('location_risk.png', 'Location Risk Chart', [(error_agg, 'Sample Data')], ['o'])
