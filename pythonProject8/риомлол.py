import pandas as pd

df_excel = pd.read_excel('Годовые_оценки_для_пндас.xlsx')

for i in range(len(df_excel)):

    print(f"{i + 1}. {df_excel.iloc[i]}")

choice = int(input("Введите номер строки, которую хотите выбрать: "))

if 1 <= choice <= len(df_excel):

    selected_row = df_excel.iloc[choice - 1]
    print(f"Ваша выбранная строка:\n{selected_row}")

    average = selected_row.mean()
    print(f"Среднее арифметическое значений в выбранной строке: {average:.2f}")
else:
    print("Неверный номер строки!")

print(df_excel.info())