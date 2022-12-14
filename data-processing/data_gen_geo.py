import pandas as pd
import numpy as np


def get_geo_data(
    field: str,
    id: int,
    size=1000,
    lat_center: int = 59,
    lon_center: int = 2,
):
    """Generate geo_data for one sensor"""
    df = pd.DataFrame()

    time = np.arange(0, size)
    df["time"] = time

    field_col = np.array([field] * size)
    df["field"] = field_col

    id_col = np.ones(size) * id
    df["id"] = id_col

    lat_col = np.random.normal(lat_center, 0.001, size)
    df["lat"] = lat_col

    lon_col = np.random.normal(lon_center, 0.001, size)
    df["lon"] = lon_col

    return df


OIL_FIELDS = np.array(["Frigg", "Magnus", "Troll", "Gullfaks", "Viking", "Snorre"])
SIZE = 200
NUM_BUOYS = [5, 3, 7, 5, 4, 4]

geo_data = pd.DataFrame()
for idx, field in enumerate(OIL_FIELDS):
    lat_cen = 59 + np.random.normal(0, 0.1, 1)[0]
    lon_cen = 2 + np.random.normal(0, 0.1, 1)[0]
    for buoy_id in range(NUM_BUOYS[idx]):
        geo_data = pd.concat(
            (
                geo_data,
                get_geo_data(
                    field=field,
                    id=buoy_id,
                    size=SIZE,
                    lat_center=lat_cen + np.random.normal(0, 0.01, 1)[0],
                    lon_center=lon_cen + np.random.normal(0, 0.01, 1)[0],
                ),
            )
        )
geo_data = geo_data.reset_index(drop=True)
geo_data.to_csv("data-processing/data/geo_data.csv", index=False)
