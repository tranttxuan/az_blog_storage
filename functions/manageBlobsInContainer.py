from functions.common.createContainer import create_container_if_not_exists, connect_to_blob_service_client


def upload_blob(blob_name, file_path, blob_client):

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
