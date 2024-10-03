import xlsxwriter

fname = input("file name: ")+".xlsx"
workbook = xlsxwriter.Workbook(fname)
worksheet = workbook.add_worksheet()

cols = ["A", "B", "C", "D", "E", "F", "G", "H"]
labels = ["Y", "r1", "r2", "dr", "k", "t1", "t2", "t3"]

cnt = 0
for l in labels:
    worksheet.write(cols[cnt]+"1", l)
    cnt += 1

output = [
    {'Y': -643818.3188955208, 'r1': 5, 'r2': 5.01, 'dr': 0.01, 'k': 1, 't1': 18, 't2': 50, 't3': 62},
    {'Y': -148362.66962801167, 'r1': 5, 'r2': 5.02, 'dr': 0.01, 'k': 2, 't1': 54, 't2': 78, 't3': 171}
]

cnt = 2
for o in output:
    for i in range(len(cols)):
        worksheet.write(cols[i]+str(cnt), o[labels[i]])
    cnt += 1

workbook.close()