from typing import List, Tuple, AnyStr, Any
from click import File
import re


class TableReader:
    @staticmethod
    def read(table_file: File) -> list[tuple[str | Any, ...]]:
        return [tuple(re.split(r'\s+\|\s+', line.strip())) for line in table_file]

