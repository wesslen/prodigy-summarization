from typing import Optional, Type

from spacy_llm.registry import registry
from spacy_llm.ty import ExamplesConfigType, FewshotExample, TaskResponseParser
from .parser import parse_responses_v1
from .task import DEFAULT_TLDR_TEMPLATE_V1, TldrTask
from .util import TldrExample


@registry.llm_tasks("tasks.Tldr.v1")
def make_tldr_task(
    template: str = DEFAULT_TLDR_TEMPLATE_V1,
    parse_responses: Optional[TaskResponseParser[TldrTask]] = None,
    prompt_example_type: Optional[Type[FewshotExample]] = None,
    examples: ExamplesConfigType = None,
    max_n_words: Optional[int] = None,
    field: str = "summary",
):
    """Tldr.v1 task factory.

    template (str): Prompt template passed to the model.
    parse_responses (Optional[TaskResponseParser[TldrTask]]): Callable for parsing LLM responses for
        this task.
    prompt_example_type (Optional[Type[FewshotExample]]): Type to use for fewshot examples.
    examples (Optional[Callable[[], Iterable[Any]]]): Optional callable that reads a file containing task examples for
        few-shot learning. If None is passed, then zero-shot learning will be used.
    max_n_words (int): Max. number of words to use in summary.
    field (str): The name of the doc extension in which to store the summary.
    """
    raw_examples = examples() if callable(examples) else examples
    example_type = prompt_example_type or TldrExample
    span_examples = (
        [example_type(**eg) for eg in raw_examples] if raw_examples else None
    )

    return TldrTask(
        template=template,
        parse_responses=parse_responses or parse_responses_v1,
        prompt_example_type=example_type,
        prompt_examples=span_examples,
        max_n_words=max_n_words,
        field=field,
    )
