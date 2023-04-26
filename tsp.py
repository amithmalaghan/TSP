import math 
import random
import itertools
import json


def distance(a,b):
    c = ((b[0]-a[0])**2) + ((b[1]-a[1])**2)
    return round(math.sqrt(c),2)

def total_distance(distance_list):
    total_dist = distance(data[distance_list[0]],data[distance_list[len(distance_list)-1]])
    #total_dist = 0.0
    for x in range(0,len(distance_list)-1):
        j = distance(data[distance_list[x]],data[distance_list[x+1]])
        total_dist = total_dist + j
    return total_dist
def distance_three(a):
    if v.index(a) == 0:
        return distance(data[a],data[v[1]])
    elif v.index(a) == (len(v)-1):
        return distance(data[a],data[v[len(v)-2]])
    else:
        ind = v.index(a)
        return distance(data[a],data[v[ind-1]]) + distance(data[a],data[v[ind+1]])

def swapPositions(list, pos1, pos2):
     
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def my_tsp(v):
    tem = 0
    temp_list = []
    min_distance = total_distance(v)
    for x in range(1,len(v)):
        #SIM = []
        for y in range(1,len(v)):
            if x == y:
                continue
        #print("----",x,y)
            tem = tem + 1 
            cop = v.copy()
            swap_list = swapPositions(cop, x, y)
            dist = total_distance(swap_list)
            if dist < min_distance:
                min_distance = dist
                v = swap_list.copy()
            #print(x,y)
                x = 1
                y = 1
            else :
                continue
    temp_list.append(v)
    temp_list.append(round(min_distance, 2))
    temp_list.append(tem)
    return temp_list

def perm_tsp(v):

    combinations = itertools.permutations(v)
    t_dist = total_distance(v)
    t_dist_list = []
    res = []

    for x in combinations:
        if total_distance(list(x)) < t_dist:
            t_dist = total_distance(list(x))
            t_dist_list = list(x)
        else:
            continue
    res.append(t_dist_list)
    res.append(round(t_dist,2))
    return res


if __name__=="__main__":
    total_test = input("please input number of test ")
    test_case= int(total_test)
    #print(test_case)
    total_len = input("please input length of data ")
    test_length= int(total_len)

    test = []
    for x1 in range(0,test_case):
        data = {}
        for y1 in range(0,test_length):
            d = []
            alpha=["","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
            #d.append(float(random.randint(0, 10000)))
            d.append(0.0)
            d.append(float(random.randint(0, 10000)))
            h = y1+1
            #print(h)
            strng = ""
            while h != 0:
                a= h%26
                h = int(h/26)
                strng = strng + alpha[a]
                data[strng] = d
        test.append(data)
        test_data = []
        sta = 0
    for x in test:
        g = {}
        data = x
        m_tsp = my_tsp(list(x.keys())) 
        p_tsp = perm_tsp(list(x.keys()))
        g['test_data'] = x
        g["my_tsp"] = m_tsp
        g["perm_tsp"] = p_tsp
        if float(p_tsp[1])  ==  float(m_tsp[1]):
            g["restult"] = "PASS"
        else:
            g["restult"] = "FAIL"
        test_data.append(g)
        sta = sta + 1
        j = len(test)
        print("status:  " + str((sta/j)*100))
    #jsonString = json.dumps(test_data)
    with open('data_test2.json', 'w') as f:
        json.dump(test_data, f)