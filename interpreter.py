import sys

program = open(sys.argv[1]).read().replace(" ","").replace("\n","")
statements = program.split(";")
vars={}
def subprogram(p):
    c=0
    if p[0]=="x":
        var=""
        c+=1
        while p[c] in "1234567890":
            var=var+p[c]
            c+=1
        var=int(var)
        if p[c:c+2]=="++":
            vars[var]=vars.get(var,0)+1
            c+=2
        elif p[c:c+3]==":=x":
            c+=3
            rightvar=""
            while p[c] in "1234567890":
                rightvar=rightvar+p[c]
                c+=1
            rightvar=int(rightvar)
            vars[var]=vars[rightvar]
    elif p.startswith("LOOPx"):
        var=""
        c+=5
        while p[c] in "1234567890":
            var=var+p[c]
            c+=1
        var=int(var)
        c+=2
        start=c
        nest=1
        while nest>0:
            if p[c:c+3]=="END":
                nest-=1
            elif p[c:c+4]=="LOOP":
                nest+=1
            c+=1
        for i in range(vars[var]):
            subprogram(p[start:c])
    else:
        raise Exception("some kind of syntax error")
    if len(p)>c and p[c]==";":
        subprogram(p[c+1:])
subprogram(program)
print vars.get(0,0)
