from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


def _load():
    path = Path(__file__).resolve().parents[1] / 'scripts' / 'summarize_wagner_eps_paths_0072.py'
    spec = spec_from_file_location('wagner_eps_0072', path)
    mod = module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def test_tokenizer_ignores_comment_letters_and_embedded_text():
    mod = _load()
    text = '''
%%Creator: Graphic data from GRAF (M L C SN should not execute)
/Label (LLR Moscow Creator) def
0.000 0.000 0.000 C 7.931 1.844 M 8.931 2.844 L SN
0.011 SL % C M L SN in trailing comment
'''
    assert mod.tokenize_eps(text) == [
        '0.000', '0.000', '0.000', 'C',
        '7.931', '1.844', 'M',
        '8.931', '2.844', 'L', 'SN',
        '0.011', 'SL',
    ]


def test_tokenizer_requires_complete_operator_tokens():
    mod = _load()
    text = 'Creator Mx xL CSN 1 2 M 3 4 L SN\n'
    assert mod.tokenize_eps(text) == ['1', '2', 'M', '3', '4', 'L', 'SN']
