from pathlib import Path

from .context_manager import queryhunter
from .reporting import (
    LoggingOptions,
    PrintingOptions,
    QueryHunterException,
    RaisingOptions,
    ReportingOptions,
    CustomReporterOptions,
    QueryHunterReporter,
)
from .queryhunter import Line


def default_base_dir(file) -> str:
    return str(Path(file).resolve().parent.parent)


__all__ = [
    "queryhunter",
    "LoggingOptions",
    "PrintingOptions",
    "RaisingOptions",
    "ReportingOptions",
    "CustomReporterOptions",
    "QueryHunterReporter",
    "Line",
    "QueryHunterException",
    "default_base_dir",
]
