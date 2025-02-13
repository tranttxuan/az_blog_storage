from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ResourceExistsError


def connect_to_blob_service_client(connection_string):
    return BlobServiceClient.from_connection_string(connection_string)


def create_container_if_not_exists(connection_string, container_name):
    """Create a container if it doesn't already exist."""
    blob_service_client = connect_to_blob_service_client(connection_string)
    container_client = blob_service_client.get_container_client(container_name)

    try:
        container_client.create_container()
        print(f"Container '{container_name}' created successfully.")
    except ResourceExistsError:
        print(f"Container '{container_name}' already exists.")

    return container_client


def get_blob_client_by_name(connection_string, container_name, blob_name):
    """Returns a BlobClient for the given blob name"""
    container_client = create_container_if_not_exists(
        connection_string, container_name)
    blob_client = container_client.get_blob_client(blob_name)
    return blob_client


def updoad_blob(blob_name, file_path, blob_client):

    with open(file_path, "rb") as data:
        blob_client.upload_blob(data)

    print(f"Uploaded {file_path} to {blob_name}.")


def download_blob(blob_name, download_path, blob_client):
    with open(download_path, "wb") as download_file:
        download_file.write(blob_client.download_blob().readall())
    print(f"Downloaded {blob_name} to {download_path}.")


def list_blobs(connection_string, container_name, blob_client):
    """Lists blobs in a given container."""
    blob_service_client = connect_to_blob_service_client(connection_string)
    container_client = blob_service_client.get_container_client(container_name)

    blob_list = container_client.list_blobs()
    for blob in blob_list:
        print(f"Blob name: {blob.name}")
