from yomitandic import DicEntry, Dictionary, create_html_element

import datetime
import csv


if __name__ == "__main__":
    dictionary = Dictionary(f"ECDICT [test]")


    with open("test.csv", 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)

        header = next(reader, None)

        cols = {}
        for index, elem in enumerate(header):
            cols[elem] = index
        
        print(f"cols {cols}")
         
        for line in reader:
            print(f"line {line}")
            word = line[cols["word"]]
            phonetic = line[cols["phonetic"]]
            translation = line[cols["translation"]]

            print(f"word: {word}")

            # Replace literal \n with actual newlines before splitting
            translation = translation.replace("\\n", "\n")

            t_list = []
            for t in translation.split("\n"):
                print(f"t: {t}")
                t_list.append(create_html_element("li", t)) 

            definition_element = create_html_element("ul", t_list)

            entry = DicEntry(word=word, reading=phonetic)
            entry.add_element(definition_element)
            dictionary.add_entry(entry)

    dictionary.export()
    dictionary.zip()
