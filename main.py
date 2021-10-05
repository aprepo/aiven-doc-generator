import requests


def print_service_type_docs(service_type, data):
    schema = data['service_types'][service_type]['user_config_schema']
    for key, value in schema['properties'].items():
        title = value['title']
        print(f"{key}")
        print(f"   {value['title']}")
        print(f"   {value['type']}")
        print(f"   {value.get('description','')}")


def main():
    response = requests.get("https://api.aiven.io/v1/service_types")
    data = response.json()
    for service_type in data['service_types']:
        print(f"Service type: {service_type}")
        print_service_type_docs(service_type, data)


if __name__ == '__main__':
    main()
