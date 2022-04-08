#Crowley Interpreter Functions Dictionary
funcs = ["echo {string}","sum <add/sub> {float} {float}","store <varname> {value}","help"]
sto = {}
def exec(args):
    if(args[0] == "echo"):
        print("[O] " + args[1])
    if(args[0] == "sum"):
        val1=0
        val2=0
        #if(args[1] == "add"):
        #    print(float(args[2]) + float(args[3]))
        #if(args[1] == "sub"):
        #    print(float(args[2]) - float(args[3]))
        try:
            val1=float(args[2])
        except:
            val1=sto[str(args[2])]
        try:
            val2=float(args[3])
        except:
            val2=sto[str(args[3])]
        if(args[1] == "add"):
            print(float(val1) + float(val2))
        if(args[1] == "sub"):
            print(float(val1) - float(val2))   
    if(args[0] == "store"):
        sto[args[1]] = args[2]
    if(args[0] == "help"):
        for i in range(len(funcs)):
            print(funcs[i])
        
    
