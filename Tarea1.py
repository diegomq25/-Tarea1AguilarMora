def check_char(charr):
    if isinstance(charr, str):
        if len(charr) == 1:
            if(charr.isalpha() == 1):
                return 0
            else:
                return("ERROR: NO ES UN CARACTER EN RANGO A-Z")
        else:
            return ("ERROR:CADENA MUY EXTENSA")
    else:
        return ("ERROR: CARACTER NO ES STRING")


def caps_switch(charr):
    if check_char(charr) == 0:
        return charr.swapcase()
    else:
        return check_char(charr)
