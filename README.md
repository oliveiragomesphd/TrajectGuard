# TrajectGuard: Location Risk Analysis with Multiple Aspect Trajectories (MAT)

This repository provides an implementation for analyzing the risk of location-based attacks using the **TrajectGuard** framework. The project includes methods to generate combinations of location data aspects and calculate the risk of unique identification.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [MAT Class Definitions](#mat-class-definitions)
  - [LocationRisk Analysis](#locationrisk-analysis)
  - [Example Usage](#example-usage)
- [TrajectGuard Framework](#trajectguard-framework)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project implements a risk analysis tool for location data using Multiple Aspect Trajectories (MAT). MAT consists of various aspects of location data, including permanent, long-term, and volatile aspects. The risk analysis tool calculates the likelihood of unique identification based on combinations of these aspects.

## Features

- Define and handle multiple aspect trajectories.
- Convert MAT objects to DataFrames for analysis.
- Generate combinations of data aspects for risk analysis.
- Calculate the risk of unique identification based on location data aspects.
- Visualize risk analysis results.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/TrajectGuard.git
    ```

2. Change to the project directory:
    ```bash
    cd TrajectGuard
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### MAT Class Definitions

The `MultipleAspectTrajectory` class represents a user's trajectory data with various aspects:
- `PermanentAspect`: Permanent characteristics.
- `LongTermAspect`: Long-term aspects associated with trajectories.
- `VolatileAspect`: Short-term, volatile aspects associated with points in trajectories.

### LocationRisk Analysis

The `LocationRisk` class performs risk analysis based on combinations of location data aspects. It calculates the risk of unique identification using methods such as combinations or permutations of data aspects.

### Example Usage

#### Permanent Aspect Risk

```python
from model.volatile import VolatileAspect
from model.point import Point
from model.trajectory import Trajectory
from model.longterm import LongTermAspect
from model.permanent import PermanentAspect
from model.mat import MultipleAspectTrajectory
from risk.permanentrisk import PermanentAspectRiskCalculator

# Define a list of MATs
mat_list = [
    MultipleAspectTrajectory(
        [Trajectory("T1", [Point(10, 20, '2021-01-01', [VolatileAspect('v1', 'V1')])], [LongTermAspect('lt1', 'L1')])],
        [PermanentAspect('aspect1', 'A'), PermanentAspect('aspect2', 'X'), PermanentAspect('aspect3', 'M')],
        '1'
    ),
    MultipleAspectTrajectory(
        [Trajectory("T2", [Point(10, 20, '2021-01-01', [VolatileAspect('v1', 'V2')])], [LongTermAspect('lt1', 'L1')])],
        [PermanentAspect('aspect1', 'A'), PermanentAspect('aspect2', 'Y'), PermanentAspect('aspect3', 'N')],
        '2'
    ),
    MultipleAspectTrajectory(
        [Trajectory("T3", [Point(10, 20, '2021-01-01', [VolatileAspect('v1', 'V3')])], [LongTermAspect('lt1', 'L2')])],
        [PermanentAspect('aspect1', 'B'), PermanentAspect('aspect2', 'X'), PermanentAspect('aspect3', 'N')],
        '3'
    ),
    MultipleAspectTrajectory(
        [Trajectory("T4", [Point(10, 20, '2021-01-01', [VolatileAspect('v1', 'V4')])], [LongTermAspect('lt1', 'L2')])],
        [PermanentAspect('aspect1', 'B'), PermanentAspect('aspect2', 'Y'), PermanentAspect('aspect3', 'M')],
        '4'
    ),
    MultipleAspectTrajectory(
        [Trajectory("T5", [Point(10, 20, '2021-01-01', [VolatileAspect('v1', 'V5')])], [LongTermAspect('lt1', 'L3')])],
        [PermanentAspect('aspect1', 'C'), PermanentAspect('aspect2', 'X'), PermanentAspect('aspect3', 'M')],
        '5'
    ),
    MultipleAspectTrajectory(
        [Trajectory("T6", [Point(10, 20, '2021-01-01', [VolatileAspect('v1', 'V6')])], [LongTermAspect('lt1', 'L3')])],
        [PermanentAspect('aspect1', 'A'), PermanentAspect('aspect2', 'X'), PermanentAspect('aspect3', 'M')],
        '6'
    )
]

# Instantiate the calculator and calculate risk
calculator = PermanentAspectRiskCalculator(mat_list)
calculator.calculate_risk()
risk_df = calculator.get_risk()

# Print the resulting DataFrame with risks
print(risk_df)
```
#### Long-Term Aspect Risk
```python
from model.volatile import VolatileAspect
from model.point import Point
from model.trajectory import Trajectory
from model.longterm import LongTermAspect
from model.permanent import PermanentAspect
from model.mat import MultipleAspectTrajectory
from risk.longtermrisk import LongTermAspectRiskCalculator

# Define a list of MATs
mat_list = [
    MultipleAspectTrajectory(
        [Trajectory("T1", [Point(10, 20, '2021-01-01', [VolatileAspect('v1', 'V1')])], [LongTermAspect('lt1', 'L1')])],
        [PermanentAspect('aspect1', 'A'), PermanentAspect('aspect2', 'X'), PermanentAspect('aspect3', 'M')],
        '1'
    ),
    MultipleAspectTrajectory(
        [Trajectory("T2", [Point(10, 20, '2021-01-01', [VolatileAspect('v1', 'V2')])], [LongTermAspect('lt1', 'L1')])],
        [PermanentAspect('aspect1', 'A'), PermanentAspect('aspect2', 'Y'), PermanentAspect('aspect3', 'N')],
        '2'
    ),
    MultipleAspectTrajectory(
        [Trajectory("T3", [Point(10, 20, '2021-01-01', [VolatileAspect('v1', 'V3')])], [LongTermAspect('lt1', 'L2')])],
        [PermanentAspect('aspect1', 'B'), PermanentAspect('aspect2', 'X'), PermanentAspect('aspect3', 'N')],
        '3'
    ),
    MultipleAspectTrajectory(
        [Trajectory("T4", [Point(10, 20, '2021-01-01', [VolatileAspect('v1', 'V4')])], [LongTermAspect('lt1', 'L2')])],
        [PermanentAspect('aspect1', 'B'), PermanentAspect('aspect2', 'Y'), PermanentAspect('aspect3', 'M')],
        '4'
    ),
    MultipleAspectTrajectory(
        [Trajectory("T5", [Point(10, 20, '2021-01-01', [VolatileAspect('v1', 'V5')])], [LongTermAspect('lt1', 'L3')])],
        [PermanentAspect('aspect1', 'C'), PermanentAspect('aspect2', 'X'), PermanentAspect('aspect3', 'M')],
        '5'
    ),
    MultipleAspectTrajectory(
        [Trajectory("T6", [Point(10, 20, '2021-01-01', [VolatileAspect('v1', 'V6')])], [LongTermAspect('lt1', 'L3')])],
        [PermanentAspect('aspect1', 'A'), PermanentAspect('aspect2', 'X'), PermanentAspect('aspect3', 'M')],
        '6'
    )
]

# Instantiate the calculator and calculate risk
calculator = LongTermAspectRiskCalculator(mat_list)
calculator.calculate_risk()
risk_df = calculator.get_risk()

# Print the resulting DataFrame with risks
print(risk_df)
```
#### AspectGuard

```python
from model.volatile import VolatileAspect
from model.point import Point
from model.trajectory import Trajectory
from model.longterm import LongTermAspect
from model.permanent import PermanentAspect
from model.mat import MultipleAspectTrajectory
from aspect_guard import aspect_guard

mat = MultipleAspectTrajectory(
    [Trajectory("T1", [Point(10, 20, '2021-01-01', [VolatileAspect('v1', 'V1')])], [LongTermAspect('lt1', 'L1')]),
     Trajectory("T2", [Point(10.5, 20.5, '2021-01-02', [VolatileAspect('v1', 'V2')])], [LongTermAspect('lt1', 'L1')]),
     Trajectory("T3", [Point(11, 21, '2021-01-03', [VolatileAspect('v1', 'V3')])], [LongTermAspect('lt1', 'L2')]),
     Trajectory("T4", [Point(11.5, 21.5, '2021-01-04', [VolatileAspect('v1', 'V4')])], [LongTermAspect('lt1', 'L2')]),
     Trajectory("T5", [Point(12, 22, '2021-01-05', [VolatileAspect('v1', 'V5')])], [LongTermAspect('lt1', 'L3')])],
    [PermanentAspect('aspect1', 'A'), PermanentAspect('aspect2', 'X'), PermanentAspect('aspect3', 'M')],
    '1'
)

# Example columns list
columns_list = [
    'lat', 'lng', 'datetime', 'aspect1', 'aspect2', 'aspect3', 'v1'
]

# Run aspect_guard
aspect_guard(mat, columns_list)
```

#### MAT Risk Assesment and AnonimoGuard
```python
from model.volatile import VolatileAspect
from model.point import Point
from model.trajectory import Trajectory
from model.longterm import LongTermAspect
from model.permanent import PermanentAspect
from model.mat import MultipleAspectTrajectory
from location_risk import LocationRisk

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

# Create LocationRisk object and run the methods, for AnonimoGuard add the dataset anonymized in anonimo parameter
lr = LocationRisk(knowledge=2, dataset=df, columns=columns, operation='combinations', title='Location Sequence Attack with Permanent Aspects', anonimo=None)
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
```

