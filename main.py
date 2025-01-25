import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):
    try:
        # HTML-Inhalt der Website abrufen
        response = requests.get(url)
        if response.status_code != 200:
            return f"Fehler: Website konnte nicht geladen werden. Statuscode: {response.status_code}"

        # HTML parsen
        soup = BeautifulSoup(response.text, 'html.parser')

        # Alle <p>-Tags (Absätze) extrahieren
        paragraphs = soup.find_all('p')

        # Fließtext zusammenfügen
        text = "\n".join([para.get_text() for para in paragraphs])

        return text
    except Exception as e:
        return f"Fehler: {e}"

# Hauptprogramm
#if __name__ == "__main__":
    # Beispiel-URL
url = "https://telegrafi.com/musk-po-shkakton-telashe-ne-evrope-cfare-perfiton-ai-nga-kjo/"
    
    # Fließtext extrahieren
extracted_text = extract_text_from_url(url)
    
    # Ergebnis anzeigen
print("\nExtrahierter Text:\n")
print(extracted_text)
    
    # Optional: Ergebnis in einer Datei speichern
with open("extrahierter_text.txt", "w", encoding="utf-8") as file:
    file.write(extracted_text)
print("\nDer Text wurde in 'extrahierter_text.txt' gespeichert.")
