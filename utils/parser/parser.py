from collections import defaultdict


class Tree(defaultdict):
    def __init__(self):
        super().__init__(Tree)


def tree_to_dict(tree):
    if isinstance(tree, dict):
        return {k: tree_to_dict(v) for k, v in tree.items()}
    return tree


def parse(data: dict) -> dict:
    output = Tree()

    for lesson in data:
        lesson_data = {
            "lecturer": lesson["lecturer"],
            "time_start": lesson["time_start"],
            "time_end": lesson["time_end"],
            "url": lesson["url"],
            "venue": lesson["venue"],
        }
        output[lesson["group"]][lesson["week"]][lesson["day"]][lesson["lesson"]] = lesson_data

    return tree_to_dict(output)

