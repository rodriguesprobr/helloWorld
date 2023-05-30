from csv_class import csv_class

arquivo_ci = csv_class("C:\\Users\\ferna\\Downloads\\qualis_ci.csv")
arquivo_geo = csv_class("C:\\Users\\ferna\\Downloads\\qualis_geo.csv")
arquivo_ci.abrir()
arquivo_geo.abrir()
header_ci = arquivo_ci.ver_header()
header_geo = arquivo_geo.ver_header()
estrato_b2_ci = arquivo_ci.pesquisar_estrato("B2")
estrato_b2_geo = arquivo_geo.pesquisar_estrato("B2")
estrato_b2_ci.insert(0, header_ci)
estrato_b2_geo.insert(0, header_geo)
print(estrato_b2_ci)
print(estrato_b2_geo)