import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path
from matplotlib.colors import Normalize
from matplotlib.colors import BoundaryNorm

PROJECT_ROOT = "/Users/umiyomi/Desktop/CodeWorks/Projects/2026kankyogakuTA"

DATA_DIR = f"{PROJECT_ROOT}/haihuyou/kankyogaku2026/data"
WAKASA_DATA_DIR = f"{DATA_DIR}/wakasa"
MAGAKI_DATA_DIR = f"{DATA_DIR}/magaki"
OUTPUT_DIR = f"{PROJECT_ROOT}/output"

# 20260624
ST1_LATITUDE = 35 + 30.496 / 60
ST2_LATITUDE = 35 + 31.161 / 60
ST3_LATITUDE = 35 + 31.848 / 60
ST4_LATITUDE = 35 + 32.535 / 60

# wakasa20260624調査データ
WAKASA_0624_ST1_PATH = f"{WAKASA_DATA_DIR}/20260624/202606241429_ASTD152-ALC-R02_0184_142943.Csv"
WAKASA_0624_ST2_PATH = f"{WAKASA_DATA_DIR}/20260624/202606241417_ASTD152-ALC-R02_0184_141756.Csv"
WAKASA_0624_ST3_PATH = f"{WAKASA_DATA_DIR}/20260624/202606241356_ASTD152-ALC-R02_0184_135631.Csv"
WAKASA_0624_ST4_PATH = f"{WAKASA_DATA_DIR}/20260624/202606241340_ASTD152-ALC-R02_0184_134017.Csv"

# magaki20260621調査データ
MAGAKI_0621_ST1_PATH = f"{MAGAKI_DATA_DIR}/20260621/0621090317_AAQ177_SNo0636.csv"
MAGAKI_0621_ST2_PATH = f"{MAGAKI_DATA_DIR}/20260621/0621090953_AAQ177_SNo0636.csv"
MAGAKI_0621_ST3_PATH = f"{MAGAKI_DATA_DIR}/20260621/0621092021_AAQ177_SNo0636.csv"
MAGAKI_0621_ST4_PATH = f"{MAGAKI_DATA_DIR}/20260621/0621092708_AAQ177_SNo0636.csv"
MAGAKI_0621_ST5_PATH = f"{MAGAKI_DATA_DIR}/20260621/0621094533_AAQ177_SNo0636.csv"
MAGAKI_0621_ST6_PATH = f"{MAGAKI_DATA_DIR}/20260621/0621095111_AAQ177_SNo0636.csv"

# magaki20260627調査データ
MAGAKI_0627_ST1_PATH = f"{MAGAKI_DATA_DIR}/20260627/0627085508_AAQ177_SNo0636.csv"
MAGAKI_0627_ST2_PATH = f"{MAGAKI_DATA_DIR}/20260627/0627090223_AAQ177_SNo0636.csv"
MAGAKI_0627_ST3_PATH = f"{MAGAKI_DATA_DIR}/20260627/0627091435_AAQ177_SNo0636.csv"
MAGAKI_0627_ST4_PATH = f"{MAGAKI_DATA_DIR}/20260627/0627092047_AAQ177_SNo0636.csv"
MAGAKI_0627_ST5_PATH = f"{MAGAKI_DATA_DIR}/20260627/0627093537_AAQ177_SNo0636.csv"
MAGAKI_0627_ST6_PATH = f"{MAGAKI_DATA_DIR}/20260627/0627094142_AAQ177_SNo0636.csv"

WAKASA_0624_DATA_DICT = {
    "St1": (WAKASA_0624_ST1_PATH, 1),
    "St2": (WAKASA_0624_ST2_PATH, 2),
    "St3": (WAKASA_0624_ST3_PATH, 3),
    "St4": (WAKASA_0624_ST4_PATH, 4)
}

MAGAKI_0621_DATA_DICT = {
    "St1": (MAGAKI_0621_ST1_PATH, 1),
    "St2": (MAGAKI_0621_ST2_PATH, 2),
    "St3": (MAGAKI_0621_ST3_PATH, 3),
    "St4": (MAGAKI_0621_ST4_PATH, 4),
    "St5": (MAGAKI_0621_ST5_PATH, 5),
    "St6": (MAGAKI_0621_ST6_PATH, 6)
}

MAGAKI_0627_DATA_DICT = {
    "St1": (MAGAKI_0627_ST1_PATH, 1),
    "St2": (MAGAKI_0627_ST2_PATH, 2),
    "St3": (MAGAKI_0627_ST3_PATH, 3),
    "St4": (MAGAKI_0627_ST4_PATH, 4),
    "St5": (MAGAKI_0627_ST5_PATH, 5),
    "St6": (MAGAKI_0627_ST6_PATH, 6)
}

