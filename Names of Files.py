import os
import re


def list_files_in_folder(folder_path, output_file_path):
    """
    Lists the names of all the files in the specified folder and saves them in a text file.
    
    Args:
        folder_path (str): Path to the folder.
        output_file_path (str): Path to the output text file.
    """
    entries = os.listdir(folder_path)

    with open(output_file_path, 'w') as file:
        for entry in entries:
            decoded_string = entry.encode('unicode_escape').decode()
            clean_string = re.sub(r'\\u[0-9a-fA-F]{4}', '', decoded_string)
            file.write(clean_string)
            file.write("\n")


# Example usage
folder_path = ""
output_file_path = ""
list_files_in_folder(folder_path, output_file_path)