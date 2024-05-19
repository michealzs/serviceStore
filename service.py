import os

def get_user_input(prompt):
    return input(prompt).strip()

def create_systemd_service_file(user, group, project_name, project_location):
    service_content = f"""[Unit]
Description=uWSGI service for {project_name}
After=network.target

[Service]
User={user}
Group={group}
WorkingDirectory={project_location}
ExecStart={project_location}/venv/bin/uwsgi --ini {project_location}/uwsgi.ini

[Install]
WantedBy=multi-user.target
"""
    service_file_path = f"/etc/systemd/system/{project_name}.service"
    try:
        with open(service_file_path, 'w') as service_file:
            service_file.write(service_content)
        print(f"Service file created at {service_file_path}")
    except PermissionError:
        print("Permission denied. Please run the script with sudo or as root.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    user = get_user_input("Enter the user: ")
    group = get_user_input("Enter the group: ")
    project_name = get_user_input("Enter the project name: ")
    project_location = get_user_input("Enter the project location: ")

    create_systemd_service_file(user, group, project_name, project_location)

if __name__ == "__main__":
    main()
