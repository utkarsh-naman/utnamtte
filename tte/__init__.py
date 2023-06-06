
def tte(expd):

    import math
    exp = str(expd)
    exp = exp.lower()
    exp = exp.replace(" ", "")
    exp = exp.replace("÷", "/")
    exp = exp.replace("×", "*")
    exp = exp.replace("math.pi", "π")
    exp = exp.replace("math.e", "e")
    exp = exp.replace("pi", "π")
    exp = exp.replace("{", "(")
    exp = exp.replace("}", ")")
    exp = exp.replace("<", "(")
    exp = exp.replace(">", ")")
    exp = exp.replace("sqrt", "√")
    exp = exp.replace("math.sqrt", "√")

    exp = exp.replace("log", "math.log")
    exp = exp.replace("ln", "math.log")
    exp = exp.replace("math.math.log", "math.log")
    exp = exp.replace("antimath.log(", "math.pow(")
    exp = exp.replace("plus", "+")
    exp = exp.replace("minus", "-")
    exp = exp.replace("into", "*")
    exp = exp.replace("times", "*")
    exp = exp.replace("multiply", "*")
    exp = exp.replace("multipliedby", "*")
    exp = exp.replace("divide", "/")
    exp = exp.replace("dividedby", "/")
    exp = exp.replace("%", "%")
    exp = exp.replace("⁽", "^(")
    exp = exp.replace("⁺", "+")
    exp = exp.replace("⁻", "-")
    exp = exp.replace("⁾", ")")
    exp = exp.replace("⁽¹⁾", "^(1)")
    exp = exp.replace("⁽½⁾", "^(1)")
    exp = exp.replace("⁽⅓⁾", "^(1/3)")
    exp = exp.replace("⁽¼⁾", "^(1/4)")
    exp = exp.replace("⁽⅛⁾", "^(1/8)")
    exp = exp.replace("⁽²⁾", "^2")
    exp = exp.replace("⁽⅔⁾", "^(2/3)")
    exp = exp.replace("⁽³⁾", "^(3)")
    exp = exp.replace("⁽¾⁾", "^(3/4)")
    exp = exp.replace("⁽⅜⁾", "^(3/8)")
    exp = exp.replace("⁽⁴⁾", "^4")
    exp = exp.replace("⁽⅝⁾", "^(5/8)")
    exp = exp.replace("⁽⅞⁾", "^(7/8)")

    exp = exp.replace("¹", "^1")
    exp = exp.replace("½", "^(1/2)")
    exp = exp.replace("⅓", "^(1/3)")
    exp = exp.replace("¼", "^(1/4)")
    exp = exp.replace("⅛", "^(1/8)")
    exp = exp.replace("²", "^2")
    exp = exp.replace("⅔", "^(2/3)")
    exp = exp.replace("³", "^(3)")
    exp = exp.replace("¾", "^(3/4)")
    exp = exp.replace("⅜", "^(3/8)")
    exp = exp.replace("⁴", "^4")
    exp = exp.replace("⅝", "^(5/8)")
    exp = exp.replace("⅞", "^(7/8)")

    exp = exp.replace("raisedtothepowerof", "^")
    exp = exp.replace("raisedtothepower", "^")
    exp = exp.replace("tothepowerof", "^")
    exp = exp.replace("tothepower", "^")
    exp = exp.replace("squarerootof", "√")
    exp = exp.replace("squareroot", "√")

    exp = exp.replace("squared", "^2")
    exp = exp.replace("square", "^2")
    exp = exp.replace("e^(iπ)", "(-1)")
    exp = exp.replace("e^(i*π)", "(-1)")

    modcount = 0
    ptpk = 0
    while ptpk < len(exp):
        if exp[ptpk] == '|':
            modcount += 1
        ptpk += 1

    if modcount % 2 != 0:
        exp = exp + '|'

    # completing left brackets
    openbrac = 0
    closebrac = 0
    ptp = 0
    while ptp < len(exp):
        if exp[ptp] == '(':
            openbrac += 1
        if exp[ptp] == ')':
            closebrac += 1
        ptp += 1
    if openbrac - closebrac != 0:
        if openbrac > closebrac:
            diff = openbrac - closebrac
            while diff > 0:
                exp = exp + ")"
                diff -= 1
        elif openbrac < closebrac:
            diff = closebrac - openbrac
            while diff > 0:
                exp = "(" + exp
                diff -= 1
    # wrong input in log
    starr = 0
    while starr < len(exp):
        if exp[starr] == 'g' and starr + 1 < len(exp) and exp[starr + 1] in ('+', '-', '/', '*'):
            exp = "ln(-1)"
        starr += 1
    # wrong input in √
    starr2 = 0
    while starr2 < len(exp):
        if exp[starr2] in ('√', 't') and starr2 + 1 < len(exp) and exp[starr2 + 1] in ('-', '/', '*'):
            exp = "ln(-1)"
        starr2 += 1
    if 'log()' in exp:
        exp = "log(0)"
    if '√()' in exp:
        exp = "log(0)"
    if len(exp) > 0 and exp[len(exp) - 1] in ('√', 'g', 't', '+', '-', '/', '%'):
        exp = ""
    # adding mod function
    bruno = 0
    while bruno < len(exp):
        bho = 1
        bhc = 0
        bcc = len(exp)
        if exp[bruno] == "|":
            inmodinc = exp[bruno:len(exp)]
            looper = 1
            while looper < len(exp) and bho != bhc:
                if inmodinc[looper] == "|":
                    bhc = 1
                    bcc = looper
                exp2 = exp[0:bruno] + f"(abs({inmodinc[1:bcc]}))" + inmodinc[bcc + 1:len(inmodinc)]
                exp = exp2
                looper += 1
        bruno += 1

    solo = 0
    while solo < len(exp):
        # to add a * before √
        if exp[solo] == "√":
            if solo > 0 and exp[solo - 1] in (
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "π", "e", ")", "]", "|"):
                exp2 = exp[0:solo] + "*" + exp[solo:len(exp)]
                exp = exp2
        solo += 1
    # for adding a * before [
    kep = 0
    for kep in range(0, len(exp)):
        if exp[kep] == "[":
            if kep > 0 and exp[kep - 1] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "π", "e", ")", "]"):
                exp = exp[0: kep] + "*" + exp[kep:len(exp)]
    # for gif function directly after √
    xg = 0
    while xg < len(exp):
        bopen2 = 1
        bclose2 = 0
        bcp2 = 0
        exp3 = exp
        if exp[xg] == "√" and exp[xg + 1] == "[":
            val2 = exp[exp.index("√") + 1:len(exp)]
            b2 = 1
            while bopen2 != bclose2:
                if val2[b2] == "[":
                    bopen2 = bopen2 + 1
                if val2[b2] == "]":
                    bclose2 = bclose2 + 1
                    bcp2 = val2.index("]")
                b2 = b2 + 1
            exp3 = exp3[0:exp3.index("√")] + f"(math.sqrt{val2[0:bcp2 + 1]})" + val2[bcp2 + 1:len(val2)]
        xg = xg + 1
        exp = exp3

    # to separate log from numbers in root
    nom = 0
    while nom < len(exp):
        if exp[nom] == "m":
            if nom - 1 >= 0 and exp[nom - 1] in (
                    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ")", "π", "e", "]", "|"):
                exp2 = exp[0:nom] + "*" + exp[nom:len(exp)]
                exp = exp2
        nom += 1

    # for adding * sign nefore and after π
    xc = 0
    while xc < len(exp):
        # to add a * before π
        if exp[xc] == "π":
            if xc > 0 and exp[xc - 1] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ")", "e", "]"):
                exp2 = exp[0:xc] + "*" + exp[xc:len(exp)]
                exp = exp2
        # to add a * after π
        if exp[xc] == "π":
            if xc + 1 != len(exp):
                if exp[xc + 1] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "π", "e", "(", "m", "√", "["):
                    exp2 = exp[0:xc + 1] + "*" + exp[xc + 1:len(exp)]
                    exp = exp2
        # to add  a * before e
        if exp[xc] == "e":
            if xc > 0 and exp[xc - 1] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "π", "e", ")", "]"):
                exp2 = exp[0:xc] + "*" + exp[xc:len(exp)]
                exp = exp2
        # to add a * after e
        if exp[xc] == "e":
            if xc + 1 != len(exp):
                if exp[xc + 1] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "π", "e", "(", "m", "√", "["):
                    exp2 = exp[0:xc + 1] + "*" + exp[xc + 1:len(exp)]
                    exp = exp2
        xc = xc + 1
    gz = 0
    while gz < len(exp):
        # for numbers directly written after √
        pss = 0
        sqbase = ""
        if exp[gz] == "√":
            pss = exp.index("√")
            if exp[gz + 1] not in ("(", "["):
                # strcb string containing base
                strcb = exp[gz + 1:len(exp)]
                j = 0
                while j < len(strcb) and strcb[j] not in ("+", "-", "/", "*", ")", "^"):
                    sqbase = strcb[0:j + 1]
                    j = j + 1
                exp2 = exp[0:pss] + f"(math.sqrt({sqbase}))" + strcb[j:len(strcb)]
                exp = exp2
            if exp[gz + 1] in ("["):
                rest = exp[gz:len(exp)]
                jd = 1
                boz = 1
                bcz = 0
                posi = len(rest)
                while boz != bcz:
                    if rest[jd] == "[":
                        boz += 1
                    if rest[jd] == "]":
                        bcz += 1
                        posi = jd
                    jd += 1
                exp2 = exp[0:posi] + f"(math.sqrt({rest[0:posi + 1]}))" + rest[posi:len(rest)]
                exp = exp2
        # for elements in brackets in √
        bopen = 1
        bclose = 0
        bcp = 0
        exp2 = exp
        if exp[gz] == "√" and exp[gz + 1] == "(":
            val = exp[exp.index("√") + 1:len(exp)]
            b = 1
            while bopen != bclose:
                if val[b] == "(":
                    bopen = bopen + 1
                if val[b] == ")":
                    bclose = bclose + 1
                    bcp = val.index(")")
                b = b + 1
            exp2 = exp2[0:exp2.index("√")] + f"(math.sqrt{val[0:bcp + 1]})" + val[bcp + 1:len(val)]
            exp = exp2
        gz = gz + 1

    z1 = 0
    while z1 < len(exp):
        # to add  a * before (
        if exp[z1] == "(":
            if z1 > 0 and exp[z1 - 1] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "π", "e", ")", "]"):
                exp2 = exp[0:z1] + "*" + exp[z1:len(exp)]
                exp = exp2
        # to add a * after )
        if exp[z1] == ")":
            if z1 + 1 != len(exp):
                if exp[z1 + 1] in (
                        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "π", "e", "(", "m", "√", "[", "l"):
                    exp2 = exp[0:z1 + 1] + "*" + exp[z1 + 1:len(exp)]
                    exp = exp2
        z1 = z1 + 1

    # for greatest integer function
    xm = 0
    exp5 = ""
    while xm < len(exp):
        if exp[xm] == "[":
            posgifs = exp.index("[")
            stat = exp[posgifs:len(exp)]
            go = 1
            gc = 0
            xv = 1
            exp4 = ""
            glast = len(stat)
            while xv < len(exp) and go != gc:
                if stat[xv] == "[":
                    go = go + 1
                if stat[xv] == "]":
                    gc = gc + 1
                    glast = xv
                xv = xv + 1
            if len(exp) > 1:
                exp4 = stat[1:glast]
            exp5 = exp.replace(exp[posgifs:posgifs + glast + 1], f"(math.floor({exp4}))")
            exp = exp5
        xm = xm + 1

    # for log with brackets
    ead = "".join(reversed(exp))
    shuru = 0
    while shuru < len(ead):
        if ead[shuru] == "g":
            if shuru > 0 and ead[shuru - 1] == "(":
                tedit = ead[0:shuru]
                beo = 1
                bec = 0
                becpos = 0
                star = len(tedit) - 2
                while beo != bec:
                    if tedit[star] == "(":
                        beo = beo + 1
                    if tedit[star] == ")":
                        bec = bec + 1
                        becpos = star
                    star -= 1
                    exp2 = ead[0:becpos] + ")" + ead[becpos:shuru] + "nl.htam" + "(" + ead[shuru + 8:len(ead)]
                ead = exp2
        shuru += 1
    ead = ead.replace("nl", "gol")
    exp = "".join(reversed(ead))

    # for log without ( ) brackets
    x4 = 0
    while x4 < len(exp):
        if exp[x4] == "g":
            if exp[x4 + 1] != "(":
                posg = exp.index("g")
                strcl = exp[x4 + 1:len(exp)]
                x5 = 0
                while x5 < len(strcl) and strcl[x5] not in ("*", "/", "+", "-", "^"):
                    x5 = x5 + 1
                if strcl[0] != "(":
                    exp2 = exp[0:posg - 7] + "(math.ln" + strcl[0:x5] + ")" + strcl[x5:len(
                        strcl)]  # changing log into ln to hide the letter g of used log and proceed
                    exp = exp2
        x4 = x4 + 1
    exp = exp.replace("ln", "log")

    # apna apna jugaad hai
    utk = 0
    while utk < len(exp):
        if utk > 0:
            if exp[utk] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "π", "e", "m"):
                if exp[utk - 1] == "g":
                    if utk + 1 < len(exp):
                        ext = exp[utk:len(exp)]
                        stop = len(exp)
                        tp = utk
                        while tp < len(exp):
                            if ext[0] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                                if exp[tp] in ("π", "e", "m", "(", "+", "-", "*", "/", "^", "√"):
                                    stop = tp
                                    tp = len(exp)
                            if ext[0] in ("π", "e"):
                                if exp[tp] in (
                                        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "(", "+", "-", "*", "/",
                                        "^", "√"):
                                    stop = tp
                                    tp = len(exp)
                            if ext[0] == "m":
                                if exp[tp] in ("+", "-", "*", "/", "^"):
                                    stop = tp
                                    tp = len(exp)

                            tp = tp + 1
                        exp2 = exp[0:utk] + "(" + exp[utk:stop] + ")" + exp[stop:len(exp)]
                        exp = exp2
                    else:
                        exp2 = exp[0:utk] + "(" + exp[utk:utk + 1] + ")"
                        exp = exp2
        utk = utk + 1

    x = 0
    while x < len(exp):
        # to add a * before √
        if exp[x] == "√":
            if x > 0 and exp[x - 1] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "π", "e", ")", "]", "|"):
                exp2 = exp[0:x] + "*" + exp[x:len(exp)]
                exp = exp2

        x = x + 1
    # combining elements of denominator after / sign in ( )
    x2 = 0
    while x2 < len(exp):
        if exp[x2] == "/":
            if exp[x2 + 1] == "(":
                x2 = len(exp)
            else:
                posdiv = exp.index("/")
                strcd = exp[x2 + 1:len(exp)]
                x3 = 0
                while x3 < len(strcd) and strcd[x3] not in (",", "*", "/", "+", "-"):
                    x3 = x3 + 1
                if strcd[0] != "(":
                    exp2 = exp[0:posdiv] + "÷(" + strcd[0:x3] + ")" + strcd[x3:len(strcd)]
                    exp = exp2
        x2 = x2 + 1
    exp = exp.replace("÷", "/")
    exp = exp.replace("π", "math.pi")
    exp = exp.replace("e", "math.e")
    exp = exp.replace("cos", "math.cos")
    exp = exp.replace("sin", "math.sin")
    exp = exp.replace("tan", "math.tan")
    exp = exp.replace("math.smath.ec", "math.sec")
    exp = exp.replace("math.cosmath.ec", "math.cosec")
    exp = exp.replace("cot", "cot")
    exp = exp.replace("^", "**")

    forzero = 0
    while forzero < len(exp):
        if exp[0] == '0' and 1 < len(exp) and exp[1] in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
            exp = exp[1:len(exp)]
            forzero = 0

        forzero = forzero + 1

    annihilatezero = 0
    while annihilatezero < len(exp):
        if exp[annihilatezero] == '0' and exp[annihilatezero - 1] in (
        '+', '-', '/', '*', '%', '√', '(', ')', '[', ']', '|') and annihilatezero + 1 < len(exp) and exp[
            annihilatezero + 1] in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
            exp = exp[0:annihilatezero] + exp[annihilatezero + 1:len(exp)]
            annihilatezero = 0
        annihilatezero = annihilatezero + 1

    return exp


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, ac