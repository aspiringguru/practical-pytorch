#very rough, ugly cleanup tool
#finds int on line by itself, strips lineself.
#strips blank lines

filepath_in = 'shakespear_sonnets.txt'
filepath_out = 'shakespear_sonnets_out.txt'

stop_point = 20
count = 0

with open(filepath_out, 'w') as f:

    with open(filepath_in) as fp:
       line = fp.readline()
       print (count, ":", line)
       if len(line) >1: f.write(line+"\n")
       count += 1
       while line:
           line = fp.readline()
           if len(line) >1: line = line.strip()#strip leading and trailing spaces
           print (count, ":'", line, "'", len(line))
           try:
               print (int(line)) #print int
               print ("was able to convert to int.")
               line = fp.readline()
           except Exception as e:
               print (e)
               print (count, ":", line)
               if len(line) >1: f.write(line+"\n")

           count += 1
           #if count >= stop_point:
            #   break


f.close()
