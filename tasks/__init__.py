from spacy import Language

from spacy_llm.pipeline.llm import DEFAULT_CACHE_CONFIG, DEFAULT_MODEL_CONFIG, DEFAULT_SAVE_IO
from spacy_llm.pipeline.llm import DEFAULT_VALIDATE_TYPES, make_llm
from .tldr import TldrTask, make_tldr_task

_LATEST_TASKS = (
    "tasks.Tldr.v1"
)

# Register llm_TASK factories with default models.
for task_handle in _LATEST_TASKS:
    Language.factory(
        name=f"llm_{task_handle.split('.')[1].lower()}",
        default_config={
            "task": {"@llm_tasks": task_handle},
            "model": DEFAULT_MODEL_CONFIG,
            "cache": DEFAULT_CACHE_CONFIG,
            "save_io": DEFAULT_SAVE_IO,
            "validate_types": DEFAULT_VALIDATE_TYPES,
        },
        func=make_llm,
    )

__all__ = [
    "make_tldr_task",
    "TldrTask",
]
