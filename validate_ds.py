import matplotlib.pyplot as plt
import xarray as xr
import numpy as np

lon = [[-99.83, -99.32], [-99.79, -99.23]]
lat = [[42.25, 42.21], [42.63, 42.59]]
# time_values = [
#     "2024-05-14T03:00:00.000000000",
#     "2024-05-14T04:00:00.000000000",
# ]
layer_name = "temperature"
# height_values = [20, 26, 12]
ensemble_values = [0, 1, 2]
dims = ["x", "y", "ensemble_member"]
values_hist = [[[1, np.nan, np.nan], [1, np.nan, np.nan]], [[1, np.nan, np.nan], [1, np.nan, np.nan]]]
values = [[[np.nan, 2, 3], [np.nan, 5, 6]], [[np.nan, 8, 9], [np.nan, 11, 12]]]
values_2 = [[[np.nan, 22, 23], [np.nan, 25, 26]], [[np.nan, 28, 29], [np.nan, 211, 212]]]
print(values)
ds = xr.Dataset(
    {
        layer_name: (
            dims,
            values,
        ),
        "pr": (
            dims,
            values_2,
        ),
    },
    coords={
        "lon": (["x", "y"], lon),
        "lat": (["x", "y"], lat),
        "ensemble_member": ensemble_values,
    },
)
ds_hist = xr.Dataset(
    {
        layer_name: (
            dims,
            values_hist,
        ),
        "pr": (
            dims,
            values_hist,
        ),
    },
    coords={
        "lon": (["x", "y"], lon),
        "lat": (["x", "y"], lat),
        "ensemble_member": ensemble_values,
    },
)
print(ds)
print(type(ds["temperature"].isel(ensemble_member=0).values))
print(type(ds["temperature"].isel(ensemble_member=0)))
print(type(ds.isel(ensemble_member=0)))
print(ds.isel(ensemble_member=0))
n_periods = len(ensemble_values)
change_ds_list = []

for period in range(1, n_periods):
    change_ds_list.append(
        xr.Dataset(ds.isel(ensemble_member=period) - ds_hist.isel(ensemble_member=0)).expand_dims("ensemble_member")
    )
    # change_ds_list[-1]["ensemble_member"]

print(change_ds_list)
change_ds = xr.concat(change_ds_list, "ensemble_member")
print(change_ds)
print(change_ds["temperature"].values)
print(change_ds["ensemble_member"].values)
print(change_ds["temperature"].isel(ensemble_member=0))
print(change_ds["temperature"].isel(ensemble_member=1))
print(change_ds["pr"].isel(ensemble_member=0))
print(change_ds["pr"].isel(ensemble_member=1))
