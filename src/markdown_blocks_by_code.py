from typing import List

def markdown_blocks_by_code(md: str | List[str]) -> List[str]:
    if type(md) == str:
        return __markdown_blocks_by_code(md)
    else:
        blocks = []

        for i in range(0, len(md)):
            blocks.extend(__markdown_blocks_by_code(md[i]))

        return blocks

def __markdown_blocks_by_code(md: str) -> List[str]:
    blocks = md.replace("\n```", "```").replace("```\n", "```").split("```")

    for i in range(1, len(blocks), 2):
        blocks[i] = f"```{blocks[i]}```"

    return blocks
