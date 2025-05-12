# Import necessary modules
import arcpy  # ArcPy is used for geographic data analysis and management
import os     # os is used for file path operations
from arcpy import metadata as md  # Access metadata management functions from arcpy

# Set the workspace to the folder containing the data whose metadata will be reviewed/edited
arcpy.env.workspace = r"C:\2025GIS\MetaData\Index\MetaData_index\MetaData"
arcpy.env.overwriteOutput = True  # Allow overwriting of outputs if necessary

try:
    # List all files in the workspace
    # Note: ListFiles is used here; ListFeatureClasses() could be used if you only want feature classes
    datasets = arcpy.ListFiles("*") or []  # Returns an empty list if nothing is found

    # Notify if no datasets were found in the workspace
    if not datasets:
        print("No files found in the workspace.")

    # Iterate through each dataset/file found
    for dataset in datasets:
        # Create the full path to the dataset
        full_path = os.path.join(arcpy.env.workspace, dataset)

        # Access the metadata of the current dataset
        meta = md.Metadata(full_path)

        # Proceed only if the metadata is editable (not read-only)
        if not meta.isReadOnly:
            # Print key metadata properties for review
            print(f"Metadata for: {dataset}")
            print(f"Title: {meta.title}")
            print(f"Tags: {meta.tags}")
            print(f"Summary: {meta.summary}")
            print(f"Access Constraints: {meta.accessConstraints}")

            # Delete the geoprocessing history section from the metadata
            meta.deleteContent('GPHISTORY')
            print('GP HISTORY DELETED!')
            print("---")

except Exception as e:
    # Print any error that occurs during processing
    print(f"An error occurred: {e}")
