
id_list = ["muzi", "frodo", "apeach", "neo"]
dicReports = {id:[] for id in id_list}
answer = [0] * len(id_list)
# print(dicReports)
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
for i in set(report):
    report = i.split(' ')
    dicReports[report[1]].append(report[0])
    print(dicReports)




