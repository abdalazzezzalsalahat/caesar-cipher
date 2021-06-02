from caesar_cipher import *

def test_encrypt():

    txt = 'good morning, Im azooz and Im here to make you wish that you are dead :)'
    actual = encrypt(txt, 10)
    assert actual == 'qyyn wybxsxq, sw kjyyj kxn sw robo dy wkuo iye gscr drkd iye kbo nokn :)'

def test_decrypt():

    txt='James this is Martin, Martin this is James'
    key = 42
    actual = decrypt(encrypt(txt, key), key)
    assert actual == 'james this is martin, martin this is james'

def test_edge_case():

    txt = 'kill everypone and run.'
    key = 6
    actual = encrypt(txt, key)
    assert actual == 'qorr kbkxevutk gtj xat.'

def test_encrypt_sentence_text():

    txt = '''for all the love and care that we give who\'s around us, and what do we get in return, we get appandened, all blame is on you, they talk about you behind your back as it is your fault just because they are not grown enough to take their own responsibility and for no reason you find your self alone.'''
    enc_txt = '''sbe nyy gur ybir naq pner gung jr tvir jub'f nebhaq hf, naq jung qb jr trg va erghea, jr trg nccnaqrarq, nyy oynzr vf ba lbh, gurl gnyx nobhg lbh oruvaq lbhe onpx nf vg vf lbhe snhyg whfg orpnhfr gurl ner abg tebja rabhtu gb gnxr gurve bja erfcbafvovyvgl naq sbe ab ernfba lbh svaq lbhe frys nybar.'''
    assert encrypt(txt, 13) == enc_txt

def test_decrypt_sentence():
    
    enc_txt = '''sbe nyy gur ybir naq pner gung jr tvir jub'f nebhaq hf, naq jung qb jr trg va erghea, jr trg nccnaqrarq, nyy oynzr vf ba lbh, gurl gnyx nobhg lbh oruvaq lbhe onpx nf vg vf lbhe snhyg whfg orpnhfr gurl ner abg tebja rabhtu gb gnxr gurve bja erfcbafvovyvgl naq sbe ab ernfba lbh svaq lbhe frys nybar.'''
    denc_txt = '''for all the love and care that we give who\'s around us, and what do we get in return, we get appandened, all blame is on you, they talk about you behind your back as it is your fault just because they are not grown enough to take their own responsibility and for no reason you find your self alone.'''
    assert decrypt(enc_txt, 13) == denc_txt

def test_not_english():

  assert break_it('lkajsduncaw oiasndlj n udnslj ijso adivusi vaj oisajd aj jj kj zsdoj a oj sadvvjuna o') == 'Not English'

def test_break_it_text():

  text = 'All times are good but there must be some bad days that you have to live in them.'
  cipher = encrypt(text, 25)
  assert break_it(cipher) == text.lower()

def test_words_count_long_sentance():

    text = "this is a test text and I can say whatever I want to say, like hbaskh jsbdiu ijsbdi ijs ijsdhb and no one cares."
    assert counter(text) == 17

def test_words_countshort_sentance():
    
    text = "This is a test text js ijsdhb whatever."
    assert counter(text) == 5


