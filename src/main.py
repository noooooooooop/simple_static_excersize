from textnode import TextNode

text_types = [
    "text",
    "bold",
    "italic",
    "code",
    "link",
    "image",
]

def main():
    test = TextNode('asdfasdfsfasdf', 'aasdfafsd', 'http://not.a.real.website.asdfasdfasdfasdfasdfadfdasf')
    print(test)

if __name__ == '__main__':
    main()
