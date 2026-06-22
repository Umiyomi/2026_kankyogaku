import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path
from matplotlib.colors import Normalize
from matplotlib.colors import BoundaryNorm

PROJECT_ROOT = "/content/drive/MyDrive/kankyogaku2026"

OFFSHORE_DATA_DIR = f"{PROJECT_ROOT}/data/offshore"
MAGAKI_DATA_DIR = f"{PROJECT_ROOT}/data/AAQ2026/0621"
OUTPUT_DIR = f"{PROJECT_ROOT}/output"

ST1_LONGITUDE = 135 + 44.3886 / 60
ST2_LONGITUDE = 135 + 44.2118 / 60
ST3_LONGITUDE = 135 + 44.1365 / 60

# 若狭湾調査データ(2025年版)
DAY1_ST1_PATH = f"{OFFSHORE_DATA_DIR}/0610130624_AAQ177_SNo0636.csv"
DAY1_ST2_PATH = f"{OFFSHORE_DATA_DIR}/0610140740_AAQ177_SNo0636.csv"
DAY1_ST3_PATH = f"{OFFSHORE_DATA_DIR}/0610150715_AAQ177_SNo0636.csv"

DAY2A_ST1_PATH = f"{OFFSHORE_DATA_DIR}/0611132450_AAQ177_SNo0636.csv"
DAY2A_ST2_PATH = f"{OFFSHORE_DATA_DIR}/0611143259_AAQ177_SNo0636.csv"
DAY2A_ST3_PATH = f"{OFFSHORE_DATA_DIR}/0611153435_AAQ177_SNo0636.csv"

DAY2B_ST1_PATH = f"{OFFSHORE_DATA_DIR}/0611132815_AAQ177_SNo0636.csv"
DAY2B_ST2_PATH = f"{OFFSHORE_DATA_DIR}/0611143522_AAQ177_SNo0636.csv"
DAY2B_ST3_PATH = f"{OFFSHORE_DATA_DIR}/0611153710_AAQ177_SNo0636.csv"

# マガキ調査データ(2026年版)
MAGAKI_ST1_PATH = f"{MAGAKI_DATA_DIR}/0621090317_AAQ177_SNo0636.csv"
MAGAKI_ST2_PATH = f"{MAGAKI_DATA_DIR}/0621090953_AAQ177_SNo0636.csv"
MAGAKI_ST3_PATH = f"{MAGAKI_DATA_DIR}/0621092021_AAQ177_SNo0636.csv"
MAGAKI_ST4_PATH = f"{MAGAKI_DATA_DIR}/0621092708_AAQ177_SNo0636.csv"
MAGAKI_ST5_PATH = f"{MAGAKI_DATA_DIR}/0621094533_AAQ177_SNo0636.csv"
MAGAKI_ST6_PATH = f"{MAGAKI_DATA_DIR}/0621095111_AAQ177_SNo0636.csv"

DAY1_DATA_DICT = {
    "St1": (DAY1_ST1_PATH, ST1_LONGITUDE),
    "St2": (DAY1_ST2_PATH, ST2_LONGITUDE),
    "St3": (DAY1_ST3_PATH, ST3_LONGITUDE)
}

DAY2_DATA_DICT = {
    "St1": (DAY2A_ST1_PATH, ST1_LONGITUDE),
    "St2": (DAY2A_ST2_PATH, ST2_LONGITUDE),
    "St3": (DAY2A_ST3_PATH, ST3_LONGITUDE)
}

DAY2B_DATA_DICT = {
    "St1": (DAY2B_ST1_PATH, ST1_LONGITUDE),
    "St2": (DAY2B_ST2_PATH, ST2_LONGITUDE),
    "St3": (DAY2B_ST3_PATH, ST3_LONGITUDE)
}

MAGAKI_DATA_DICT = {
    "St1": (MAGAKI_ST1_PATH, 6),
    "St2": (MAGAKI_ST2_PATH, 5),
    "St3": (MAGAKI_ST3_PATH, 4),
    "St4": (MAGAKI_ST4_PATH, 3),
    "St5": (MAGAKI_ST5_PATH, 2),
    "St6": (MAGAKI_ST6_PATH, 1)
}

# ===== 演習設定（主にここを変更する） =====
ACTIVE_DATASET = "DAY1"      # "DAY1", "DAY2", "DAY2B", "MAGAKI" から選ぶ
USE_AUTO_LIMITS = True        # True: データの min/max を軸範囲に使う

