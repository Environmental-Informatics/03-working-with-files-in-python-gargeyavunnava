import math as m

def list_mean(l):
    numerator=0
    for i in range(len(l)):
        numerator += l[i]
    mean = numerator/len(l)
    return mean

def list_cumulative_sum(l):
    cumulative_sum_list = [0]*len(l)
    cumul_sum = 0
    for i in range(len(l)):
        cumul_sum += l[i]
        cumulative_sum_list[i] = cumul_sum     
    return cumulative_sum_list

def calculate_dist(lx,ly):
    subseq_dist_list = [None]*(len(lx)-1)
    for i in range(len(subseq_dist_list)):
        dist = m.sqrt( (lx[i]-lx[i+1])**2 + (ly[i]-ly[i+1])**2) 
        subseq_dist_list[i] = dist
    return subseq_dist_list

def list_elements_to_float(l):
    return list(map(float,l))

def list_elements_to_int(l):
    l = list_elements_to_float(l)
    return list(map(int,l))

#Section 1
file1 = open('2008Male00006.txt', 'r') 
lines = file1.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].split(',')
    lines[i][-1] = lines[i][-1].strip('\n')

#Section 2
cnt=0
for sublist in lines:
    if len(sublist) != 15:
        last_line = sublist
        lines.pop(cnt)
    cnt=cnt+1

keys = lines[0]
lines[:] = lines[1:]

#Section 3
dic = {}
for i in range(len(lines[0])):
    dic[keys[i]] = []
    for sublist in lines:
        tmp=sublist[i]
        dic[keys[i]].append(tmp)
        
convert_functions = [list_elements_to_float, list_elements_to_int] #storing functions in list to make them easy to call

#Section 4
float_keys = [4,5,8,9,10,11,12,13,14]
int_keys = [3]
key_type = [float_keys,int_keys]

for j in range(len(key_type)):
    typecasted_lists = []
    key_as_str_lists = []
    for i in range(len(key_type[j])):
        key_as_str_lists.append(dic[keys[key_type[j][i]]])
    tmp = map(convert_functions[j], key_as_str_lists)
    typecasted_lists+= list(tmp)
    for i in range(len(key_type[j])):
        dic[keys[key_type[j][i]]] = typecasted_lists[i]

#Section 5        
dic['Distance'] = [0] + calculate_dist(dic[' X'],dic[' Y'])
dic['Distance traveled'] = list_cumulative_sum(dic['Distance'])

#Section 6
f = open("Georges_life.txt","w+")

f.write('Raccoon name: George '+ str(dic['George #'][0]) + '\n')
f.write('Average Location: X=' + str(list_mean(dic[' X'])) + ', Y=' + str(list_mean(dic[' Y'])) + '\n')
f.write('Distance traveled: '+ str(sum(dic['Distance'])) + '\n')
f.write('Average energy level: ' + str(list_mean(dic['Energy Level'])) + '\n')
f.write('Raccoon end state: ' + last_line[0] + '\r\n')
s = '\t'
f.write('Date'+s+'Time'+s+'X'+s+'Y'+s+'Asleep'+s+'Behavior Mode'+s+'Distance traveled'+'\n')
for i in range(len(dic['Time'])):
    f.write(str(dic['Day'][i])+s+str(dic['Time'][i])+s+str(dic[' X'][i])+s+str(dic[' Y'][i])+s+str(dic[' Asleep'][i])+s+str(dic['Behavior Mode'][i])+s+str(dic['Distance traveled'][i])+'\n')
f.close()