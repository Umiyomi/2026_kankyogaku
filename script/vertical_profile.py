import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path
from matplotlib.colors import Normalize
from matplotlib.colors import BoundaryNorm

PROJECT_ROOT = "/content/drive/MyDrive/kankyogaku2026"

WAKASA_DATA_DIR = f"{PROJECT_ROOT}/data/wakasa"
MAGAKI_DATA_DIR = f"{PROJECT_ROOT}/data/magaki"
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
    "St1": (WAKASA_0624_ST1_PATH, ST1_LATITUDE),
    "St2": (WAKASA_0624_ST2_PATH, ST2_LATITUDE),
    "St3": (WAKASA_0624_ST3_PATH, ST3_LATITUDE),
    "St4": (WAKASA_0624_ST4_PATH, ST4_LATITUDE)
}

MAGAKI_0621_DATA_DICT = {
    "St1": (MAGAKI_0621_ST1_PATH, 6),
    "St2": (MAGAKI_0621_ST2_PATH, 5),
    "St3": (MAGAKI_0621_ST3_PATH, 4),
    "St4": (MAGAKI_0621_ST4_PATH, 3),
    "St5": (MAGAKI_0621_ST5_PATH, 2),
    "St6": (MAGAKI_0621_ST6_PATH, 1)
}

MAGAKI_0627_DATA_DICT = {
    "St1": (MAGAKI_0627_ST1_PATH, 6),
    "St2": (MAGAKI_0627_ST2_PATH, 5),
    "St3": (MAGAKI_0627_ST3_PATH, 4),
    "St4": (MAGAKI_0627_ST4_PATH, 3),
    "St5": (MAGAKI_0627_ST5_PATH, 2),
    "St6": (MAGAKI_0627_ST6_PATH, 1)
}

# ===== 演習設定（主にここを変更する） =====
ACTIVE_DATASET = "WAKASA_0624"      # "WAKASA_0624", "MAGAKI_0621", "MAGAKI_0627" から選ぶ
USE_AUTO_LIMITS = False        # True: データの min/max を軸範囲に使う

DATASET_SETTINGS = {
    "WAKASA_0624": {
        "data_dict": WAKASA_0624_DATA_DICT,
        "output_csv": "concated_wakasa_0624_profile_df.csv",
        "save_dir": OUTPUT_DIR + "/wakasa/contour",
        "depthmax": 30,
        "temp_vmin": 21.0,  "temp_vmax": 25.0,
        "sal_vmin": 29.5,   "sal_vmax": 34.3,
        "chl_vmin": 0,      "chl_vmax": 10.0,
        "temp_title": "temp-wakasa_0624_profile",
        "sal_title": "sal-wakasa_0624_profile",
        "chl_title": "chl-wakasa_0624_profile",
        "temp_level_step": 0.2,
        "sal_level_step": 0.2,
        "chl_level_step": 0.2,
        "chl_fine_sub_step": 0.1,
        "chl_fine_coarse_step": 4.0,
        "chl_fine_levels": False,
    },
    "MAGAKI_0621": {
        "data_dict": MAGAKI_0621_DATA_DICT,
        "output_csv": "concated_magaki_0621_profile_df.csv",
        "save_dir": OUTPUT_DIR + "/magaki/contour",
        "depthmax": 30,
        "temp_vmin": 21.0,  "temp_vmax": 25.0,
        "sal_vmin": 29.5,   "sal_vmax": 34.3,
        "chl_vmin": 0,      "chl_vmax": 10.0,
        "temp_title": "temp-magaki_0621_profile",
        "sal_title": "sal-magaki_0621_profile",
        "chl_title": "chl-magaki_0621_profile",
        "temp_level_step": 0.2,
        "sal_level_step": 0.2,
        "chl_level_step": 0.2,
        "chl_fine_sub_step": 0.1,
        "chl_fine_coarse_step": 4.0,
        "chl_fine_levels": False,
    },
    "MAGAKI_0627": {
        "data_dict": MAGAKI_0627_DATA_DICT,
        "output_csv": "concated_magaki_0627_profile_df.csv",
        "save_dir": OUTPUT_DIR + "/magaki/contour",
        "depthmax": 30,
        "temp_vmin": 21.0,  "temp_vmax": 25.0,
        "sal_vmin": 29.5,   "sal_vmax": 34.3,
        "chl_vmin": 0,      "chl_vmax": 10.0,
        "temp_title": "temp-magaki_0627_profile",
        "sal_title": "sal-magaki_0627_profile",
        "chl_title": "chl-magaki_0627_profile",
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
        usecols=[0, 1, 2, 8], names=["depth(m)", "temp(℃)", "sal", "chl-a(μg/l)"],
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


def draw_profile_and_savefig(df: pd.DataFrame, x_col: str, y_col: str, title: str, xlabel: str, ylabel: str, vmin: float, vmax: float, depthmax: float, save_dir: str) -> None:

    c_dict = {
        "St1": "r",
        "St2": "b",
        "St3": "g",
        "St4": "c",
        "St5": "m",
        "St6": "y"
    }

    plt.figure(figsize=(10, 6))

    for i, (station, station_df) in enumerate(df.groupby("station")):
        plt.scatter(station_df[x_col], station_df[y_col] * -1, label=station, color=c_dict.get(station, "k"), alpha=0.6)

    plt.title(title, fontsize=20)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.xlim(vmin, vmax)
    plt.ylim(depthmax * -1, 0.5)

    # 保存
    Path(save_dir).mkdir(parents=True, exist_ok=True)
    plt.savefig(Path(save_dir) / f"{title}.png", format="png")
    plt.close()

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
    draw_profile_and_savefig(
        df=concated_df,
        x_col="temp(℃)",
        y_col="depth(m)",
        title=settings["temp_title"],
        xlabel="℃",
        ylabel="m",
        vmin=temp_vmin,
        vmax=temp_vmax,
        depthmax=settings["depthmax"],
        save_dir=settings["save_dir"],
    )

    # 塩分プロット
    if USE_AUTO_LIMITS:
        sal_vmin = concated_df["sal"].min()
        sal_vmax = concated_df["sal"].max()
    else:
        sal_vmin = settings["sal_vmin"]
        sal_vmax = settings["sal_vmax"]
    draw_profile_and_savefig(
        df=concated_df,
        x_col="sal",
        y_col="depth(m)",
        title=settings["sal_title"],
        xlabel="salinity",
        ylabel="m",
        vmin=sal_vmin,
        vmax=sal_vmax,
        depthmax=settings["depthmax"],
        save_dir=settings["save_dir"],
    )

    # クロロフィルプロット
    if USE_AUTO_LIMITS:
        chl_vmin = concated_df["chl-a(μg/l)"].min()
        chl_vmax = concated_df["chl-a(μg/l)"].max()
    else:
        chl_vmin = settings["chl_vmin"]
        chl_vmax = settings["chl_vmax"]
    draw_profile_and_savefig(
        df=concated_df,
        x_col="chl-a(μg/l)",
        y_col="depth(m)",
        title=settings["chl_title"],
        xlabel="μg/l",
        ylabel="m",
        vmin=chl_vmin,
        vmax=chl_vmax,
        depthmax=settings["depthmax"],
        save_dir=settings["save_dir"],
    )


if __name__ == "__main__":
    # test()
    main_process()
