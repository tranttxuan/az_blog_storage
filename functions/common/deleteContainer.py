from functions.common.createContainer import get_container_client


def delete_container(connection_string, container_name):
    container_client = get_container_client(connection_string, container_name)
    container_client.delete_container()
    print(f"Container '{container_name}' deleted.")
