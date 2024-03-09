# MarkdownToMindMap
## 功能介绍
这是一个可以将Markdown文件转化为思维导图（PDF格式）的文件。注意，生成的思维导图只会保留各级标题的信息，而不会显示标题下的内容。
## 运行需求及使用方法
运行前需要安装graphviz库
> Graphviz是一个开源的图形可视化软件，它提供了一种简单的描述语言来描述图形结构以及一系列用于绘制这些结构的工具。Graphviz提供了多种布局算法，可以根据用户提供的图形描述自动生成图形的布局

```
pip install graphviz
```

使用时，将需要转换的Markdown文件放入MD文件夹中，将mindmap.py中的filename该为Markdown文件的名字，运行这个程序，结果会保存在PDF文件夹中。
