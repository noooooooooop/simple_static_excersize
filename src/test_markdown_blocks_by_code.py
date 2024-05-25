import unittest

from markdown_blocks_by_code import markdown_blocks_by_code
from textnode import TextNode

if 'unittest.util' in __import__('sys').modules:
    # Show full diff in self.assertEqual.
    __import__('sys').modules['unittest.util']._MAX_LENGTH = 999999999


class TestMain(unittest.TestCase):
    def test_breakup_markdown_1(self):
        doc = \
"""This is a block
```This is a code block
This is a code block```

This is a block
`This` is an `inline` code block and should not be split
This is a block

```This is a code block
This is a code block
```

This is a block
This is a block
This is a block
"""
        doc = markdown_blocks_by_code(doc)

        self.assertEqual(doc, [
        "This is a block",
        "```This is a code block\nThis is a code block```",

         """
This is a block
`This` is an `inline` code block and should not be split
This is a block
""",

        "```This is a code block\nThis is a code block```",

         """
This is a block
This is a block
This is a block
""",
        ])

    def test_breakup_markdown_2(self):
        docs = [
            """This is a block
```This is a code block```
This is a block""",
            """This is a block
```This is a code block```
This is a block""",
        ]

        docs = markdown_blocks_by_code(docs)

        self.assertEqual(docs, [
        "This is a block",
        "```This is a code block```",
        "This is a block",
        "This is a block",
        "```This is a code block```",
        "This is a block",
        ])

    def test_breakup_markdown_3(self):
        docs = [
            "",
            "",
        ]

        docs = markdown_blocks_by_code(docs)

        self.assertEqual(docs, [
            "",
            "",
        ])

if __name__ == "__main__":
    unittest.main()
