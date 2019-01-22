import unicodedata

# also from Stack Overflow
def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

def test_remove():
    all_ok = True
    all_ok &= "Ooster" == remove_accents("Ööstèr")
    return all_ok

assert test_remove() == True
