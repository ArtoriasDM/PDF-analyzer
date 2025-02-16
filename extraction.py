import pdfplumber

def extract_data(pdf_name, headers):

    headers = ["Esito", "Es1", "Es2", "Es3"]

    with pdfplumber.open(pdf_name) as pdf:
        # crea una hashmap per contenere le colonne estratte dal file
        columns = {header: [] for header in headers}

        page = pdf.pages[0]
        table = page.extract_table()

        first_row = table[0]
        indices = {}

        for header in headers:
            if header in first_row:
                indices[header] = first_row.index(header)
        for row in table[1:]:
            for header, index in indices.items():
                columns[header].append(row[index])

        # itera sulle diverse pagine del file
        for page in pdf.pages[1:]:
            # estrae il contenuto della pagina e crea una lista di liste con le diverse righe 
            table = page.extract_table()
            # a partire dalla seconda riga prende gli elementi delle colonne e le salva nella hashmap secondo intestazione
            for row in table:
                for header, index in indices.items():
                    columns[header].append(row[index])
    return columns



        