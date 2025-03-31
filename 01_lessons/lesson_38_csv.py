# panda - full data analysis library
# openpyx - designed specifically for excel files
# google sheets pytho API
import csv

data = open('/Users/mh184y/PycharmProjects/python_start/10_resources/example.csv', encoding='utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data)
print(data_lines)

data_lines[0]
len(data_lines)

for line in data_lines[1:]:
    print(line)

print(data_lines[1][3])

all_emails = []
for line in data_lines[1:]:
    all_emails.append(line[3])

file_to_output = open('to_save_file.csv', mode='w', newline='')
csv_writer = csv.writer(file_to_output, delimiter=',')
csv_writer.writerow(all_emails)
file_to_output.close()