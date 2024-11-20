import os
import shutil
import glob

def get_directory():
    return input("Enter the path to your directory:\n")

def define_file_types():
    return {
        'image': ['.jpg', '.png', '.gif'],
        'video': ['.mp4', '.avi', '.mov'],
        'document': ['.pdf', '.docx', '.txt'],
        'audio': ['.mp3', '.wav', '.ogg'],
        'compressed': ['.zip', '.rar', '.7z'],
        'executable': ['.exe', '.msi', '.apk'],
        'code': ['.py', '.java', '.c', '.js'],
        'spreadsheet': ['.xlsx', '.xls', '.csv'],
        'presentation': ['.pptx', '.ppt', '.odp'],
    }

def create_folders(directory, file_types):
    for folder in file_types.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def move_files(directory, file_types):
    for file in glob.glob(directory + '/*'):
        if os.path.isfile(file):
            file_extension = os.path.splitext(file)[1].lower()
            moved = False
            for type, extensions in file_types.items():
                if file_extension in extensions:
                    shutil.move(file, os.path.join(directory, type))
                    print(f"Moved {file} to {type} folder")
                    moved = True
                    break
            if not moved:
                print(f"File {file} type not recognized")
                shutil.move(file, os.path.join(directory, 'unknown'))
                print(f"Moved {file} to unknown folder")
        elif os.path.isdir(file):
            print(f"Skipping directory {file}")

def main():
    directory = get_directory()
    file_types = define_file_types()
    create_folders(directory, file_types)
    move_files(directory, file_types)

if __name__ == "__main__":
    main()
