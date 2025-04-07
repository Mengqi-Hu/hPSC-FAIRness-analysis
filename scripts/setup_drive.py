
# setup_drive.py

import pandas as pd
import re
import os
from google.colab import drive

def setup_drive(root_dir_name='hPSC-FAIRness Analysis'):
    # Mount Google Drive
    drive.mount('/content/drive', force_remount=True)

    # Print the root_dir_name to confirm it’s being set correctly
    print(f"Setting up root directory with name: '{root_dir_name}'")


    # Define the root directory path
    root_dir = f'/content/drive/My Drive/{root_dir_name}'
    print(f"Root directory path: '{root_dir}'")

    # Define subdirectories for your project
    data_dir = os.path.join(root_dir, 'data')
    processed_dir = os.path.join(data_dir, 'processed')
    results_dir = os.path.join(root_dir, 'results')

    # Create subdirectories if they don't exist
    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(processed_dir, exist_ok=True)
    os.makedirs(results_dir, exist_ok=True)

    return root_dir, data_dir, processed_dir, results_dir
