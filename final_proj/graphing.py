import matplotlib.pyplot as plt
def bar_it(rev_no,se):
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.bar(rev_no,se)
    plt.show()
if __name__ == '__main__':
    rev_no=[]
    se=[]
    f=open(r"rev_no.txt","w")
    f1=open(r"se.txt","w")
    while(f.readline()==""):
        rev_no.append(int(f.readline()))
    while(f1.readline()==""):
        se.append(int(f1.readline())) 
    bar_it(rev_no,se)