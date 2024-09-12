import matplotlib.pyplot as plt
import xarray as xr
from pathlib import Path

indicator = "102"
model = "cnrm_aladin"
scenario = ["rcp26", "rcp45"]
# scenario = ["ssp370"]
path_to_netcdfs = Path(
    f"/lustre/storeC-ext/users/klimakverna/development/Klimakverna-pilot-KAPy/KAPy/results/7.netcdf/{model}"
)
path_to_save_figures = Path(
    f"/lustre/storeC-ext/users/klimakverna/development/Klimakverna-pilot-KAPy/testcase_1_results/{model}"
)
files = [
    # "/lustre/storeC-ext/users/kin2100/MET/annmeans_bc/far_future_mean/pr/30yrmean_ff_ecearth-r12i1p1-cclm_rcp26_3dbc-eqm-sn2018v2005_rawbc_norway_1km_pr_annual_merged.nc"
    f"{path_to_netcdfs}/{indicator}_{scenario[0]}_change_periods.nc",
    f"{path_to_netcdfs}/{indicator}_{scenario[1]}_change_periods.nc",
]

cmap = plt.cm.PuOr
alpha = 0.8
# fig = plt.figure()
# ds = xr.open_dataset(files[0])
# print(ds)
# ds["pr"].isel(time=0).plot(robust=True, vmin=-1e-5, vmax=1e-5, cmap=cmap, alpha=alpha)
# plt.savefig(f"{path_to_save_figures}/{indicator}_{scenario[0]}_pr_{model}")

for sceanrio_idx, filename in enumerate(files):
    ds = xr.open_dataset(filename)
    print(ds)
    for period in [0, 1]:
        plt.figure()
        ds["indicator_mean"].isel(periodID=period).plot(robust=True, vmin=-1e-5, vmax=1e-5, cmap=cmap, alpha=alpha)
        plt.savefig(
            f"{path_to_save_figures}/{indicator}_{scenario[sceanrio_idx]}_indicator_mean_{model}_period_{period}"
        )

        fig = plt.figure()
        ds["indicator_mean_rel"].isel(periodID=period).plot(robust=True, vmin=-20, vmax=20, cmap=cmap, alpha=alpha)
        plt.savefig(
            f"{path_to_save_figures}/{indicator}_{scenario[sceanrio_idx]}_indicator_mean_rel_{model}_period_{period}"
        )

plt.show()
