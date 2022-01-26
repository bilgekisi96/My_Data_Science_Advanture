"""
Merhaba yeni bir parantez sorusuyla karşınızdayım:sweat_smile:
This problem was asked by Google.
You're given a string consisting solely of (, ), and *. * can represent either a  (, ), or an empty string.
Determine whether the parentheses are balanced.
For example, (()* and (*) are balanced. )*( is not balanced.

"""



def replace_par(text):
    while '()' in text or '*' in text or ',' in text or '.' in text:
        text = text.replace('()', '').replace('*', '').replace(',', '').replace('.', '')
    return text
fin=replace_par("(*)")
print(fin)
if ")(" in fin:print("unbalance")
else:print("balance")



