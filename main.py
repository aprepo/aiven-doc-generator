import requests


def print_row(param, value_type, desc):
    print(f"  * - {param}")
    print(f"    - {value_type}")
    print(f"    - {desc}")

def print_header(txt):
    print(txt)
    print(f"".ljust(len(txt), "-"))


def print_service_type_docs(service_type, data):
    schema = data['service_types'][service_type]['user_config_schema']

    print("")
    # Table header
    print(".. list-table::")
    print("  :header-rows: 1")
    print("")
    print_row("Parameter", "Value Type", "Description")

    # Rows
    for key, value in schema['properties'].items():
        title = value['title']
        print_row(
            f"``{key}``", 
            #f"``{value.get('title', '')}``", 
            value.get('type', ''), 
            value.get('title') + " " + value.get("description", '')
            )
        pass
    # Empty row to end
    print("")


def main():
    response = requests.get("https://api.aiven.io/v1/service_types")
    data = response.json()
    for service_type in data['service_types']:
        print_header(f"Service type: {service_type}")
        print_service_type_docs(service_type, data)


if __name__ == '__main__':
    main()
