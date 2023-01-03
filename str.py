st="Hello World"
pattern='l'
start=0
for i in range(st.count(pattern)):
    out=st.index(pattern,start)
    print(out,end='')
    start=out+1
    