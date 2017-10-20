# coding: utf-8


class HtmlCode:
    def __init__(self, json):
        self.jsondoc = json
        self.similar = self.jsondoc["Similar"]
        self.info = self.jsondoc["Similar"]["Info"]
        self.results = self.jsondoc["Similar"]["Results"]


    def get_message(self):
        return "this works as expected"


    def convert_to_html(self):

        html_text = "</head><head><title>Resultados</title><meta charset='utf-8'><meta name='viewport' content='width=device-width, initial-scale=1'>" \
                    "<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css'>" \
                    "<script src='https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js'></script>" \
                    "<script src='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js'></script><html>\n\t<body>\n\t\t<table class='table'>\n\t\t\t" \
                    "<tr><th>Nombre</th><th>Similitud</th></tr>"

        for elemento in range (0, len(self.results)):
            text = "<tr><td>" + self.results[elemento]['Name'] + "</td><td>" + self.results[elemento]['Type'] + "</td></tr>\n"
            html_text = html_text + text
        html_text = html_text + "\n\t\t</table\n\t</body>\n</html>"
        return html_text
