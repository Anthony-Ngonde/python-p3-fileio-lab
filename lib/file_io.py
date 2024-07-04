from pathlib import Path

def write_file(file_name, file_content):

    file_path = Path(file_name).with_suffix('.txt')
    with file_path.open('w') as file:
        file.write(file_content)

def append_file(file_name, file_content):
    file_path = Path(file_name).with_suffix('.txt')
    with file_path.open('a') as file:
        file.write(file_content)

def read_file(file_name):
    file_path = Path(file_name).with_suffix('.txt')
    with file_path.open('r') as file:
        return file.read()


# Example usage:
write_file(file_name="logfile", file_content="Log 1: 5 bananas added")
append_file(file_name="logfile", file_content="Log 2: 3 bananas subtracted")
content = read_file(file_name="logfile")
print(content)