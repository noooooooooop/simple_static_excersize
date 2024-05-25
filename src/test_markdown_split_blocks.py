import unittest

from markdown_split_blocks import markdown_split_blocks, get_block_type
from textnode import TextNode

if 'unittest.util' in __import__('sys').modules:
    # Show full diff in self.assertEqual.
    __import__('sys').modules['unittest.util']._MAX_LENGTH = 999999999


class TestMain(unittest.TestCase):
    def test_breakup_markdown_0(self):
        doc = """This is a paragraph
This is a paragraph
This is a paragraph"""

        doc = markdown_split_blocks(doc)

        self.assertEqual(doc, [
            "This is a paragraph\nThis is a paragraph\nThis is a paragraph"
        ])

    def test_breakup_markdown_1(self):
        doc = """This is a block1
# This is a heading1
This is a block2

This is a block3
This is a block4
This is a block5

# This is a heading2
### This is a heading3
"""
        doc = markdown_split_blocks(doc)

        self.assertEqual(doc, [
        "This is a block1",
        "# This is a heading1",
        "This is a block2",
         """This is a block3
This is a block4
This is a block5""",
        "# This is a heading2",
        "### This is a heading3",
        ])

    def test_breakup_markdown_2(self):
        docs = ""
        docs = markdown_split_blocks(docs)

        self.assertEqual(docs, [])

    def test_breakup_markdown_3(self):
        doc = """This is a block1
1. This is a list1
2. This is a list2
3. This is a list3
This is a block2

This is a block3
This is a block4
This is a block5

1. This is a list4

1. This is a list5
"""
        doc = markdown_split_blocks(doc)

        self.assertEqual(doc, [
        "This is a block1",

        """1. This is a list1
2. This is a list2
3. This is a list3""",

        "This is a block2",

        """This is a block3
This is a block4
This is a block5""",

        "1. This is a list4",

        "1. This is a list5",
        ])

    def test_breakup_markdown_4(self):
        doc = """This is a block1
> This is a quote1
This is a block2

This is a block3
This is a block4
This is a block5

> This is a quote2
> This is a quote3
"""
        doc = markdown_split_blocks(doc)

        self.assertEqual(doc, [
        "This is a block1",

        "> This is a quote1",

        "This is a block2",

        """This is a block3
This is a block4
This is a block5""",

        "> This is a quote2\n> This is a quote3",
        ])

    def test_breakup_markdown_5(self):
        doc = """This is a block1
* This is a list1
* This is a list2
* This is a list3
This is a block2

This is a block3
This is a block4
This is a block5

* This is a list4

* This is a list5
"""
        doc = markdown_split_blocks(doc)

        self.assertEqual(doc, [
        "This is a block1",

        """* This is a list1
* This is a list2
* This is a list3""",

        "This is a block2",

        """This is a block3
This is a block4
This is a block5""",

        "* This is a list4",

        "* This is a list5",
        ])

    def test_breakup_markdown_6(self):
        doc = """This is a block.
This is part of the same block.

This is another block.
This is part of another same block."""

        doc = markdown_split_blocks(doc)

        self.assertEqual(doc, [
            "This is a block.\nThis is part of the same block.",
            "This is another block.\nThis is part of another same block.",
        ])

    def test_breakup_markdown_7(self):
        doc = """
        

This is a block.
This is part of the same block.





This is another block.
This is part of another same block.



"""
        doc = markdown_split_blocks(doc)

        self.assertEqual(doc, [
            "This is a block.\nThis is part of the same block.",
            "This is another block.\nThis is part of another same block.",
        ])


    def test_breakup_markdown_8(self):
        self.maxDiff = None

        doc = """# This is a heading
```This is a code block
This is a code block```
This is a block

This is a block
`This` is an `inline` code block and should not be split
This is a block

* This is an unordered list
* This is an unordered list
* This is an unordered list

1. This is an ordered list
2. This is an ordered list
3. This is an ordered list

> This is a
> multiline
> quote

This is a block
This is a block
This is a block
"""
        doc = markdown_split_blocks(doc)

        self.assertEqual(doc, [
        "# This is a heading",

        "```This is a code block\nThis is a code block```",

        "This is a block",

         "This is a block\n`This` is an `inline` code block and should not be split\nThis is a block",

        "* This is an unordered list\n* This is an unordered list\n* This is an unordered list",

        "1. This is an ordered list\n2. This is an ordered list\n3. This is an ordered list",

        "> This is a\n> multiline\n> quote",

        "This is a block\nThis is a block\nThis is a block",
        ])

    def test_identify_1(self):
        self.maxDiff = None

        block = "# This is a heading"
        block_type = get_block_type(block)

        self.assertEqual(block_type, "heading")

    def test_identify_2(self):
        self.maxDiff = None

        block = """* This is an unordered list
* This is an unordered list
* This is an unordered list"""

        block_type = get_block_type(block)

        self.assertEqual(block_type, "unordered_list")

    def test_identify_3(self):
        self.maxDiff = None

        block = """1. This is an unordered list
2. This is an ordered list
3. This is an ordered list"""

        block_type = get_block_type(block)

        self.assertEqual(block_type, "ordered_list")

    def test_identify_4(self):
        self.maxDiff = None

        block = """```This is a code block
This is a code block
This is a code block```"""

        block_type = get_block_type(block)

        self.assertEqual(block_type, "code")

    def test_identify_5(self):
        self.maxDiff = None

        block = """> This is a quote
> This is a quote
> This is a quote"""

        block_type = get_block_type(block)

        self.assertEqual(block_type, "quote")

    def test_identify_6(self):
        self.maxDiff = None

        block = """This is a paragraph
This is a paragraph
This is a paragraph"""

        block_type = get_block_type(block)

        self.assertEqual(block_type, "paragraph")

if __name__ == "__main__":
    unittest.main()
