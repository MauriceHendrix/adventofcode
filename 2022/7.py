from dataclasses import dataclass
from typing import List
input = open('7.txt').readlines()


@dataclass
class File:
    size: int
    name: str

@dataclass
class Folder:
    dis_str: str
    files: List[File]
    folders: List['Folder']
    parent: 'Folder'

    def total_size(self) -> int:
        return sum(file.size for file in self.files) + sum(folder.total_size() for folder in self.folders)

all_folders = {}
current_folder = ''
for line in input:
    line=line.strip()
    if line.startswith('$ cd ..'):
        current_folder = all_folders[current_folder].parent.dis_str
    elif line.startswith('$ cd '):
        parent = current_folder
        current_folder += '|' + line[5:]
        all_folders.setdefault(current_folder, Folder(current_folder, [], [], all_folders.get(parent, None)))
        assert current_folder in all_folders
        if parent != '':
            all_folders[parent].folders.append(all_folders[current_folder])
    elif line[0].isnumeric():
        size, name = line.split(' ')
        all_folders[current_folder].files.append(File(int(size), name))
#    print([line, current_folder])

#print(all_folders)
print(sum(folder.total_size() for folder in all_folders.values() if folder.total_size() <= 100000))
#print(all_folders['|/|a'])