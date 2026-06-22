import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path

OFFSHORE_DATA_DIR = "/Users/umiyomi/Desktop/CodeWorks/Projects/2025kankyogakuTA/data/drive-download-20250701T092229Z-1-001"
MAGAKI_DATA_DIR = "/Users/umiyomi/Desktop/CodeWorks/Projects/2026kankyogakuTA/data/AAQ2026/0621"
OUTPUT_DIR = "/Users/umiyomi/Desktop/CodeWorks/Projects/2026kankyogakuTA/output/"

ST1_LONGITUDE = 135 + 44.3886 / 60
ST2_LONGITUDE = 135 + 44.2118 / 60
ST3_LONGITUDE = 135 + 44.1365 / 60

DAY1_ST1_PATH = f"{OFFSHORE_DATA_DIR}/0610130624_AAQ177_SNo0636.csv" 
DAY1_ST2_PATH = f"{OFFSHORE_DATA_DIR}/0610140740_AAQ177_SNo0636.csv"
DAY1_ST3_PATH = f"{OFFSHORE_DATA_DIR}/0610150715_AAQ177_SNo0636.csv"

DAY2A_ST1_PATH = f"{OFFSHORE_DATA_DIR}/0611132450_AAQ177_SNo0636.csv"
DAY2A_ST2_PATH = f"{OFFSHORE_DATA_DIR}/0611143259_AAQ177_SNo0636.csv"
DAY2A_ST3_PATH = f"{OFFSHORE_DATA_DIR}/0611153435_AAQ177_SNo0636.csv"

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

MAGAKI_DATA_DICT = {
    "St1": (MAGAKI_ST1_PATH, 1),
    "St2": (MAGAKI_ST2_PATH, 2),
    "St3": (MAGAKI_ST3_PATH, 3),
    "St4": (MAGAKI_ST4_PATH, 4),
    "St5": (MAGAKI_ST5_PATH, 5),
    "St6": (MAGAKI_ST6_PATH, 6)
}

# ===== 演習設定（主にここを変更する） =====
ACTIVE_DATASET = "MAGAKI"       # "DAY1", "DAY2", "MAGAKI" から選ぶ
USE_AUTO_LIMITS = True       # True: データの min/max を軸範囲に使う

DATASET_SETTINGS = {
    "DAY1": {
        "data_dict": DAY1_DATA_DICT,
        "output_csv": "concated_day1_df.csv",
        "save_dir": OUTPUT_DIR + "/offshore_day1/profile",
        "depthmax": 6,
        "temp_vmin": 19,    "temp_vmax": 22,
        "sal_vmin": 32,     "sal_vmax": 35,
        "chl_vmin": 0.5,    "chl_vmax": 4.0,
        "temp_title": "temp-day1_profile",
        "sal_title": "sal-day1_profile",
        "chl_title": "chl-day1_profile",
    },
    "DAY2": {
        "data_dict": DAY2_DATA_DICT,
        "output_csv": "concated_day2_df.csv",
        "save_dir": OUTPUT_DIR + "/offshore_day2/profile",
        "depthmax": 6,
        "temp_vmin": 19,    "temp_vmax": 22,
        "sal_vmin": 32,     "sal_vmax": 35,
        "chl_vmin": 0.5,    "chl_vmax": 4.0,
        "temp_title": "temp-day2_profile",
        "sal_title": "sal-day2_profile",
        "chl_title": "chl-day2_profile",
    },
    "MAGAKI": {
        "data_dict": MAGAKI_DATA_DICT,
        "output_csv": "concated_magaki_df.csv",
        "save_dir": OUTPUT_DIR + "/magaki/profile",
        "depthmax": 6,
        "temp_vmin": 25.0,  "temp_vmax": 30.0,
        "sal_vmin": 30.5,   "sal_vmax": 34,
        "chl_vmin": 0,      "chl_vmax": 46.0,
        "temp_title": "temp-magaki_profile",
        "sal_title": "sal-magaki_profile",
        "chl_title": "chl-magaki_profile",
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
