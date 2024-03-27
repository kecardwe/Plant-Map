start = int(input("Start Position: "))
end = int(input("End Position: "))
x=0
listofletter=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "aa", "ab", "ac", "ad", "ae", "af", "ag", "ah", "ai", "aj", "ak", "al", "am", "an", "ao", "ap", "aq", "ar", "as", "at", "au", "av", "aw", "ax", "ay", "az", "ba", "bb", "bc", "bd", "be", "bf", "bg", "bh", "bi", "bj", "bk", "bl", "bm", "bn", "bo", "bp", "bq", "br", "bs", "bt", "bu", "bv", "bw", "bx", "by", "bz"]
with open ("HTML_Part.txt","w") as output:
    output.write("<body>\n")
    while start != end+1:
        output.write("       <div id=\"%s\">\n"%listofletter[x])
        output.write("        <a href =\"Computer%d.html\" font=\"5\">\n"%start)
        output.write("            %d.\n"%start)
        output.write("        </a>\n")
        output.write("       </div>\n")
        x=x+1
        start=start+1
    output.write("</body>\n")
    output.write("</html>")
    
