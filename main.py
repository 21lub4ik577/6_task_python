import os
import csv

file_name = 'poll.csv'

if not os.path.exists(file_name):
    with open(file_name, "w", encoding='utf-8', newline="") as f:
        write = csv.writer(f, delimiter=";")
        write.writerow(['ПИТАННЯ', 'ВАРІАНТ', 'ГОЛОСІВ'])

def main():
    while True:
        print("\МІНІ ОПИТУВАЛЬНИК/")
        print("1. СТВОРИТИ НОВЕ ОПИТУВАННЯ")
        print("2. ПРОГОЛОСУВАТИ")
        print("3. ПОКАЗАТИ РЕЗУЛЬТАТИ ОПИТУВАННЯ")
        print("4. ВИЙТИ")
        inpt = input("\nОБЕРІТЬ ДІЮ: ")

        if inpt == '1':
            print("СТВОРЕННЯ НОВОГО ОПИТУВАННЯ:\n ")

            quest = input("ВВЕДІТЬ ТЕКСТ ДЛЯ ОПИТУВАННЯ: ").strip()
            count = int(input("СКІЛЬКИ ВАРІАНТІВ ВІДПОВІДЕЙ: "))
            opt = []

            for i in range(count):
                num_quest = input(f"ВАРІАНТ {i + 1}: ")
                opt.append(num_quest)
            with open(file_name, "a", encoding='utf-8', newline="") as fl:
                in_gol = csv.writer(fl, delimiter=";")
                for g in opt:
                    in_gol.writerow([quest, g, 0])
            print("СТВОРЕНО!!!\n\n")


        elif inpt == "2":
            print("\nГОЛОСУВАННЯ:")
            with open(file_name, "r", encoding="utf-8", newline="") as fl:
                read = list(csv.reader(fl, delimiter=";"))
            if len(read) <= 1:
                print("ОПИТУВАННЯ ВІДСУТНІ!!!")
                continue
            
            questions = {}
            for r in read[1:]:
                quest, opt, votes = r
                if quest not in questions:
                    questions[quest] = []
                questions[quest].append(opt)
            
            print("ДОСТУПНІ ОПИТУВАННЯ: ")
            quest_list = list(questions.keys())
            for i, quest in enumerate(quest_list, 1):
                print(f"{i}. {quest}")
            quest_choice = int(input("ОБЕРІТЬ ОПИТУВАННЯ: ")) -1
            question = quest_list[quest_choice]
            
            opts = questions[question]
            print(f"\nОПИТУВАННЯ: {question}")
            for i, opt in enumerate(opts, 1):
                print(f"{i}. {opt}")
            o_choice = int(input("\nВАШ ВИБІР: ")) -1
            chosen_opt = opts[o_choice]

            for row in read[1:]:
                if row[0] == question and row[1] == chosen_opt:
                    row[2] = str(int(row[2]) + 1)
            with open(file_name, "w", encoding="utf-8", newline="") as fl:
                writer = csv.writer(fl, delimiter=";")
                writer.writerows(read)
            print("ГОЛОС ЗАРАХОВАНО!\n\n")
                        

        elif inpt == "3":
            print("\nРЕЗУЛЬТАТИ ОПИТУВАННЯ:")
            with open(file_name, "r", encoding="utf-8", newline="") as fl:
                read = list(csv.reader(fl, delimiter=";"))
            if len(read) <= 1:
                print("ОПИТУВАННЯ ВІДСУТНІ!!!")
                continue

            questions = {}
            for r in read[1:]:
                quest, opt, votes = r
                if quest not in questions:
                    questions[quest] = []
                questions[quest].append((opt, int(votes)))
            
            print("ДОСТУПНІ ОПИТУВАННЯ: ")
            quest_list = list(questions.keys())
            for i, quest in enumerate(quest_list, 1):
                print(f"{i}. {quest}")

            quest_choice = int(input("ОБЕРІТЬ ОПИТУВАННЯ ДЛЯ ПЕРЕГЛЯДУ РЕЗУЛЬТАТІВ: ")) - 1
            sele_quest = quest_list[quest_choice]

            print(f"\nРЕЗУЛЬТАТИ ОПИТУВАННЯ: {sele_quest}")

            options = questions[sele_quest]
            max_vot = max(v for o, v in options)

            print("РЕЗУЛЬТАТИ:")
            for opt, votes in options:
                print(f"{opt} — {votes} голосів")

            lead = [opt for opt, votes in options if votes == max_vot]
            print(f"\nЛідер: {', '.join(lead)}\n\n")


        elif inpt == "4":
            print("\nРОБОТУ ЗАВЕРШЕНО!")
            break

if __name__ == "__main__":
    main()
