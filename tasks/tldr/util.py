from spacy.training import Example

from spacy_llm.compat import BaseModel, Self


class TldrExample(BaseModel):
    text: str
    summary: str

    @classmethod
    def generate(cls, example: Example, **kwargs) -> Self:
        return cls(
            text=example.reference.text,
            summary=getattr(example.reference._, kwargs["field"]),
        )
