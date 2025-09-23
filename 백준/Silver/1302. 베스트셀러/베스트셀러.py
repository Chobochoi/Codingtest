N = int(input())
dic = {}

for i in range(N):
    name = input()

    if name not in dic:
        dic[name] = 1
    else:
        dic[name] += 1

max_value = max(dic.values())

st = []

for key, value in dic.items():
    if value == max_value:
        st.append(key)

st.sort()

print(st[0])