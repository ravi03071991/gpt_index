from llama_index.core.multi_modal_llms.base import MultiModalLLM
from llama_index.multi_modal_llms.mistral import MistralMultiModal


def test_embedding_class():
    names_of_base_classes = [b.__name__ for b in MistralMultiModal.__mro__]
    assert MultiModalLLM.__name__ in names_of_base_classes


def test_init():
    m = MistralMultiModal(max_tokens=400)
    assert m.max_tokens == 400
