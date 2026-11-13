import matplotlib.pyplot as plt
p = "karyer.txt"
o = "word_stat.txt"
f = open(p, 'r', encoding='utf-8')
t = f.read().lower()
d = '!"#\'()*+-=,./:;<>?[\\]^—'
for x in d:
    t = t.replace(x, " ")
w = t.split()
n = len(w)
k = {}
for x in w:
    if x in k:
        k[x] += 1
    else:
        k[x] = 1
s = sorted(k.items(), key=lambda i: i[1], reverse=True)
with open(o, "w", encoding="utf-8") as u:
    u.write(f"{'WORD: ':<20} | {'COUNT: ' :<24} | {'PERCENT: ':<20}" + '\n')
    for x, c in s:
        if (n > 0):
            r = (c / n) * 100
        else:
            r = 0
        u.write(f"{x :<20} | {c:<24} | {r:<5.2f}%" + '\n')
m = {}
for x in t:
    if x.isalpha():
        m[x] = m.get(x, 0) + 1
a = sorted(m.items(), key=lambda i: i[0])
l = [i[0] for i in a]
v = [i[1] for i in a]
plt.figure(figsize=(14, 6))
plt.bar(l, v, color="skyblue", edgecolor="black")
plt.title(f"Встречаемость букв в тексте ({p})", fontsize=14)
plt.xlabel("The Letters", fontsize=12)
plt.ylabel("Repet count", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
