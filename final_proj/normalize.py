import csv
import senti
import time
# import matplotlib.pyplot as plt
def get_nr():
    x=[]
    text=[]
    y=[]
    with open('/Users/anand/Desktop/hacks/devJAMS/material/reviews.csv','rt')as f:
        data = csv.reader(f)
        i=0
        for row in data:
            i+=1
            if i <=80 and i!=1:
                #print(row)
                x.append(row[0][0])
                text.append(row[1])
                #print('no of stars:',row[0][0])
            elif i == 1:
                print('i=1')
            else:
                break
    #print(text)
    #print(x)
    # print(len(text), len(x))
    print('starting....')
    print('text: ',text)
    print('STAR RATINGS: ',x)
    su=0
    for i in x:
        g = int(i)
        su+=g
    oor = su/len(x)
    print('or', oor)
    rev_no = []
    se=[]
    for i in range(13):
        rev_no.append(str(i+1))
        sentiment = senti.get_senti(text[i])
        temp = int(x[i])*sentiment['score']
        print(temp)
        se.append(str(temp))
        time.sleep(0.2)
        y.append(temp)
    print(rev_no , se)
    f = open(r"rev.txt","a")
    f1 = open(r"se.txt","a")
    for i in rev_no:
        f.writelines(i+'\n')
    for i in se:
        f1.writelines(i+'\n')
    f.close()
    f1.close()
    # fig = plt.figure()
    # ax = fig.add_axes([0,0,1,1])
    # ax.bar(rev_no,se)
    # plt.show()
    s=0
    for i in y:
        s+=i+(3*i/2)
    nr = s/len(y)
    return [nr,oor]
if __name__ == "__main__":
    print(get_nr())