DATASET_SETTINGS = {
    "DAY1": {
        "data_dict": DAY1_DATA_DICT,
        "output_csv": "concated_day1_contour_df.csv",
        "save_dir": OUTPUT_DIR + "/offshore_day1/contour",
        "depthmax": 6,
        "temp_vmin": 19,    "temp_vmax": 22,
        "sal_vmin": 32,     "sal_vmax": 35,
        "chl_vmin": 0.5,    "chl_vmax": 4.0,
        "temp_title": "temp-day1_contour",
        "sal_title": "sal-day1_contour",
        "chl_title": "chl-day1_contour",
        "temp_level_step": 0.2,
        "sal_level_step": 0.2,
        "chl_level_step": 0.2,
        "chl_fine_sub_step": 0.1,
        "chl_fine_coarse_step": 4.0,
        "chl_fine_levels": False,
    },
    "DAY2": {
        "data_dict": DAY2_DATA_DICT,
        "output_csv": "concated_day2_contour_df.csv",
        "save_dir": OUTPUT_DIR + "/offshore_day2/contour",
        "depthmax": 6,
        "temp_vmin": 19,    "temp_vmax": 22,
        "sal_vmin": 32,     "sal_vmax": 35,
        "chl_vmin": 0.5,    "chl_vmax": 4.0,
        "temp_title": "temp-day2_contour",
        "sal_title": "sal-day2_contour",
        "chl_title": "chl-day2_contour",
        "temp_level_step": 0.2,
        "sal_level_step": 0.2,
        "chl_level_step": 0.2,
        "chl_fine_sub_step": 0.1,
        "chl_fine_coarse_step": 4.0,
        "chl_fine_levels": False,
    },
    "DAY2B": {
        "data_dict": DAY2B_DATA_DICT,
        "output_csv": "concated_day2b_contour_df.csv",
        "save_dir": OUTPUT_DIR + "/offshore_day2b/contour",
        "depthmax": 6,
        "temp_vmin": 19,    "temp_vmax": 22,
        "sal_vmin": 32,     "sal_vmax": 35,
        "chl_vmin": 0.5,    "chl_vmax": 4.0,
        "temp_title": "temp-day2b_contour",
        "sal_title": "sal-day2b_contour",
        "chl_title": "chl-day2b_contour",
        "temp_level_step": 0.2,
        "sal_level_step": 0.2,
        "chl_level_step": 0.2,
        "chl_fine_sub_step": 0.1,
        "chl_fine_coarse_step": 4.0,
        "chl_fine_levels": False,
    },
    "MAGAKI": {
        "data_dict": MAGAKI_DATA_DICT,
        "output_csv": "concated_magaki_contour_df.csv",
        "save_dir": OUTPUT_DIR + "/magaki/contour",
        "depthmax": 6,
        "temp_vmin": 25.0,  "temp_vmax": 30.0,
        "sal_vmin": 30.5,   "sal_vmax": 34,
        "chl_vmin": 1.5,    "chl_vmax": 40,
        "temp_title": "temp-magaki_contour",
        "sal_title": "sal-magaki_contour",
        "chl_title": "chl-magaki_contour",
        "temp_level_step": 0.2,
        "sal_level_step": 0.2,
        "chl_level_step": 0.2,
        "chl_fine_sub_step": 0.1,
        "chl_fine_coarse_step": 4.0,
        "chl_fine_levels": False,
    },
}

def load_and_format_data(csv_file_path: str, station: str, longitude: float) -> pd.DataFrame:

    skiprows = None
    with open(csv_file_path, 'r', encoding='shift-jis') as f:
        for num, line in enumerate(f):
            if "[Item]" in line:
                skiprows = num

    if skiprows is None:
        raise ValueError(f"[Item] 行が見つかりません: {csv_file_path}")

    df = pd.read_csv(
        csv_file_path, skiprows=skiprows + 2, encoding="shift-jis",
        usecols=[0, 1, 2, 8, 9, 12], names=["depth(m)", "temp(℃)", "sal", "chl-a(μg/l)", "turb(FTU)", "DO(%)"],
        header=None
    )
    df["station"] = station
    df["longitude"] = longitude

    return df


def concat_station_data(data_dict: dict) -> pd.DataFrame:
    df_list = []
    for station, (station_path, station_longitude) in data_dict.items():
        dataframe = load_and_format_data(
            csv_file_path=station_path,
            station=station,
            longitude=station_longitude,
        )
        df_list.append(dataframe)
    return pd.concat(df_list, ignore_index=True)


