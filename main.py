from yomitandic import DicEntry, Dictionary, create_html_element
import datetime
import csv

freq_threshold = 50000

creation_date = str(datetime.date.today())

if __name__ == "__main__":
    dictionary = Dictionary(f"ECDICT [{creation_date}]")

    with open("ecdict.csv", 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)

        header = next(reader, None)

        cols = {}
        for index, elem in enumerate(header):
            cols[elem] = index
        

        for line in reader:
            word = line[cols["word"]]
            phonetic = line[cols["phonetic"]]
            translation = line[cols["translation"]]

            print(word)

            frq = line[cols["frq"]]
            if frq == 0:
                continue

            translation = translation.replace("\\n", "\n")

            t_list = []
            for t in translation.split("\n"):
                t_list.append(create_html_element("li", t)) 

            definition_element = create_html_element("ul", t_list)

            entry = DicEntry(word=word, reading=phonetic)
            entry.add_element(definition_element)
            dictionary.add_entry(entry)

    dictionary.export()
    dictionary.zip()


