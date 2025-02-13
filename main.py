from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os
from step import get_blob_client_by_name, updoad_blob, download_blob, list_blobs

# Load variables from .env file
load_dotenv()


if __name__ == "__main__":

    container_name = "containertestx"

    # Paths for your test file to upload and download
    local_file_path_to_upload = os.path.join(
        "data", "file_to_upload.txt")  # Path to the file to upload
    local_file_path_to_download = os.path.join(
        "data", "downloaded_file.txt")  # Path to save the downloaded file
    blob_name = "uploadedblob.txt"

    # Get the Azure Storage connection string
    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    if not connection_string:
        raise ValueError(
            "AZURE_STORAGE_CONNECTION_STRING is not set in .env file")
    blob_client = get_blob_client_by_name(
        connection_string, container_name, blob_name)

    # # Ensure the connection string and container name are set before running operations
    if blob_client:
        # Test upload_blob function
        # updoad_blob(blob_name, local_file_path_to_upload, blob_client)

        # Test download_blob function
        # download_blob(blob_name, local_file_path_to_download, blob_client)

        # Test list_blobs function
        list_blobs(connection_string, container_name, blob_client)
    else:
        print("Please check your connection to azure storage")
