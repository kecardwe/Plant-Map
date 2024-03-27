with open ("Update_Tools\KMS_Computer_Inventory_Work.csv","r") as file:
    file.readline()
    data=file.readlines()
    inp=int(input("Input number of computers added: "))
    y=1564+len(data)-inp
    x=len(data)-inp
    while inp != 0:      
        strofitems=data[x].split(",")
        x=x+1
        y=y+1
        with open ("Computer_Webpages\Computer%d.html"%x,"w") as output:
            output.write("<html>\n")
            output.write("    <head>\n")
            output.write("        <meta charset=\"utf-8\">\n")
            output.write("        <title>www.Computer_%d.com</title>\n"%x)
            output.write("        <p><b><u>Computer %d</u>\n"%x)
            if strofitems[2] == "LEB":
                output.write("        LEB</b></p>\n")
            if strofitems[2] == "Daimler Test":
                output.write("        Daimler Test</b></p>\n")
            if strofitems[2] == "Heatsink":
                output.write("        Heatsink</b></p>\n")
            if strofitems[2] == "Daimler FA":
                output.write("        Daimler FA</b></p>\n")
            if strofitems[2] == "Daimler Sub":
                output.write("        Daimler Sub</b></p>\n")
            if strofitems[2] == "Conformal Coat":
                output.write("        Conformal Coat</b></p>\n")
            if strofitems[2] == "Handplace West":
                output.write("        Handplace West</b></p>\n")
            if strofitems[2] == "Handplace East":
                output.write("        Handplace East</b></p>\n")
            if strofitems[2] == "SMT West":
                output.write("        SMT West</b></p>\n")
            if strofitems[2] == "SMT East":
                output.write("        SMT East</b></p>\n")
            if strofitems[2] == "Pack/FSW":
                output.write("        Pack/FSW</b></p>\n")
            if strofitems[2] == "Repair":
                output.write("        Repair</b></p>\n")
            if strofitems[2] == "CPE Lab":
                output.write("        CPE Lab</b></p>\n")
            if strofitems[2] == "FIP/TO220":
                output.write("        FIP/TO220</b></p>\n")
            output.write("    </head>\n")
            output.write("    <style>\n")
            output.write("        img{\n")
            output.write("            width: 480px;\n")
            output.write("            height: 640px;\n")
            output.write("            margin-top: -200px;\n")
            output.write("            margin-left: 740px;\n")
            output.write("            transform: rotate(0deg);\n")
            output.write("        }\n")
            output.write("    </style>\n")
            output.write("    <body>\n")
            output.write("        <p>\n")
            output.write("            <b>Hostname: </b>%s<br>\n"%strofitems[1])
            output.write("            <b>NetID: </b>%s<br>\n"%strofitems[3])
            output.write("            <b>Serial Number: </b>%s<br>\n"%strofitems[4])
            output.write("            <b>Manufacturer:</b>%s<br>\n"%strofitems[5])
            output.write("            <b>Model: </b>%s<br>\n"%strofitems[6])
            output.write("            <b>Operating System: </b>%s<br>\n"%strofitems[7])
            output.write("            <b>IP Address: </b>%s<br>\n"%strofitems[8])
            if len(strofitems[9]) > 72 and len(strofitems[9]) < 162:
                output.write("            <b>MAC Address: </b>%s<br>%s\n"%(strofitems[9][0:72],strofitems[9][72:len(strofitems[9])]))
            elif len(strofitems[9]) > 162:
                output.write("            <b>MAC Address: </b>%s<br>%s<br>%s\n"%(strofitems[9][0:72],strofitems[9][72:162],strofitems[9][162:len(strofitems[9])]))
            else:
                output.write("            <b>MAC Address: </b>%s<br>\n"%strofitems[9])
            output.write("        </p>\n")
            output.write("        <img src=\"../Images/IMG_%d.JPG\">"%y)
            output.write("    </body>\n")
            output.write("</html>\n")
            inp=inp-1



