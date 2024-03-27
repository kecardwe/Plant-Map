num_computers=0


with open('output.txt','r') as file:
    data=file.readlines()
 
    print(data)
    with open('fixed.txt','a') as fixed:
          fixed.write('NetID/UserName\n')
    counter=0
    for i in data:
          keyword=str('NetID/UserName')
          counter=counter+1
          if keyword in i and 'echo' not in i:
              with open('fixed.txt','a') as fixed:
                  fixed.write(data[counter])
                  num_computers=num_computers+1
                  fixed.close()
    with open('fixed.txt','a') as fixed:
          fixed.write('\n')
          fixed.write('Hostname\n')
    counter=0
    for i in data:
          keyword=str('Hostname/SerialNumber')
          counter=counter+1
          if keyword in i and 'echo' not in i:
                  with open('fixed.txt','a') as fixed:
                      fixed.write(data[counter])
                      num_computers=num_computers+1
                      fixed.close()
    with open('fixed.txt','a') as fixed:
          fixed.write('\n')
          fixed.write('S e r i a l N u m b e r\n')
    counter=0
    for i in data:
          keyword=str('S e r i a l N u m b e r')
          counter=counter+1
          if keyword in i:
              with open('fixed.txt','a') as fixed:
                  fixed.write(data[counter+1])
                  num_computers=num_computers+1
                  fixed.close()
    with open('fixed.txt','a') as fixed:
          fixed.write('\n')
          fixed.write('M a n u f a c t u r e r\n')
    counter=0
    for i in data:
          keyword=str('M a n u f a c t u r e r')
          counter=counter+1
          if keyword in i:
              with open('fixed.txt','a') as fixed:
                  fixed.write(data[counter+1])
                  num_computers=num_computers+1
                  fixed.close()
    with open('fixed.txt','a') as fixed:
          fixed.write('\n')          
          fixed.write('M o d e l\n')
    counter=0
    for i in data:
          keyword=str('M o d e l')
          counter=counter+1
          if keyword in i and ' I n s p i r o n' not in i:
              with open('fixed.txt','a') as fixed:
                  fixed.write(data[counter+1])
                  num_computers=num_computers+1
                  fixed.close()
    with open('fixed.txt','a') as fixed:
          fixed.write('\n')
          fixed.write('MAC Address\n')
    for i in data:
          keyword=str('Physical Address')
          if keyword in i and '-E0' not in i:
              with open('fixed.txt','a') as fixed:
                  fixed.write(i[39:len(i)])
                  num_computers=num_computers+1
                  fixed.close()
    with open('fixed.txt','a') as fixed:
         fixed.write('\n')
         fixed.write('IP Address\n')
    for i in data:
         keyword=str('IPv4 Address')
         if keyword in i and 'Link-local' not in i and 'Autoconfiguration' not in i:
             with open('fixed.txt','a') as fixed:
                 fixed.write(i[39:len(i)])
                 num_computers=num_computers+1
                 fixed.close() 
    with open('fixed.txt','a') as fixed:
          fixed.write('\n')          
          fixed.write('Operating System\n')
    counter=0
    for i in data:
          keyword=str('----------------------------------------------')
          counter=counter+1
          if keyword in i and 'echo' not in i:
              with open('fixed.txt','a') as fixed:
                  fixed.write(data[counter-2])
                  num_computers=num_computers+1
                  fixed.close()
    with open('fixed.txt','a') as fixed:
         fixed.write('\n')
         fixed.write('Tanium?\n')
    counter=0
    for i in data:
        keyword=str('Tanium')
        counter=counter+1
        if keyword in i and 'echo' not in i and 'tasklist' not in i:
            check=data[counter]
            if 'Windows' in check:
                break
            else:
                with open('fixed.txt','a') as fixed:
                    fixed.write('Yes\n')
                    num_computers=num_computers+1
    num_computers=num_computers/9

