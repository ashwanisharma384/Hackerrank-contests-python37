# string="subsequence"
# pattern="sue"

st=input()[8:-1]
pt=input()[9:-1]
n=0
for p in pt:
    n += st.count(p)

print(n)
