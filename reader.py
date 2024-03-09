from io import StringIO
from enum import Enum
import os


class Type(Enum):
    paragraph = 0
    HEAD_1 = 1
    HEAD_2 = 2
    HEAD_3 = 3
    HEAD_4 = 4
    HEAD_5 = 5
    HEAD_6 = 6


def Type_convert(line_type):
    if line_type == Type.paragraph:
        return 0
    elif line_type == Type.HEAD_1:
        return 1
    elif line_type == Type.HEAD_2:
        return 2
    elif line_type == Type.HEAD_3:
        return 3
    elif line_type == Type.HEAD_4:
        return 4
    elif line_type == Type.HEAD_5:
        return 5
    elif line_type == Type.HEAD_6:
        return 6


def check_title(line):
    if not line.startswith('#'):
        return Type.paragraph, None
    elif not line.startswith('##'):
        return Type.HEAD_1, line.lstrip('#').strip()
    elif not line.startswith('###'):
        return Type.HEAD_2, line.lstrip('#').strip()
    elif not line.startswith('####'):
        return Type.HEAD_3, line.lstrip('#').strip()
    elif not line.startswith('#####'):
        return Type.HEAD_4, line.lstrip('#').strip()
    elif not line.startswith('######'):
        return Type.HEAD_5, line.lstrip('#').strip()
    else:
        return Type.HEAD_6, line.lstrip('#').strip()


def print_tree(node, level=0):
    if node is not None:
        print("  " * level + str(node.content))
        for child in node.children:
            print_tree(child, level + 1)


class TreeNode:
    def __init__(self, content, parent, level):
        self.content = content
        self.parent = parent
        self.children = []
        self.level = level

    def add_child(self, child_node):
        self.children.append(child_node)


class Markdown_content:
    def __init__(self):
        self.title = []

    def add(self, line):
        line = line.strip()
        line_type = check_title(line)[0]
        content = check_title(line)[1]

        if line_type == Type.paragraph:
            pass
        elif line_type == Type.HEAD_1:
            node = TreeNode(content, None, Type.HEAD_1)
            self.title.append(node)
        else:
            index = 2
            parent = self.title[-1]
            while index < Type_convert(line_type):
                try:
                    parent = parent.children[-1]
                except:
                    self.info()
                    assert 0
                index += 1
            node = TreeNode(content, parent, Type.HEAD_2)
            parent.add_child(node)

    def info(self):
        for node in self.title:
            print_tree(node)


class Markdown_reader:
    def __init__(self, filename, encoding='utf-8'):
        self.markdown_content = Markdown_content()
        # 获取当前脚本的目录
        current_directory = os.path.dirname(os.path.abspath(__file__))
        # 指定 MD 文件夹路径
        md_folder = os.path.join(current_directory, 'MD')
        # 指定要打开的 MD 文件名
        filename_to_open = filename
        # 构建完整的文件路径
        file_to_open = os.path.join(md_folder, filename_to_open)
        with open(file_to_open, 'r', encoding=encoding) as file:
            self.__content = file.read()

    def parse_content(self):
        with StringIO(self.__content) as file:
            for line in file:
                # print(line.strip())
                self.markdown_content.add(line)
        self.markdown_content.info()
        return self.markdown_content.title


if __name__ == "__main__":
    m = Markdown_reader(filename="test_file.md", encoding="utf-8")
    m.parse_content()

# 可能的新功能
# 1.错误修正，如一级标题下直接接三级标题，可以修正三级标题为二级标题
# paragraph总结功能
