import logging
from pathlib import Path
import pandas as pd

logger = logging.getLogger(__name__)

def load_orders(file_path: Path) -> pd.DataFrame:

    logger.info("Läser in orderdata från %s", file_path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"Filen kunde inte hittas: {file_path}"
        )

    data = pd.read_csv(file_path)

    logger.info("Läste in %s rader", len(data))

    return data