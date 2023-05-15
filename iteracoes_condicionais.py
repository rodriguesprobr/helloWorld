import csv

csv_file = "C:\\Users\\ferna\\Downloads\\2020_BR_Region_Mobility_Report.csv"

file = open(
    csv_file,
    "r",
    encoding="utf8"
)
csv_reader = csv.reader(file)
header = []
header = next(csv_reader)

print("O cabeçalho do Arquivo CSV é")
for head_num in range(0, len(header)):
    print(str(head_num) + ": " + header[head_num])

rows = []
for row in csv_reader:
    rows.append(row)

grocery_and_pharmacy_percent_change_from_baseline_value = 0.00
grocery_and_pharmacy_percent_change_from_baseline_row = []

for row in rows:
    if row[10] != "":
        grocery_and_pharmacy_percent_change_from_baseline_row = row if int(row[10]) > grocery_and_pharmacy_percent_change_from_baseline_value else grocery_and_pharmacy_percent_change_from_baseline_row
        #if int(row[10]) > grocery_and_pharmacy_percent_change_from_baseline_value:
            #grocery_and_pharmacy_percent_change_from_baseline_row = row

print(grocery_and_pharmacy_percent_change_from_baseline_row)
print("Pico de movimentação para Supermercados e Farmácias foi em: " +
      grocery_and_pharmacy_percent_change_from_baseline_row[3] +
      " no estado " +
      grocery_and_pharmacy_percent_change_from_baseline_row[2]
      )

# Usando break Somente os 500 primeiros resultados
grocery_and_pharmacy_percent_change_from_baseline_value = 0.00
grocery_and_pharmacy_percent_change_from_baseline_row = []
size = 1

for row in rows:
    if row[10] != "":
        grocery_and_pharmacy_percent_change_from_baseline_row = row if int(row[10]) > grocery_and_pharmacy_percent_change_from_baseline_value else grocery_and_pharmacy_percent_change_from_baseline_row
        #if int(row[10]) > grocery_and_pharmacy_percent_change_from_baseline_value:
            #grocery_and_pharmacy_percent_change_from_baseline_row = row
    size += 1
    if size >= 500:
        break

print(grocery_and_pharmacy_percent_change_from_baseline_row)
print("Pico de movimentação para Supermercados e Farmácias nos 100 primeiros resutlados foi em: " +
      grocery_and_pharmacy_percent_change_from_baseline_row[3] +
      " no estado " +
      grocery_and_pharmacy_percent_change_from_baseline_row[2]
      )

register = 0
print(rows[register][2])
while rows[register][2] == "":
    print("O registro número " + str(register) + " é nacional.")
    register += 1
