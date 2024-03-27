with open ("Search_bar_maker.txt","w") as output:
    c=1
    i=0
    x=0
    y=1
    output.write("<button onclick=\"myFunction()\">Search by IP</button>\n")
    while c != 365:
        output.write("<a href =\"Computer_Webpages\Computer%d.html\" font=\"5\" id=\"link%d\">\n"%(c,c))
        output.write("</a>\n")
        c=c+1
    output.write("<script>\n")
    output.write("  function myFunction() {\n")
    output.write("    let search = prompt(\"Enter IP Address\");\n")
    with open ("KMS_Production_Computer_Inventory_SearchBar.csv","r") as input:
        data=input.readlines()
        for i in data:
            strofitems=data[x].split(",")
            last=data[x-1].split(",")
            x=x+1
            output.write("    if (search ==\"%s\") {\n"%strofitems[7])
            if last[1]=="User-PC204" and strofitems[1]=="User-PC204":
                output.write("    document.getElementById(\"link%d\").innerHTML=\n"%y)
                output.write("    \"Computer %d\";\n"%y)
                y=y+1
            elif last[1]=="Computer not Responding" and strofitems[1]=="Computer not Responding":
                output.write("    document.getElementById(\"link%d\").innerHTML=\n"%y)
                output.write("    \"Computer %d\";\n"%y)
                y=y+1
            elif last[1]==strofitems[1]:
                output.write("    document.getElementById(\"link%d\").innerHTML=\n"%y)
                output.write("    \"Computer %d\";\n"%y)
            else:
                output.write("    document.getElementById(\"link%d\").innerHTML=\n"%y)
                output.write("    \"Computer %d\";\n"%y)
                y=y+1
            output.write("    }\n")
    output.write("  }\n")
    output.write("</script>")