#!/usr/bin/env python3


f = open("name_003.md")
names = f.read().split()

sec_hist = {}
thr_hist = {}

for name in names:
	sec = name[1]
	thr = name[2]
	if sec not in sec_hist:
		sec_hist[sec] = 1
	else:
		sec_hist[sec] = sec_hist[sec] + 1
	if thr not in thr_hist:
		thr_hist[thr] = 1
	else:
		thr_hist[thr] = thr_hist[thr] + 1


from collections import OrderedDict
sec_hist = OrderedDict(sorted(sec_hist.items(), key=lambda x: x[1], reverse=True))
thr_hist = OrderedDict(sorted(thr_hist.items(), key=lambda x: x[1], reverse=True))


# print(sec_hist)
# print(thr_hist)


print("# 이름 글자 빈도\n")

print("## 이름 첫째 글자 빈도")
for i,(k,v) in enumerate(sec_hist.items()):
	print("%s %d" % (k,v))

print("\n")
print("## 이름 둘째 글자 빈도")
for i,(k,v) in enumerate(thr_hist.items()):
	print("%s %d" % (k,v))