import graphviz
import os
from reader import Markdown_reader


class Mindmap:
    def __init__(self, titles, filename):
        self.titles = titles
        self.edge_list = []
        self.node_count = 0
        self.graph = graphviz.Digraph(comment='思维导图')
        self.filename = filename.strip()[:-3]

    def construct(self):
        for root in self.titles:
            self.construct_tree(root, None)
        self.graph.edges(self.edge_list)
        self.save()

    def construct_tree(self, root, parent):
        new_parent = self.node_count
        self.graph.node(str(self.node_count), root.content, fontname="Fangsong")
        if parent is not None:
            self.edge_list.append((str(parent), str(self.node_count)))
        self.node_count += 1
        if not root.children:
            return
        else:
            for child in root.children:
                self.construct_tree(child, new_parent)

    def save(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        output_folder = os.path.join(current_directory, 'PDF')
        output_path = os.path.join(output_folder, self.filename+'_MindMap')
        # 如果文件夹不存在，创建它
        os.makedirs(output_folder, exist_ok=True)
        # 保存图像文件
        self.graph.render(output_path, format='pdf', cleanup=True)


if __name__ == "__main__":
    filename = "test_file.md"
    reader = Markdown_reader(filename)
    title = reader.parse_content()
    Map = Mindmap(title, filename)
    Map.construct()
