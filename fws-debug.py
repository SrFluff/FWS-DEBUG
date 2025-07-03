import os
doc = []
if os.path.exists("log.eff"):
    f = open("log.eff", "r")
    for line in f:
        doc.append(line[0:-1])
else:
    print("No log.eff file present")
    exit()
i = 0
while i < len(doc):
    if doc[i] == "a1":
        print("[" + str(i) + "] Integer pushed")
    elif doc[i] == "a2":
        print("[" + str(i) + "] String pushed")
    elif doc[i] == "a3":
        print("[" + str(i) + "] Random number pushed")
    elif doc[i] == "a4":
        print("[" + str(i) + "] Arithmetic operation pushed")
    elif doc[i] == "b0":
        print("[" + str(i) + "] Value retrieved from stack")
    elif doc[i] == "c1":
        print("[" + str(i) + "] Jump if equal")
    elif doc[i] == "c2":
        print("[" + str(i) + "] Jump if not equal")
    elif doc[i] == "c3":
        print("[" + str(i) + "] Jump if less than")
    elif doc[i] == "d0":
        print("[" + str(i) + "] Exit called")
    elif doc[i] == "e0":
        print("[" + str(i) + "] Stack item popped")
    elif doc[i] == "f0":
        print("[" + str(i) + "] Stack items swapped")
    i += 1