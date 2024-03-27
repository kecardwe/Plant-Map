with open ("Update_Tools\KMS_Computer_Inventory_Work.csv","r") as file:
    with open ("Updates.txt","w") as output:
        file.readline()
        data=file.readlines()
        inp=int(input("Input number of computers added: "))
        y=len(data)-inp
        x=len(data)-inp
        output.write("Section 1\n\n")
        while y != len(data):
            y=y+1
            output.write("    <a href =\"Computer_Webpages\Computer%d.html\" font=\"5\" id=\"link%d\">\n"%(y,y))
            output.write("    </a>\n")
        output.write("\n")
        output.write("Section 2\n\n")
        while inp != 0:      
            strofitems=data[x].split(",")
            x=x+1
            output.write("        if (search ==\"%d\") {\n"%x)
            output.write("        document.getElementById(\"link%d\").innerHTML=\n"%x)
            output.write("        \"Computer %d\";\n"%x)
            output.write("        }\n")
            
            output.write("        if (search ==\"%s\") {\n"%strofitems[1])
            output.write("        document.getElementById(\"link%d\").innerHTML=\n"%x)
            output.write("        \"Computer %d\";\n"%x)
            output.write("        }\n")
            ips=strofitems[8]
            if len(ips)==0:
                next
            else:
                ip=("")
                for i in ips:
                    if i=="|":
                        output.write("        if (search ==\"%s\") {\n"%ip)
                        output.write("        document.getElementById(\"link%d\").innerHTML=\n"%x)
                        output.write("        \"Computer %d\";\n"%x)
                        output.write("        }\n")
                        ip=("")
                    else:
                        ip=ip+i
                output.write("        if (search ==\"%s\") {\n"%ip)
                output.write("        document.getElementById(\"link%d\").innerHTML=\n"%x)
                output.write("        \"Computer %d\";\n"%x)
                output.write("        }\n")
            
            macs=strofitems[9]
            if len(macs)==0:
                next
            else:
                mac=("")
                for i in macs:
                    if i=="|":
                        output.write("        if (search ==\"%s\") {\n"%mac)
                        output.write("        document.getElementById(\"link%d\").innerHTML=\n"%x)
                        output.write("        \"Computer %d\";\n"%x)
                        output.write("        }\n")
                        mac=("")
                    else:
                        mac=mac+i
                lastmac=mac[0:len(mac)-1]
                output.write("        if (search ==\"%s\") {\n"%lastmac)
                output.write("        document.getElementById(\"link%d\").innerHTML=\n"%x)
                output.write("        \"Computer %d\";\n"%x)
                output.write("        }\n")
            inp=inp-1
                
                
                