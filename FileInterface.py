import os
import re
import json

class FileError(Exception):
    """File not found"""
    pass

class InputError(Exception):
    """Values input incorrect"""
    pass

class FileInfo(object):
    """
    'file_path' attribute found when in the same directory, can be otherwise entered manually
    """
    def __init__(self, filename: str, file_type: str, file_path = None):
        self.filename = filename
        self.file_type = file_type
        self.manual_file_path = file_path

    @property
    def file_path(self, path = os.path.dirname(os.path.realpath(__file__))):
        if self.manual_file_path == 0:
            return self.manual_file_path
        else:
            filenames = []
            for root, dirs, files in os.walk(path):
                if self.filename in files:
                    filenames.append(os.path.join(root, self.filename))
            if (x := len(filenames)) == 1:
                return filenames[0]
            elif x > 1:
                raise InputError(f"Multiple files of {self.filename}")
            elif x == 0:
                raise InputError(f"File {self.filename} not found")
            else:
                raise InputError("Unknown error occured")

    def __str__(self):
        return f"""
        Filename: {self.filename}
        File Path: {self.file_path}
        File Type: {self.file_type}
        """

class getFileData():
    """
    Method find_all: Default parameter for path is the directory of the file.
    """

    regex_file_info = FileInfo("FileRegex.json", "json")

    @property
    def file_type_regex(self):
        with open(self.regex_file_info.file_path, "r") as json_file:
            regex = json.load(json_file)
        return regex

    def findFiles(self, file_type,  path = os.path.dirname(os.path.realpath(__file__))):
        paths = [] # instanciate paths list
        filenames = [] # instanciate filenames list
        for root, dirs, files in os.walk(path):
            for filename in files:
                if re.search(self.file_type_regex[file_type] ,filename) != None: # Check if .??? is in the filename
                    paths.append(os.path.join(root, filename)) # adds path to the paths list
                    filenames.append(filename) # adds filename to filenames list
        if len(paths) >= 1:
            return {"paths": tuple(paths), "filenames": tuple(filenames), "file_type": "Excel"}
        elif len(paths) == 0: # check if file exists
            raise FileError("File not found") # raises file error
        else:
            raise FileError("Unknown Error") # traises file error

    def UserInterface(self, file_type):
        num1, num2 = 0, 0
        file_dict= self.findFiles(file_type)
        filename_list = file_dict["filenames"]
        file_paths_list = file_dict["paths"]
        print()
        for filename in filename_list: #finds all filenames with the specified file type
            num1 += 1
            print(f"{str(num1)}. {filename}\n") # prints out options
        file_choice = int(input("Choose File: ")) - 1 # Asks User for the file choice (Relative to a list)
        
        return FileInfo(filename_list[file_choice], file_type, file_paths_list[file_choice])
