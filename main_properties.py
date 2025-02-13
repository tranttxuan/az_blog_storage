from dotenv import load_dotenv
import os
from functions.manageContainerProperties import list_container_properties, set_container_properties

load_dotenv()


if __name__ == "__main__":

    container_name = os.getenv("CONTAINER_NAME")
    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

    if not connection_string:
        raise ValueError(
            "AZURE_STORAGE_CONNECTION_STRING is not set in .env file")

    set_container_properties(connection_string, container_name)

    list_container_properties(connection_string, container_name)