# ===== 演習設定（主にここを変更する） =====
ACTIVE_DATASET = "WAKASA_0624"      # "WAKASA_0624", "MAGAKI_0621", "MAGAKI_0627" から選ぶ
USE_AUTO_LIMITS = False        # True: データの min/max を軸範囲に使う

DATASET_SETTINGS = {
    "WAKASA_0624": {
        "data_dict": WAKASA_0624_DATA_DICT,
        "output_csv": "concated_wakasa_0624_contour_df.csv",
        "save_dir": OUTPUT_DIR + "/wakasa/contour",
        "depthmax": 30,
        "temp_vmin": 21.0,  "temp_vmax": 25.0,
        "sal_vmin": 29.5,   "sal_vmax": 34.3,
        "chl_vmin": 0,      "chl_vmax": 10.0,
        "temp_title": "temp-wakasa_0624_contour",
        "sal_title": "sal-wakasa_0624_contour",
        "chl_title": "chl-wakasa_0624_contour",
        "temp_level_step": 0.2,
        "sal_level_step": 0.2,
        "chl_level_step": 0.2,
        "chl_fine_sub_step": 0.1,
        "chl_fine_coarse_step": 4.0,
        "chl_fine_levels": False,
    },
    "MAGAKI_0621": {
        "data_dict": MAGAKI_0621_DATA_DICT,
        "output_csv": "concated_magaki_0621_contour_df.csv",
        "save_dir": OUTPUT_DIR + "/magaki/contour",
        "depthmax": 30,
        "temp_vmin": 21.0,  "temp_vmax": 25.0,
        "sal_vmin": 29.5,   "sal_vmax": 34.3,
        "chl_vmin": 0,      "chl_vmax": 10.0,
        "temp_title": "temp-magaki_0621_contour",
        "sal_title": "sal-magaki_0621_contour",
        "chl_title": "chl-magaki_0621_contour",
        "temp_level_step": 0.2,
        "sal_level_step": 0.2,
        "chl_level_step": 0.2,
        "chl_fine_sub_step": 0.1,
        "chl_fine_coarse_step": 4.0,
        "chl_fine_levels": False,
    },
    "MAGAKI_0627": {
        "data_dict": MAGAKI_0627_DATA_DICT,
        "output_csv": "concated_magaki_0627_contour_df.csv",
        "save_dir": OUTPUT_DIR + "/magaki/contour",
        "depthmax": 30,
        "temp_vmin": 21.0,  "temp_vmax": 25.0,
        "sal_vmin": 29.5,   "sal_vmax": 34.3,
        "chl_vmin": 0,      "chl_vmax": 10.0,
        "temp_title": "temp-magaki_0627_contour",
        "sal_title": "sal-magaki_0627_contour",
        "chl_title": "chl-magaki_0627_contour",
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
    ax.set_xlabel('station')
    ax.set_ylabel('depth [m]')
    ax.set_ylim(depthmax * -1, 0.0)
    # x軸はstationの番号で、整数刻み
    ax.set_xticks(np.arange(1, len(np.unique(x)) + 1))
    ax.set_xticklabels(np.arange(1, len(np.unique(x)) + 1))

    # 保存
    Path(save_dir).mkdir(parents=True, exist_ok=True)
    fig.savefig(Path(save_dir) / f"{title}.png", format="png")
    plt.close(fig)

    # plt.show()


def main_process(settings: dict):

    concated_df = concat_station_data(data_dict=settings["data_dict"])

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


def pipeline():
    
    RUNS = [
        {
            "dataset": ["WAKASA_0624", "MAGAKI_0621", "MAGAKI_0627"],
            "settings_overrides": {
                "depthmax": 30,
                "run_suffix": "30m",
                "chl_vmin": 0.1,
                "chl_vmax": 5.0,
            }
        },
        {
            "dataset": ["MAGAKI_0621", "MAGAKI_0627"],
            "settings_overrides": {
                "depthmax": 6,
                "run_suffix": "6m",
                "chl_vmin": 0.1,
                "chl_vmax": 5.0,
            }
        }
    ]
    
    for run in RUNS:
        for dataset in run["dataset"]:
            settings = DATASET_SETTINGS[dataset].copy()
            settings.update(run["settings_overrides"])
            settings["save_dir"] = f"{settings['save_dir']}/{settings['run_suffix']}"
            Path(settings["save_dir"]).mkdir(parents=True, exist_ok=True)
            settings["output_csv"] = f"{settings['output_csv']}_{settings['run_suffix']}"
            settings["temp_title"] = f"{settings['temp_title']}_{settings['run_suffix']}"
            settings["sal_title"] = f"{settings['sal_title']}_{settings['run_suffix']}"
            settings["chl_title"] = f"{settings['chl_title']}_{settings['run_suffix']}"
            main_process(settings)

if __name__ == "__main__":
    # test()
    pipeline()
