#!/usr/bin/env python

import sys

from preprocessor import Preprocessor
from processor import Processor


def main() -> int:
    """
    Main entry point of the program.
    """
    mmdata_path: str = "input/mmdata.json"

    pp: Preprocessor = Preprocessor(mmdata_path)

    pp.load_all()

    p: Processor = Processor()

    p.calc_team_graph(pp)

    return 0


if __name__ == "__main__":
    sys.exit(main())
