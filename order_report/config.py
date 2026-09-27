from dataclasses import dataclass#
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

@dataclass(frozen=True)
class Reportconfig:
    input_path: Path
    output_dir: Path

CONFIG = Reportconfig(
    input_path=BASE_DIR / "data" / "orders.csv",
    output_dir=BASE_DIR / "output",
)


#INPUT_FILE = BASE_DIR / "data" / "orders.csv"
#OUTPUT_FOLDER = BASE_DIR / "output"

