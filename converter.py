import netCDF4 as nc
import os

def print_nc_file_details(nc_file):
    try:
        ds = nc.Dataset(nc_file)
        
        print(f"Details of {nc_file}:")
        print("Global Attributes:")
        for attr in ds.ncattrs():
            print(f"  {attr}: {ds.getncattr(attr)}")
        
        print("Dimensions:")
        for dim in ds.dimensions.values():
            print(f"  {dim.name}: {dim.size}")
        
        print("Variables:")
        for var_name, var in ds.variables.items():
            print(f"  {var_name} ({var.dimensions}): {var.shape}")
            print(f"    Attributes:")
            for attr in var.ncattrs():
                print(f"      {attr}: {var.getncattr(attr)}")
        
        ds.close()
    except Exception as e:
        print(f"Failed to read details of {nc_file} due to {str(e)}")

def batch_print_nc_details(nc_folder):
    for file_name in os.listdir(nc_folder):
        if file_name.endswith('.nc'):
            nc_file = os.path.join(nc_folder, file_name)
            print_nc_file_details(nc_file)

# 使用示例
nc_folder = 'C:/Users/DIC/Desktop/20240517_GOCI2_test'  # .nc文件所在目录
batch_print_nc_details(nc_folder)
