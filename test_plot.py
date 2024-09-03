import matplotlib.pyplot as plt
import xarray as xr
from pathlib import Path

# files = ["/lustre/storeC-ext/users/klimakverna/development/Klimakverna-pilot-KAPy/KAPy/results/4.ensstats/time_binning_periods/hadgem/102_CMIP5_rcp26_ensstats.nc", "/lustre/storeC-ext/users/klimakverna/development/Klimakverna-pilot-KAPy/KAPy/results/4.ensstats/time_binning_periods/hadgem/102_CMIP5_rcp45_ensstats.nc"]
indicator = "102"
model = "hadgem"
scenario = ["rcp26", "rcp45"]
path_to_netcdfs = Path("testcase_1_results")
files = [
    f"{path_to_netcdfs}/{indicator}_{scenario[0]}_change_periods.nc",
    f"{path_to_netcdfs}/{indicator}_{scenario[1]}_change_periods.nc",
]

for filename in files:
    ds = xr.open_dataset(filename)
    print(ds)
    for period in [0, 1]:
        plt.figure()
        ds["indicator_mean"].isel(periodID=period).plot()
        plt.savefig(f"{path_to_netcdfs}/{indicator}_{scenario[period]}_indicator_mean_{model}_period_{period}")

plt.show()
