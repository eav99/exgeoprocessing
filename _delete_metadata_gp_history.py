import arcpy
import os
from arcpy import metadata as md

arcpy.env.workspace = r"C:\2025GIS\MetaData\Index\MetaData_index\MetaData"
arcpy.env.overwriteOutput = True

#full_path =  r"C:\2025GIS\MetaData\Index\MetaData_index\MetaData"
try:
    # List all feature classes or items in the workspace
    datasets = arcpy.ListFiles("*") or []  # You can use ListFeatureClasses() if you expect feature classes
    if not datasets:
        print("No files found in the workspace.")

    for dataset in datasets:
        full_path = os.path.join(arcpy.env.workspace, dataset)
        meta = md.Metadata(full_path)
        if not meta.isReadOnly:
           
            print(f"Metadata for: {dataset}")
            print(f"Title: {meta.title}")
            print(f"Tags: {meta.tags}")
            print(f"Summary: {meta.summary}")
            print(f"Access Constraints: {meta.accessConstraints}")
            meta.deleteContent('GPHISTORY')
            print('GP HISTORY DELETED!')
            print("---")
            

except Exception as e:
    print(f"An error occurred: {e}")
