#python_postgreSQL_car#
#######################

Tato tabulke postgreSQL je vytvořena pomocí Python ver. 3.11.0 a  knihovně psycopg2 ver. 2.9.5.

Uložiště obsahuje 4 soubory:
1. connection.py: udaje k přihlášení do postgreSQL databáze
2. creating_table.py: vytvoření tabulky
3. inserting_values.py: vložení hodnot 
4. README

Hodnoty se zadávaji v terminálu pomocí funkce input(). V terminálu se vypíše tabulke před vložením dále 3 otázky na vložení vozidel (značka vozidla, stáří vozidla a cena vozidla) poté se vypíše opět tabulka s novými hodnotami.
Na konci je pro kontrolu vypsaný stav uzavření spojení(0=open, 1=close) pokud je vypsaná 1 vše je OK. 
