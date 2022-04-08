#Crowley Interpreter Build 0.1
import func
print("Crowley Interpreter Build 0.1 [version1/april08.2022]")
vars = {}
while True:
    cmd = input("[I] ")
    args = cmd.split()
    try:
        func.exec(args)
    except:
        error = 'Invalid Input'
        print("[O] Error: " + error)

        
