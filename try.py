import netCDF4 as nc
import numpy as np
import pandas as pd

# 打開 NetCDF 檔案
file_path = 'GK2B_GOCI2_L2_20230814_001530_LA_Chl.nc'
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

# 匯出成 CSV 檔案
csv_file_path = 'output_filtered.csv'
df_filtered.to_csv(csv_file_path, index=False)

print(f"數據已匯出至 {csv_file_path}")
