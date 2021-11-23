def collect():
    from time import sleep
    import subprocess
    #import goahead
    x=input('type x: ')
    x=str(x)
    y=input('type y: ')
    y=str(y)
    c=0
    ip1='9C:A5:C0:03:AD:6C'
    ip2='70:F8:2B:B5:21:B1'
    ip3='70:F8:2B:B5:21:B0'
    for i in range(10):
            cells=[]
            #subprocess.Popen(["nmcli","d","wifi","connect","test","password","gbu134265"])
            Process=subprocess.Popen(["iwlist","wlan1","scan"],stdout=subprocess.PIPE,universal_newlines=True)
            out,err=Process.communicate()
            new_l=out.split('\n')
            for line in new_l:
                    line=line.lstrip()
                    line=line.rstrip()
                    if line.startswith("Cell"):
                            line1=line.split()
                    #       print line1[4]
                            if line1[4]== ip1 or line1[4]==ip2 or line1[4]==ip3:
                                    cells.append(line1[4])
                    
                    if line.startswith("ESSID") and (line1[4]==ip1 or line1[4]==ip2 or line1[4]==ip3):
                            line2=line.split(":")
                    #       print line2[1]
                            cells.append(line2[1])
                    if line.startswith("Quality") and (line1[4]==ip1 or line1[4]==ip2 or line1[4]==ip3):
                            line5=line.split()
                            #line6=line.split(' ')
                            #line5=line.split("=")
                            line6=line5[2].split("=")
                    #       print line6[1]
                            cells.append(line6[1])
            cells.reverse()
            #print(cells)
            #print(cells, file=open("output3.txt", "a"))
            file = open("train.txt", "a")
            for index in range(len(cells)):
                if c==0:
                    file.write(str(cells[1]) + "\t" + str(cells[4])+ "\t"+str(cells[7])+ "\t"+"x position"+ "\t"+ "y position"+ "\n")
                    file.write(str(cells[0].split("/")[0]) + "\t" + str(cells[3].split("/")[0])+ "\t"+str(cells[6].split("/")[0])+"\t"+x+"\t"+y+"\t"+ "\n")
                    c+=1
                else:
                    file.write(str(cells[0].split("/")[0]) + "\t" + str(cells[3].split("/")[0])+ "\t"+str(cells[6].split("/")[0])+"\t"+x+"\t"+y+"\t"+"\n")
            file.close()
            #print(cells)
            sleep(5)


