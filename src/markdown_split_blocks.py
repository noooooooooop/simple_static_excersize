from markdown_blocks_by_code import markdown_blocks_by_code

import re

def markdown_split_blocks(md: str):
    #blocks = markdown_blocks_by_newline(md.split("\n"))

    blocks = [[block] for block in md.split("\n")]

    current_header = "paragraph"
    previous_header = "paragraph"

    for i in range(len(blocks)-1, -1, -1):
        previous_header = current_header
        current_header = "paragraph"

        if blocks[i][0][:2] == "> ":
            current_header = "quote"
        if len(re.findall(r"^[\*-]\s", blocks[i][0])) > 0:
            current_header = "unordered_list"
        if len(re.findall(r"^[0-9][0-9]?[0-9]?\.\s", blocks[i][0])) > 0:
            current_header = "ordered_list"
        if len(re.findall(r"^[#]{0,6}\s", blocks[i][0])) > 0:
            current_header = "heading"
            # headings should be one line per block
            previous_header = ""

        # BUG: not going to work, it skips over blanks, but then merges them
        if blocks[i][0] == "":
            # This check makes sure that paragraphs break up amongst themselves
            current_header = ""
            blocks.pop(i)
            continue

        if previous_header != "" and current_header == previous_header and i < len(blocks) - 1:
            blocks[i].extend(blocks[i+1])
            blocks.pop(i+1)

    blocks = ["\n".join(block).lstrip("\n").rstrip("\n") for block in blocks]

    blocks = markdown_blocks_by_code(blocks)

    blocks = [re.sub(r"^[\s\t]+$", "", block) for block in blocks]

    blocks = [block for block in blocks if block != ""]

    #blocks = markdown_blocks_by_newline(blocks)

    return blocks

def get_block_type(block: str) -> str:
    if len(re.findall(r"^[#]{0,6} ", block)) > 0: return "heading"

    if block[:2] == "* ": return "unordered_list"

    if len(re.findall(r"^[0-9][0-9]?[0-9]?. ", block)) > 0: return "ordered_list"

    if len(re.findall(r"```", block)) > 0: return "code"

    if block[:2] == "> ": return "quote"

    return "paragraph"
