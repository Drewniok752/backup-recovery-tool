import os
import boto3
import datetime

# AWS S3 setup
s3 = boto3.client('s3')
bucket_name = 'your-bucket-name'

# Backup local files to S3
def backup_to_s3(file_path):
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    s3_file_path = f"backup/{current_date}/{os.path.basename(file_path)}"
    s3.upload_file(file_path, bucket_name, s3_file_path)
    print(f"Uploaded {file_path} to S3 bucket {bucket_name} at {s3_file_path}")

# Example usage
file_to_backup = 'path/to/your/file.txt'
backup_to_s3(file_to_backup)
