import pandas as pd
import numpy as np


def get_pollution_data(
    field: str,
    id: int,
    size=1000,
    depth_sin_var=2,
    depth_mean=25,
    depth_noise_var=2.5,
    temp_log_mult=3.5,
    temp_max=16,
    oil_spill_mean=0.4,
    oil_spill_var=0.3,
    oil_min=0.2,
    oil_max=10,
    oil_surface_chance=0.2,
):
    """Generate pollution data. Based of ID123 in ISD4000"""
    df = pd.DataFrame()

    time = np.arange(0, size)
    df["time"] = time

    field_col = np.array([field] * size)
    df["field"] = field_col

    id_col = np.ones(size) * id
    df["id"] = id_col

    # Generate depth values based on sin and noise
    sinus = np.sin(np.arange(0, size / 5, 0.2)) * depth_sin_var + depth_mean
    depth = sinus + np.random.normal(0, depth_noise_var, size)
    depth += np.random.choice([0, 1.5, -4], size=size, p=[0.8, 0.15, 0.05])
    depth_day = np.random.randint(0, 165)
    for i in range(size // 168 + 1):
        depth[i * 168 + depth_day : i * 168 + depth_day + 3] -= 22
    # clip to avoid - values
    depth = np.clip(depth, 0, 50)
    df["depth"] = depth

    # get pressure based on depth
    pressure = depth * 9.81 + np.random.normal(0, 3, size)
    df["pressure"] = pressure

    # get temperature based on depth
    temperature = -np.log(depth + 0.1) * temp_log_mult + temp_max
    temperature = np.clip(temperature, 2.5, temp_max)
    temperature += np.random.normal(0, 0.2, size)
    df["temperature"] = temperature

    oil_spill = np.random.normal(oil_spill_mean, oil_spill_var, size) + np.clip(
        -depth + 10, 0, oil_max
    )
    oil_spill = np.clip(oil_spill, oil_min, oil_max)
    for i in range(size // 168 + 1):
        if np.random.uniform(0, 1, 1)[0] > oil_surface_chance:
            oil_spill[i * 168 : i * 168 + 168] = np.clip(
                oil_spill[i * 168 : i * 168 + 168], 0, 1
            )
    oil_spill += np.random.normal(0, 0.05, size)
    df["oil_spill"] = oil_spill

    return df


OIL_FIELDS = np.array(["Frigg", "Magnus", "Troll", "Gullfaks", "Viking", "Snorre"])
SIZE = 1000
NUM_BUOYS = [5, 3, 7, 5, 4, 4]
pollution_df = pd.DataFrame()
for idx, field in enumerate(OIL_FIELDS):
    # Set distributions based on oil_fields
    depth_sin_var = 2 + np.random.normal(0, 0.3, 1)[0]
    depth_mean = 25 + np.random.normal(0, 2, 1)[0]
    depth_noise_var = 2.5 + np.random.normal(0, 0.2, 1)[0]
    temp_log_mult = 3.5 + np.random.normal(0, 0.3, 1)[0]
    temp_max = 16 + np.random.normal(0, 1, 1)[0]
    oil_spill_mean = 0.4 + np.random.normal(0, 0.3, 1)[0]
    oil_spill_var = 0.3 + np.random.normal(0, 0.1, 1)[0]
    oil_min = 0.2 + np.random.normal(0, 0.05, 1)[0]
    oil_max = 10 + np.random.normal(0, 0.8, 1)[0]
    oil_surface_chance = 0.2 + np.random.normal(0, 0.02, 1)[0]

    for buoy_id in range(NUM_BUOYS[idx]):
        pollution_df = pd.concat(
            (
                pollution_df,
                get_pollution_data(
                    field=field,
                    id=buoy_id,
                    size=SIZE,
                    depth_sin_var=depth_sin_var,
                    depth_mean=depth_mean,
                    depth_noise_var=depth_noise_var,
                    temp_log_mult=temp_log_mult,
                    temp_max=temp_max,
                    oil_spill_mean=oil_spill_mean,
                    oil_spill_var=oil_spill_var,
                    oil_min=oil_min,
                    oil_max=oil_max,
                    oil_surface_chance=oil_surface_chance,
                ),
            )
        )
pollution_df = pollution_df.reset_index()
pollution_df = pollution_df.drop("index", axis=1)

pollution_df.to_csv("data-processing/data/ID123.csv", index=False)
