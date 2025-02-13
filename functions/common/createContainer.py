from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ResourceExistsError


def connect_to_blob_service_client(connection_string):
    try:
        return BlobServiceClient.from_connection_string(connection_string)
    except Exception as e:
        print(f"Error creating container: {e}")


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
