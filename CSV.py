import csv
"""
file=open('example.csv')
file_reader=csv.reader(file)

#data=list(file_reader)
#print(data)
#print(data[0][2])


for row in file_reader:
    print('row no ='+str(file_reader.line_num)+' '+ str(row))
    """
output_file=open('out.csv','w',newline='')
output_writer=csv.writer(output_file,delimiter ='#')
output_writer.writerow(['1','2','3'])
output_writer.writerow(['25','15'])
output_file.close()
