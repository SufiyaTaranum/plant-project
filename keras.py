import kaggle as kg
import boto3
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv(verbose=True, dotenv_path='./src/.env')

print('Pulling data from Kaggle')

# Checking authentication
try:
    kg.api.authenticate()
    print("Authentication to Kaggle successful!")
except Exception as e:
    print(f"Authentication failed! Error: {e}")

# Attempting download
try:
    file_path = './data_raw/'
    kg.api.dataset_download_files(dataset="vipoooool/new-plant-diseases-dataset",
                                  path=file_path,
                                  unzip=True)
    print(f"File download successful! Data is in {file_path}")
except Exception as e:
    print(f"Download failed! Error: {e}")

# Define file paths
train_tfrecord_file = f'{file_path}leaves.tfrecord'
val_tfrecord_file = f'{file_path}test_leaves.tfrecord'
# Print file paths
print(f"Train TFRecord file: {train_tfrecord_file}")
print(f"Validation TFRecord file: {val_tfrecord_file}")






