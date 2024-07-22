from src.generators.pager import mini_pager


def test_pager_returns_10_lines():
    minipager = mini_pager('../data.txt')
    assert len(next(minipager).split('\n')) == 10

def test_pager_returns_30_lines_with_3_iterations():
    minipager = mini_pager('../data.txt')
    text = ''
    text += next(minipager)
    text += next(minipager)
    text += next(minipager)
    assert text.count('\n') == 30


