# import csv
# path=r'D:\PycharmProjects\automation_practise\utilities\business-financial-data-june-2025-quarter.csv'
# def read_from_csv():
#     with open(path,'r') as reading:
#          subject=[]
#          read=csv.DictReader(reading)
#          for row in read:
#              subject.extend(row['Period'])
#     return set(subject)
# print(read_from_csv())

# def factorial():
#     a=[4,3,5]
#     n=[]
#     for i in a:
#         b=1
#         for j in range(2,i+1):
#             b*=j
#         n.append(b)
#     print(n)
# factorial()


# a=[{12:234},{89:89}]
# print({key:value for i in a for key,value in i.items()})

a=[12,32,45,455,90]
print([a[value] for value in range(len(a)) if value%2==0 if a[value]%2==0])