with open ("KMS_Computer_Inventory_Work.csv","r") as input:
    input.readline()
    data=input.readlines()
    t=0
    x=0
    y=1548
    for i in data:      
        strofitems=data[x].split(",")
        y=y+1
        while t==0:
            if y==1623 or y==1625 or y==1626 or y==1627 or y==1628 or y==1629 or y==1630 or y==1652 or y==1675 or y==1686 or y==1724 or y==1844 or y==1894 or y==1895 or y==1905 or y==1922:
                y=y+1
            else:
                x=x+1
                with open ("Computer%d.html"%x,"w") as output:
                    output.write("<html>\n")
                    output.write("    <head>\n")
                    output.write("        <meta charset=\"utf-8\">\n")
                    output.write("        <title>www.Computer_%d.com</title>\n"%x)
                    output.write("        <p><b><u>Computer %d</u></b></p>\n"%x)
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
                    if strofitems[2] == "LEB":
                        output.write("            <b>Location: </b><a href=\"..\Section_Webpages\LEB.html\">%s</a><br>\n"%(strofitems[2]))
                    if strofitems[2] == "Daimler Test":
                        output.write("            <b>Location: </b><a href=\"..\Section_Webpages\Daimler_Test.html\">%s</a><br>\n"%(strofitems[2]))
                    if strofitems[2] == "Heatsink":
                        output.write("            <b>Location: </b><a href=\"..\Section_Webpages\Heatsink.html\">%s</a><br>\n"%(strofitems[2]))
                    if strofitems[2] == "Daimler FA":
                        output.write("            <b>Location: </b><a href=\"..\Section_Webpages\Daimler_FA.html\">%s</a><br>\n"%(strofitems[2]))
                    if strofitems[2] == "Daimler Sub":
                        output.write("            <b>Location: </b><a href=\"..\Section_Webpages\Daimler_Sub.html\">%s</a><br>\n"%(strofitems[2]))
                    if strofitems[2] == "Conformal Coat":
                        output.write("            <b>Location: </b><a href=\"..\Section_Webpages\Conformal_Coat.html\">%s</a><br>\n"%(strofitems[2]))
                    if strofitems[2] == "Handplace West":
                        output.write("            <b>Location: </b><a href=\"..\Section_Webpages\HandPlaceWest.html\">%s</a><br>\n"%(strofitems[2]))
                    if strofitems[2] == "Handplace East":
                        output.write("            <b>Location: </b><a href=\"..\Section_Webpages\HandPlaceEast.html\">%s</a><br>\n"%(strofitems[2]))
                    if strofitems[2] == "SMT West":
                        output.write("            <b>Location: </b><a href=\"..\Section_Webpages\SurfaceMountWest.html\">%s</a><br>\n"%(strofitems[2]))
                    if strofitems[2] == "SMT East":
                        output.write("            <b>Location: </b><a href=\"..\Section_Webpages\SurfaceMountEast.html\">%s</a><br>\n"%(strofitems[2]))
                    if strofitems[2] == "Pack/FSW":
                        output.write("            <b>Location: </b><a href=\"..\Section_Webpages\Pack-FSW.html\">%s</a><br>\n"%(strofitems[2]))
                    if strofitems[2] == "Repair":
                        output.write("            <b>Location: </b><a href=\"..\Section_Webpages\Repair.html\">%s</a><br>\n"%(strofitems[2]))
                    if strofitems[2] == "CPE Lab":
                        output.write("            <b>Location: </b><a href=\"..\Section_Webpages\CPE_Lab.html\">%s</a><br>\n"%(strofitems[2]))
                    if strofitems[2] == "FIP/TO220":
                        output.write("            <b>Location: </b><a href=\"..\Section_Webpages\FIP-TO220.html\">%s</a><br>\n"%(strofitems[2]))
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
                    output.write("        <p><a href=\"../Homepage (click me).html\">Homepage</a></p>\n")
                    output.write("        <img src=\"../Images/IMG_%d.JPG\">"%y)
                    output.write("    </body>\n")
                    output.write("</html>\n")
                    break
    
        
    
        