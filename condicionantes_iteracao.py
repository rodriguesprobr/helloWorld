import csv

# Variável com o caminho e o nome do arquivo CSV a ser aberto.
csv_file = "C:\\Users\\ferna\\Downloads\\2020_BR_Region_Mobility_Report.csv"

# método de abrir o arquivo CSV. Nativo
file = open(
    csv_file, # nome do arquivo
    "r", # somente leitura
    encoding="utf-8" # detalha que a codificação do CSV é UTF-8
)

csv_reader = csv.reader(file) # atribui um ponteiro de leitura ao arquivo csv

header = []
header = next(csv_reader) #coloca a primeuira posição do ponteiro em uma variável header

#exibe as colunas (atributos) do cabeçalho
print("O cabeçalho do Arquivo CSV é")
for head_num in range(0, len(header)):
    print(str(head_num) + ": " + header[head_num])

# aloca em uma variavel do python todas as linhas (rows) do arquivo csv (sem header)
rows = []
for row in csv_reader:
    rows.append(row)

grocery_value = 0.00
grocery_row = []

for row in rows:
    if row[10] != "":
        #grocery_value = int(row[10]) if int(row[10]) > grocery_value else grocery_value
        #grocery_row = row if int(row[10]) > grocery_value else grocery_row
        if int(row[10]) > grocery_value:
            grocery_value = int(row[10])
            grocery_row = row

print(
    "Pico de movimentação para Mercados e Farmácias foi em: " +
    grocery_row[3] +
    " no estado " +
    grocery_row[2] +
    " na data de " +
    grocery_row[8] +
    " com um pico de " +
    str(grocery_value)
)

grocery_value = 0.00
grocery_row = []
size = 1

for row in rows:
    if row[10] != "":
        if int(row[10]) > grocery_value:
            grocery_value = int(row[10])
            grocery_row = row
    if size >= 500:
        break
    size += 1

print(
    "Pico de movimentação para Mercados e Farmácias foi em: " +
    grocery_row[1] +
    " na data de " +
    grocery_row[8] +
    " com um pico de " +
    str(grocery_value)
)

register = 0
#print(rows[register][2])
while rows[register][2] == "":
    print("Acessando rows[" + str(register) + "]")
    print("A linha número " + str(register) + " é nacional. Data: " + str(rows[register][8]))
    register += 1