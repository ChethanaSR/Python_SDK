import csv



f = open( "C:\\Users\\rchethana\\Documents\\SDK_Automation\\XML-TestData\\Metadata\\100-Function_Series_Verification_012.csv" )
csv_f = csv.reader( f )

series_id_csv = []
id_with_semicolon = ""
id_with_semicolon_1 =''

for row in csv_f:
    if row[0] == "Series ID":
        for col in range( 1, 101): series_id_csv.append( row[col] )
        break
#print series_id_csv
#
# for id in range(0, len(series_id_csv)):
#     id_with_semicolon_1 = id_with_semicolon_1 + series_id_csv[id] + ";"
# print id_with_semicolon_1


for id in range(0, len(series_id_csv)):
    if "("in series_id_csv[id]:
        value = series_id_csv[id].split("(")
        series_id_csv[id] = value[0].strip()
    id_with_semicolon= id_with_semicolon + series_id_csv[id]+";"
print id_with_semicolon[:-1]




