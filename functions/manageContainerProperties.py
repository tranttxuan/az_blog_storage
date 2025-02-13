
from functions.common.createContainer import get_container_client


def set_container_properties(connection_string, container_name):
    # Set container properties
    container_client = get_container_client(
        connection_string, container_name)
    properties = container_client.get_container_properties()
    print(f"Properties before setting metadata: {properties}")

    # Add metadata
    metadata = {
        'category': 'images',
        'owner': 'admin'
    }
    container_client.set_container_metadata(metadata)

    # Retrieve updated properties
    properties = container_client.get_container_properties()
    print(f"Properties after setting metadata: {properties}")


def list_container_properties(connection_string, container_name):
    container_client = get_container_client(connection_string, container_name)
    properties = container_client.get_container_properties()
    print(f"Container metadata: {properties['metadata']}")
    print(f"Other properties: {properties}")
