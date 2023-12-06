# create the best isEven implementation


out = open("even.c", "w")

out.write("int isEven(int input) {\n")

for i in range(-100000000,100000000):
    line = f"\tif (input == {i}) " + "{ \n\t\treturn "
    if i % 2 == 0: 
        line += "1;\n\t}\n"
    else: 
        line += "0;\n\t}\n"
    out.write(line)
out.write("}\n")