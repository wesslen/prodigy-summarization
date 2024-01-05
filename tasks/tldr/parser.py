from typing import Iterable

from spacy.tokens import Doc

from .task import TldrTask


def parse_responses_v1(
    task: TldrTask, docs: Iterable[Doc], responses: Iterable[str]
) -> Iterable[str]:
    """Parses LLM responses for spacy.Tldr.v1.
    task (TldrTask): Task instance.
    docs (Iterable[Doc]): Corresponding Doc instances.
    responses (Iterable[str]): LLM responses.
    RETURNS (Iterable[str]): Summary per doc/response.
    """
    for prompt_response in responses:
        yield prompt_response.replace("'''", "").strip()
