from typing import List
from pathlib import Path


class Parser:
    extensions: List[str] = []

    def validate_extension(self, extension):
        for ex in self.extensions:
            if ex == extension:
                return True
            else:
                return False

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

