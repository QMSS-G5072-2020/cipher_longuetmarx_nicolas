
import pytest

def cipher(text, shift, encrypt=True):
    alphabet = 'abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWYZ'
    new_text = ''
    if (isinstance(shiftarror('Only works with non string shifters.')
    else:
        for c in text:
            index = alphabet.find(c)
            if index == -1:
                new_text += c
            else:
                new_index = index + shift if encrypt == True else index - shift
                new_index %= len(alphabet)
                new_text += alphabet[new_index:new_index+1]
        return new_text

def test_cipher_first():
    example="veni"
    expected='ygpk'
    actual = cipher(example, 2)
    assert actual == expected
test_cipher_first()

def test_cipher_second():
    example=-2
    expected='tgbg'
    actual = cipher('vidi', example)
    assert actual == expected
test_cipher_second()

def test_cipher_third():
    example='@€$'
    expected='@€$'
    actual = cipher(example, 2)
    assert actual == expected
test_cipher_third()

def test_cipher_four():
        with pytest.raises(AssertionError):
            cipher('vici', two)
test_cipher_four()

