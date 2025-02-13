

# def set_container_properties():
#     # Set container properties
#     properties = container_client.get_container_properties()
#     print(f"Properties before setting metadata: {properties}")

#     # Add metadata
#     metadata = {
#         'category': 'images',
#         'owner': 'admin'
#     }
#     container_client.set_container_metadata(metadata)

#     # Retrieve updated properties
#     properties = container_client.get_container_properties()
#     print(f"Properties after setting metadata: {properties}")

# def list_container_properties():
#     properties = container_client.get_container_properties()
#     print(f"Container metadata: {properties['metadata']}")
#     print(f"Other properties: {properties}")

# def delete_container():
#     container_client.delete_container()
#     print(f"Container '{container_name}' deleted.")
