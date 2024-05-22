from textnode import TextNode
from split_nodes_delimiter import split_nodes_delimiter
from extract_markdown_links import split_markdown_links

text_types = [
    "text",
    "bold",
    "italic",
    "code",
    "link",
    "image",
]

# TODO: support headers
def convert_markdown_to_textnodes(doc: str):
    nodes = [TextNode(doc, "text")]

    nodes = split_nodes_delimiter(nodes, "**", "italic")
    nodes = split_nodes_delimiter(nodes, "*", "bold")
    nodes = split_nodes_delimiter(nodes, "`", "bold")
    nodes = split_markdown_links(nodes, is_image=False)
    nodes = split_markdown_links(nodes, is_image=True)

    return nodes

def main():
    test = TextNode('asdfasdfsfasdf', 'aasdfafsd', 'http://not.a.real.website.asdfasdfasdfasdfasdfadfdasf')
    print(test)

if __name__ == '__main__':
    main()
