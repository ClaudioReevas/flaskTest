# coding: utf-8

# import the required libaries for POSTGRES
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Main class with the required methods
class HtmlCode:
    def __init__(self, json): #class initialization
        self.jsondoc = json
        self.similar = self.jsondoc["Similar"]
        self.info = self.jsondoc["Similar"]["Info"]
        self.results = self.jsondoc["Similar"]["Results"]


    def get_message(self): # just for test puproses
        return "this works as expected"


    def convert_to_html(self):   # this method converts the response to HTML
        self.create_database()
        self.create_table()
        # html_text is just the header and html initial part, google is simple for front end dev to understand
        # this please google about it
        html_text = "</head><head><title>Resultados</title><meta charset='utf-8'><meta name='viewport' content='width=device-width, initial-scale=1'>" \
                    "<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css'>" \
                    "<script src='https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js'></script>" \
                    "<script src='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js'></script><html>\n\t<body>\n\t\t<table class='table'>\n\t\t\t" \
                    "<tr><th>Nombre</th><th>Similitud</th></tr>"

        # With a for it's taking each of the results from the lists of results and filling a table but also is adding
        # data to the POSTGRES TABLE
        # (see self.results = self.jsondoc["Similar"]["Results"])
        for elemento in range (0, len(self.results)):
            text = "<tr><td>" + self.results[elemento]['Name'] + "</td><td>" + self.results[elemento]['Type'] + "</td></tr>\n"
            html_text = html_text + text
            self.add_data(self.results[elemento]['Name'], self.results[elemento]['Type'])

        # Finishing cycle we write the final part of the html and return the HTML as result of convert_to_html() method
        html_text = html_text + "\n\t\t</table\n\t</body>\n</html>"
        return html_text

    def create_database(self):  # this method is just creating the database buuuuut! is considering if it exists or not


        connection = psycopg2.connect("dbname=postgres user=postgres password=y0ur-p4ss")
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = connection.cursor()

        sentencia = "select datname from pg_database where datname='tastedive';"    # select over the context of postgres
                                                                                    # to find if database exists
        cur.execute(sentencia)
        elemento = cur.fetchone()
        print elemento #just printing to doublecheck

        # by checking if the database exists POSTGRES return a tuple where you can see the name
        # of the database or None if there is just nothing

        if elemento != None:    # if exist just print it
            a, = elemento
            print a,
        else:                   # if doesn't exist create it
            sentencia = "CREATE DATABASE tastedive;"
            cur.execute(sentencia)

        connection.close()

    def create_table(self):     # this method is just creating the database buuuuut! is considering if it exists or not
        connection = psycopg2.connect("dbname=tastedive user=postgres password=y0ur-p4ss")
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = connection.cursor()
        # yes... all this next line to see if the table exists (it works... so what?)
        listar_tablas = """
                        SELECT table_schema||'.'||table_name AS full_rel_name
                        FROM information_schema.tables
                        WHERE table_schema = 'public';
                        """
        print listar_tablas
        cur.execute(listar_tablas)
        elementos = cur.fetchone()
        print elementos
        if elementos != None:    # Now switch to spanish, why because this was the first line i commented... Si existe la tabla personas dentro del esquema plublic en la base de datos tastedive solo imprimir
            a, = elementos
            print a,
        else:           #Si NO existe la tabla personas dentro del esquema plublic en la base de datos tastedive entonces CREAR LA TABLA PERSONAS
            create_table = """
                            CREATE TABLE Personas (
                            name varchar(255),
                            type varchar(255));
                            """
            cur.execute(create_table)
        connection.close()

    def add_data(self, name, type_var): #add_data is the method we called to insert into the table the values

        connection = psycopg2.connect("dbname=tastedive user= postgres password=y0ur-p4ss")
        cur = connection.cursor()

        insert_table = "INSERT INTO Personas (name,type) VALUES ('" + name + "','" + type_var + "')" # just do the insert

        cur.execute(insert_table)
        connection.commit()
        cur.close()
        connection.close()



    def print_data(self):   # printing for this example purposes is useless, so i will use it on another example
        pass


