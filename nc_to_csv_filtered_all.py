import netCDF4 as nc
import numpy as np
import pandas as pd
import os

# 讀取並處理單個 NetCDF 檔案的函數
def process_nc_file(file_path):
    # 打開 NetCDF 檔案
    dataset = nc.Dataset(file_path)

    # 讀取 geophysical_data 群組中的變數
    geophysical_data = dataset.groups['geophysical_data']
    Chl = geophysical_data.variables['Chl'][:]
    flag = geophysical_data.variables['flag'][:]

    # 讀取 navigation_data 群組中的變數
    navigation_data = dataset.groups['navigation_data']
    latitude = navigation_data.variables['latitude'][:]
    longitude = navigation_data.variables['longitude'][:]

    # 轉換成一維數組
    latitude_flat = latitude.flatten()
    longitude_flat = longitude.flatten()
    Chl_flat = Chl.flatten()
    flag_flat = flag.flatten()

    # 創建 DataFrame
    data = {
        'Latitude': latitude_flat,
        'Longitude': longitude_flat,
        'Chlorophyll': Chl_flat,
        'Flag': flag_flat
    }
    df = pd.DataFrame(data)

    # 只保留有葉綠素值的行
    df_filtered = df[df['Chlorophyll'].notnull()]

    # 取得原始檔案的目錄和檔名
    dir_name, base_name = os.path.split(file_path)
    # 創建 output 資料夾
    output_dir = os.path.join(dir_name, 'output')
    os.makedirs(output_dir, exist_ok=True)
    # 設定 CSV 檔案的路徑和檔名
    csv_file_path = os.path.join(output_dir, f'{os.path.splitext(base_name)[0]}.csv')

    # 匯出成 CSV 檔案
    df_filtered.to_csv(csv_file_path, index=False)

    print(f"數據已匯出至 {csv_file_path}")

# 指定資料夾路徑
folder_path = r"C:\Users\DIC\Desktop\20240517_GOCI2_test"

# 遍歷資料夾內的所有 .nc 檔案
for file_name in os.listdir(folder_path):
    if file_name.endswith('.nc'):
        file_path = os.path.join(folder_path, file_name)
        process_nc_file(file_path)
