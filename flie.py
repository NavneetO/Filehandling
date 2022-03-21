file=open("Multitable.txt","w")
for i in range(1,11):
    h=i*2
    file.write(str(i))
    file.write("x2 =")
    file.write( str(h) )
    file.write('\n')
file.close()