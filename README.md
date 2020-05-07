# FileInterface
An interface for you to find files and request the file name of a file

Usage:
```
interface = getFileInfo()

result = interface.UserInterface("pdf")
# <class instance>.UserInterface(<file type>)

files = interface.findFiles("docx")
```
.UserInterface(<file type>) method returns a `FileInfo` object.
```
>>> result.file_type
  pdf
>>> result.filename
  helloworld.pdf
>>> result.file_path
  C:\...\helloworld.pdf
```
File must be placed in the working directory of the python file.

You can add more file types + regex in the FileRegex.json file if neccessary.
