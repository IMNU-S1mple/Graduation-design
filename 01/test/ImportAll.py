import sys
import  os
# 获取当前文件所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 获取当前文件所在目录的父级目录
parent_dir = os.path.dirname(current_dir)

pparent_dir = os.path.dirname(parent_dir)

def add_all_subdirectories_to_syspath(path):
    for root, dirs, files in os.walk(path):
        for d in dirs:
            dir_path = os.path.abspath(os.path.join(root, d))
            sys.path.append(dir_path)

add_all_subdirectories_to_syspath(pparent_dir)