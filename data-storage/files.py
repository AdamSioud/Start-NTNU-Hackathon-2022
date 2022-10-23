try:
    from google.cloud import storage
    import google.cloud.storage
    import json
    import os
    import sys
except Exception as e:
    print("Error : {} ".format(e))

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\asiou\OneDrive\Desktop\Start-NTNU-Hackathon-2022\data-storage\jofeadar-4b2832e0d055.json"
storage_client = storage.Client()


bucket = storage_client.get_bucket('jofeadar_bucket')

# Getting all Files from GCP Bucket


filename = [filename.name for filename in list(bucket.list_blobs(prefix='')) ]
print(filename)


# Downloading a File from Bucket

first_file = bucket.blob(blob_name = 'ekkolodd.txt').download_as_string()

with open ('ekkolodd.csv', "wb") as f:
        f.write(first_file)


# Pushing a file on GCP bucket

filename= 'new.csv'
UPLOADFILE = os.path.join(os.getcwd(), filename)

bucket = storage_client.get_bucket("jofeadar_bucket")
blob = bucket.blob(filename)
blob.upload_from_filename(UPLOADFILE)
