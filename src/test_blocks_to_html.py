import unittest

from blocks_to_html import block_headings_to_html, block_ordered_list_to_html, block_paragraph_to_html, block_unordered_list_to_html, block_quote_to_html, block_code_to_html, blocks_to_html
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

if 'unittest.util' in __import__('sys').modules:
    # Show full diff in self.assertEqual.
    __import__('sys').modules['unittest.util']._MAX_LENGTH = 999999999


class TestHTMLNode(unittest.TestCase):
    def test_ol_block_to_html_1(self):
        result = block_ordered_list_to_html("1. This is a list")

        self.assertEqual(
            result,
            ParentNode(
                "ol",
                [
                    ParentNode("li", [LeafNode(value="This is a list")]),
                ]
            )
        )

    def test_ol_block_to_html_2(self):
        result = block_ordered_list_to_html("1. This is a list\n2. This is a list\n3. This is a list")

        self.assertEqual(
            result,
            ParentNode(
                "ol",
                [
                    ParentNode("li", [LeafNode(value="This is a list")]),
                    ParentNode("li", [LeafNode(value="This is a list")]),
                    ParentNode("li", [LeafNode(value="This is a list")]),
                ]
            )
        )

    def test_ol_block_to_html_3(self):
        result = block_ordered_list_to_html("1. **This** is a list\n2. This is a list\n3. This is a list")

        self.assertEqual(
            result,
            ParentNode(
                "ol",
                [
                    ParentNode("li", [
                               LeafNode("i", value="This"),
                               LeafNode(value=" is a list"),
                               ]),
                    ParentNode("li", [LeafNode(value="This is a list")]),
                    ParentNode("li", [LeafNode(value="This is a list")]),
                ]
            )
        )

    def test_ul_block_to_html_1(self):
        result = block_unordered_list_to_html("* *This* is a list\n* This is a list\n* This is a list")

        self.assertEqual(
            result,
            ParentNode(
                "ul",
                [
                    ParentNode("li", [
                               LeafNode("b", value="This"),
                               LeafNode(value=" is a list"),
                               ]),
                    ParentNode("li", [LeafNode(value="This is a list")]),
                    ParentNode("li", [LeafNode(value="This is a list")]),
                ]
            )
        )

    def test_quote_block_to_html_1(self):
        result = block_quote_to_html("> *This* is a list\n> This is a list\n> This is a list")

        self.assertEqual(
            result,
            ParentNode(
                "blockquote",
                [
                    ParentNode("p", [
                               LeafNode("b", value="This"),
                               LeafNode(value=" is a list"),
                               ]),
                    ParentNode("p", [LeafNode(value="This is a list")]),
                    ParentNode("p", [LeafNode(value="This is a list")]),
                ]
            )
        )

    def test_quote_code_to_html_1(self):
        result = block_code_to_html(f"""def some_func(arg: asdf):
    for stuff in range(0, len(arg)):
        do stuff
""")

        self.assertEqual(
            result,
            ParentNode("pre", [
                LeafNode("code", 
f"""def some_func(arg: asdf):
    for stuff in range(0, len(arg)):
        do stuff
"""
                )
            ])
        )

    def test_headings_to_html_1(self):
        result = block_headings_to_html("# *This* is a heading")

        self.assertEqual(
            result,
            ParentNode("h1", [
               LeafNode("b", value="This"),
               LeafNode(value=" is a heading"),
            ]),
        )

    def test_headings_to_html_2(self):
        result = block_headings_to_html("### This is a heading")

        self.assertEqual(
            result,
            ParentNode("h3", [
               LeafNode(value="This is a heading"),
            ]),
        )

    def test_headings_to_html_3(self):
        result = block_headings_to_html("###### This is a heading")

        self.assertEqual(
            result,
            ParentNode("h6", [
               LeafNode(value="This is a heading"),
            ]),
        )

    def test_paragraph_to_html_1(self):
        result = block_paragraph_to_html("This is a paragraph")

        self.assertEqual(
            result,
            ParentNode("p", [
               LeafNode(value="This is a paragraph"),
            ]),
        )

    def test_paragraph_to_html_2(self):
        result = block_paragraph_to_html("**This** is a paragraph")

        self.assertEqual(
            result,
            ParentNode("p", [
               LeafNode("i", "This"),
               LeafNode(value=" is a paragraph"),
            ]),
        )

    def test_ol_block_to_html_1_to_html(self):
        result = block_ordered_list_to_html("1. This is a list").to_html()

        self.assertEqual(
            result,
            "<ol><li>This is a list</li></ol>"
        )

    def test_ol_block_to_html_2_to_html(self):
        result = block_ordered_list_to_html("1. This is a list\n2. This is a list\n3. This is a list").to_html()

        self.assertEqual(
            result,
            "<ol><li>This is a list</li><li>This is a list</li><li>This is a list</li></ol>"
        )

    def test_ol_block_to_html_3_to_html(self):
        result = block_ordered_list_to_html("1. **This** is a list\n2. This is a list\n3. This is a list").to_html()

        self.assertEqual(
            result,
            "<ol><li><i>This</i> is a list</li><li>This is a list</li><li>This is a list</li></ol>"
        )

    def test_ul_block_to_html_1_to_html(self):
        result = block_unordered_list_to_html("* *This* is a list\n* This is a list\n* This is a list").to_html()

        self.assertEqual(
            result,
            "<ul><li><b>This</b> is a list</li><li>This is a list</li><li>This is a list</li></ul>"
        )

    def test_quote_block_to_html_1_to_html(self):
        result = block_quote_to_html("> *This* is a list\n> This is a list\n> This is a list").to_html()

        self.assertEqual(
            result,
            "<blockquote><p><b>This</b> is a list</p><p>This is a list</p><p>This is a list</p></blockquote>"
        )

    def test_code_block_to_html_1_to_html(self):
        result = block_code_to_html(f"""def some_func(arg: asdf):
    for stuff in range(0, len(arg)):
        do stuff
""").to_html()

        self.assertEqual(
            result, """<pre><code>def some_func(arg: asdf):
    for stuff in range(0, len(arg)):
        do stuff
</code></pre>"""
        )

    def test_headings_to_html_1_to_html(self):
        result = block_headings_to_html("# *This* is a heading").to_html()

        self.assertEqual(
            result,
            "<h1><b>This</b> is a heading</h1>"
        )

    def test_headings_to_html_2_to_html(self):
        result = block_headings_to_html("### This is a heading").to_html()

        self.assertEqual(
            result,
            "<h3>This is a heading</h3>"
        )

    def test_headings_to_html_3_to_html(self):
        result = block_headings_to_html("###### This is a heading").to_html()

        self.assertEqual(
            result,
            "<h6>This is a heading</h6>"
        )

    def test_paragraph_to_html_1_to_html(self):
        result = block_paragraph_to_html("This is a paragraph").to_html()

        self.assertEqual(
            result,
            "<p>This is a paragraph</p>"
        )

    def test_paragraph_to_html_2_to_html(self):
        result = block_paragraph_to_html("**This** is a paragraph").to_html()

        self.assertEqual(
            result,
            "<p><i>This</i> is a paragraph</p>"
        )

    def test_blocks_to_html_headings(self):
        input = [
            "## This is a heading",
            "#### This is a heading",
            "###### This is a heading",
        ]

        result = blocks_to_html(input)

        self.assertEqual(
            result,
            ParentNode("div", [
                ParentNode("h2", [ LeafNode(value="This is a heading") ]),
                ParentNode("h4", [ LeafNode(value="This is a heading") ]),
                ParentNode("h6", [ LeafNode(value="This is a heading") ]),
            ])
        )

    def test_blocks_to_html_paragraphs(self):
        input = [
            "This is a paragraph",
            "This is a paragraph",
        ]

        result = blocks_to_html(input)

        self.assertEqual(
            result,
            ParentNode("div", [
                ParentNode("p", [ LeafNode(value="This is a paragraph") ]),
                ParentNode("p", [ LeafNode(value="This is a paragraph") ]),
            ])
        )

    def test_blocks_to_html_ordered_list(self):
        input = [
            "1. This is an ordered list\n2. This is an ordered list",
        ]

        result = blocks_to_html(input)

        self.assertEqual(
            result,
            ParentNode("div", [
                ParentNode("ol", [
                    ParentNode("li", [ LeafNode(value="This is an ordered list") ]),
                    ParentNode("li", [ LeafNode(value="This is an ordered list") ]),
                ]),
            ])
        )

    def test_blocks_to_html_unordered_list(self):
        input = [
            "* This is an unordered list\n* This is an unordered list",
        ]

        result = blocks_to_html(input)

        self.assertEqual(
            result,
            ParentNode("div", [
                ParentNode("ul", [
                    ParentNode("li", [ LeafNode(value="This is an unordered list") ]),
                    ParentNode("li", [ LeafNode(value="This is an unordered list") ]),
                ]),
            ])
        )

    def test_blocks_to_html_quote(self):
        input = [
            "> This is a quote\n> This is a quote",
        ]

        result = blocks_to_html(input)

        self.assertEqual(
            result,
            ParentNode("div", [
                ParentNode("blockquote", [
                    ParentNode("p", [ LeafNode(value="This is a quote") ]),
                    ParentNode("p", [ LeafNode(value="This is a quote") ]),
                ]),
            ])
        )

    def test_blocks_to_html_code(self):
        input = [
            """```def some_func(args: adsf):
    for thing in args:
        do stuff```""",
        ]

        result = blocks_to_html(input)

        self.assertEqual(
            result,
            ParentNode("div", [
                ParentNode("pre", [
                    LeafNode("code", value="""def some_func(args: adsf):
    for thing in args:
        do stuff"""),
                ]),
            ])
        )

    def test_blocks_to_html_all(self):
        input = [
            "## This is a heading",
            "#### This is a heading",
            "###### This is a heading",
            "This is a paragraph",
            "This is a paragraph",
            "1. This is an ordered list\n2. This is an ordered list",
            "* This is an unordered list\n* This is an unordered list",
            "> This is a quote\n> This is a quote",
            """```def some_func(args: adsf):
    for thing in args:
        do stuff```""",
        ]

        result = blocks_to_html(input)

        self.assertEqual(
            result,
            ParentNode("div", [
                ParentNode("h2", [ LeafNode(value="This is a heading") ]),
                ParentNode("h4", [ LeafNode(value="This is a heading") ]),
                ParentNode("h6", [ LeafNode(value="This is a heading") ]),
                ParentNode("p", [ LeafNode(value="This is a paragraph") ]),
                ParentNode("p", [ LeafNode(value="This is a paragraph") ]),
                ParentNode("ol", [
                    ParentNode("li", [ LeafNode(value="This is an ordered list") ]),
                    ParentNode("li", [ LeafNode(value="This is an ordered list") ]),
                ]),
                ParentNode("ul", [
                    ParentNode("li", [ LeafNode(value="This is an unordered list") ]),
                    ParentNode("li", [ LeafNode(value="This is an unordered list") ]),
                ]),
                ParentNode("blockquote", [
                    ParentNode("p", [ LeafNode(value="This is a quote") ]),
                    ParentNode("p", [ LeafNode(value="This is a quote") ]),
                ]),

                ParentNode("pre", [
                    LeafNode("code", value="""def some_func(args: adsf):
    for thing in args:
        do stuff"""),
                ]),
            ])
        )

    def test_blocks_to_html_headings_to_html(self):
        self.maxDiff = None

        input = [
            "## This is a heading",
            "#### This is a heading",
            "###### This is a heading",
        ]

        result = blocks_to_html(input).to_html()

        self.assertEqual(
            result,
            """<div><h2>This is a heading</h2><h4>This is a heading</h4><h6>This is a heading</h6></div>"""
        )

    def test_blocks_to_html_paragraphs_to_html(self):
        self.maxDiff = None

        input = [
            "This is a paragraph",
            "This is a paragraph",
        ]

        result = blocks_to_html(input).to_html()

        self.assertEqual(
            result,
            """<div><p>This is a paragraph</p><p>This is a paragraph</p></div>"""
        )

    def test_blocks_to_html_ordered_list_to_html(self):
        self.maxDiff = None

        input = [
            "1. This is an ordered list\n2. This is an ordered list",
        ]

        result = blocks_to_html(input).to_html()

        self.assertEqual(
            result,
            """<div><ol><li>This is an ordered list</li><li>This is an ordered list</li></ol></div>"""
        )

    def test_blocks_to_html_unordered_list_to_html(self):
        self.maxDiff = None

        input = [
            "* This is an unordered list\n* This is an unordered list",
        ]

        result = blocks_to_html(input).to_html()

        self.assertEqual(
            result,
            """<div><ul><li>This is an unordered list</li><li>This is an unordered list</li></ul></div>"""
        )

    def test_blocks_to_html_quote_to_html(self):
        self.maxDiff = None

        input = [
            "> This is a quote\n> This is a quote",
        ]

        result = blocks_to_html(input).to_html()

        self.assertEqual(
            result,
            """<div><blockquote><p>This is a quote</p><p>This is a quote</p></blockquote></div>"""
        )

    def test_blocks_to_html_code_to_html(self):
        self.maxDiff = None

        input = [
            """```some_func(args: adsf)
    for thing in args:
        do stuff```""",
        ]

        result = blocks_to_html(input).to_html()

        self.assertEqual(
            result,
            """<div><pre><code>some_func(args: adsf)
    for thing in args:
        do stuff</code></pre></div>"""
        )

    def test_blocks_to_html_all_to_html(self):
        self.maxDiff = None

        input = [
            "## This is a heading",
            "#### This is a heading",
            "###### This is a heading",
            "This is a paragraph",
            "This is a paragraph",
            "1. This is an ordered list\n2. This is an ordered list",
            "* This is an unordered list\n* This is an unordered list",
            "> This is a quote\n> This is a quote",
            """```some_func(args: adsf)
    for thing in args:
        do stuff```""",
        ]

        result = blocks_to_html(input).to_html()

        self.assertEqual(
            result,
            """<div><h2>This is a heading</h2><h4>This is a heading</h4><h6>This is a heading</h6><p>This is a paragraph</p><p>This is a paragraph</p><ol><li>This is an ordered list</li><li>This is an ordered list</li></ol><ul><li>This is an unordered list</li><li>This is an unordered list</li></ul><blockquote><p>This is a quote</p><p>This is a quote</p></blockquote><pre><code>some_func(args: adsf)
    for thing in args:
        do stuff</code></pre></div>"""
        )

#            """<div>
#            <h2>This is a heading</h2>
#            <h4>This is a heading</h4>
#            <h6>This is a heading</h6>
#            <ol>
#                <li>This is an ordered list</li>
#                <li>This is an ordered list</li>
#            </ol>
#            <ul>
#                <li>This is an unordered list</li>
#                <li>This is an unordered list</li>
#            </ul>
#            <blockquote>
#                <p>This is a quote</p>
#                <p>This is a quote</p>
#            </blockquote>
#
#            <pre><code>def some_func(args: adsf):
#    for thing in args:
#        do stuff</code></pre>
#</div>"""

if __name__ == "__main__":
    unittest.main()