def draw_contour_and_savefig(
    df: pd.DataFrame,
    x_col: str,
    y_col: str,
    value_col: str,
    title: str,
    label: str,
    save_dir: str,
    vmin: float,
    vmax: float,
    depthmax: float,
    cmap: str = "jet",
    level_step: float = 0.2,
    fine_sub_step: float = 0.1,
    fine_coarse_step: float = 4.0,
    fine_levels: bool = False,
) -> None:
    x = df[x_col].to_numpy()
    y = df[y_col].to_numpy() * -1
    z = df[value_col].to_numpy()

    if fine_levels:
        # 低濃度域は fine_sub_step 刻み、vmin 以降は fine_coarse_step 刻み
        levels_sub = np.arange(0, vmin, fine_sub_step)
        levels_coarse = np.arange(vmin, vmax + fine_coarse_step, fine_coarse_step)
        levels = np.concatenate([levels_sub, levels_coarse])
    else:
        levels = np.arange(vmin, vmax + level_step / 2, level_step)

    print(levels)

    x_unique = np.unique(x)
    y_unique = np.unique(y)

    X, Y = np.meshgrid(x_unique, y_unique)
    Z = np.full_like(X, np.nan, dtype=float)

    # 位置を一括でインデックスに変換
    ix = np.searchsorted(x_unique, x)
    iy = np.searchsorted(y_unique, y)

    # 一括で値を代入
    Z[iy, ix] = z

    # nanを0で置き換え
    Z = np.nan_to_num(Z, nan=0.0)

    # 描画
    fig, ax = plt.subplots(figsize=(8, 6))

    if fine_levels:
        cmap_obj = plt.colormaps[cmap].resampled(len(levels) - 1)
        norm = BoundaryNorm(boundaries=levels, ncolors=len(levels) - 1)
    else:
        cmap_obj = cmap
        norm = Normalize(vmin=vmin, vmax=vmax)

    contourf = ax.contourf(X, Y, Z, levels=levels, cmap=cmap_obj, norm=norm)
    contour = ax.contour(X, Y, Z, levels=levels, colors='black', linewidths=0.5)

    ax.clabel(contour, fmt='%2.1f', colors='black', fontsize=8)

    if fine_levels:
        fig.colorbar(contourf, ax=ax, ticks=levels, boundaries=levels)
    else:
        fig.colorbar(contourf, ax=ax, label=label)

    ax.set_title(title, fontsize=20)
    ax.set_xlabel('latitude')
    ax.set_ylabel('depth [m]')
    ax.set_ylim(depthmax * -1, 0.0)
    ax.set_xlim(x.min(), x.max())

    # 保存
    Path(save_dir).mkdir(parents=True, exist_ok=True)
    fig.savefig(Path(save_dir) / f"{title}.png", format="png")
    plt.close(fig)

    # plt.show()


def main_process():

    settings = DATASET_SETTINGS[ACTIVE_DATASET]
    concated_df = concat_station_data(data_dict=settings["data_dict"])
    Path(settings["save_dir"]).mkdir(parents=True, exist_ok=True)
    concated_df.to_csv(f"{settings['save_dir']}/{settings['output_csv']}")

    print(concated_df.min())
    print(concated_df.max())

    # 水温プロット
    if USE_AUTO_LIMITS:
        temp_vmin = concated_df["temp(℃)"].min()
        temp_vmax = concated_df["temp(℃)"].max()
    else:
        temp_vmin = settings["temp_vmin"]
        temp_vmax = settings["temp_vmax"]
    draw_contour_and_savefig(
        df=concated_df,
        x_col="longitude",
        y_col="depth(m)",
        value_col="temp(℃)",
        title=settings["temp_title"],
        label="℃",
        save_dir=settings["save_dir"],
        vmin=temp_vmin,
        vmax=temp_vmax,
        depthmax=settings["depthmax"],
        cmap="jet",
        level_step=settings["temp_level_step"],
        fine_levels=False,
    )

    # 塩分プロット
    if USE_AUTO_LIMITS:
        sal_vmin = concated_df["sal"].min()
        sal_vmax = concated_df["sal"].max()
    else:
        sal_vmin = settings["sal_vmin"]
        sal_vmax = settings["sal_vmax"]
    draw_contour_and_savefig(
        df=concated_df,
        x_col="longitude",
        y_col="depth(m)",
        value_col="sal",
        title=settings["sal_title"],
        label="salinity",
        save_dir=settings["save_dir"],
        vmin=sal_vmin,
        vmax=sal_vmax,
        depthmax=settings["depthmax"],
        cmap="jet",
        level_step=settings["sal_level_step"],
        fine_levels=False,
    )

    # クロロフィルプロット
    if USE_AUTO_LIMITS:
        chl_vmin = concated_df["chl-a(μg/l)"].min()
        chl_vmax = concated_df["chl-a(μg/l)"].max()
    else:
        chl_vmin = settings["chl_vmin"]
        chl_vmax = settings["chl_vmax"]
    draw_contour_and_savefig(
        df=concated_df,
        x_col="longitude",
        y_col="depth(m)",
        value_col="chl-a(μg/l)",
        title=settings["chl_title"],
        label="μg/l",
        save_dir=settings["save_dir"],
        vmin=chl_vmin,
        vmax=chl_vmax,
        depthmax=settings["depthmax"],
        cmap="jet",
        level_step=settings["chl_level_step"],
        fine_sub_step=settings["chl_fine_sub_step"],
        fine_coarse_step=settings["chl_fine_coarse_step"],
        fine_levels=settings["chl_fine_levels"],
    )


if __name__ == "__main__":
    # test()
    main_process()
