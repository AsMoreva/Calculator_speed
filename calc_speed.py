# Импорт модуля tkinter для создания графического интерфейса пользователя (GUI)
import tkinter as tk

# Определение функции для конвертации скорости между различными единицами измерения
def convert_speed():
    
    try:
        # Получение значения из текстового поля ввода и преобразование его в число с плавающей точкой
        value = float(entry.get())
        # Получение выбранной единицы измерения из выпадающего списка "от"
        from_unit = from_var.get()
        # Получение выбранной единицы измерения из выпадающего списка "до"
        to_unit = to_var.get()
        
        # Конвертация скорости из км/ч в другие единицы измерения
        if from_unit == to_unit:
            result = value
        elif from_unit == "km/h":
            if to_unit == "m/s":
                result = value * 1000 / 3600
            elif to_unit == "mph":
                result = value * 0.621371
            elif to_unit == "ft/s":
                result = value * 0.911344
            elif to_unit == "knots":
                result = value * 0.539957
            elif to_unit == "mach":
                result = value / 1225.044
        elif from_unit == "m/s":
            if to_unit == "km/h":
                result = value * 3600 / 1000
            elif to_unit == "mph":
                result = value * 2.23694
            elif to_unit == "ft/s":
                result = value * 3.28084
            elif to_unit == "knots":
                result = value * 1.94384
            elif to_unit == "mach":
                result = value / 340.29
        elif from_unit == "mph":
            if to_unit == "km/h":
                result = value * 1.60934
            elif to_unit == "m/s":
                result = value * 0.44704
            elif to_unit == "ft/s":
                result = value * 1.46667
            elif to_unit == "knots":
                result = value * 0.868976
            elif to_unit == "mach":
                result = value / 767.269
        elif from_unit == "ft/s":
            if to_unit == "km/h":
                result = value * 1.09728
            elif to_unit == "m/s":
                result = value * 0.3048
            elif to_unit == "mph":
                result = value * 0.681818
            elif to_unit == "knots":
                result = value * 0.592484
            elif to_unit == "mach":
                result = value / 1116.437
        elif from_unit == "knots":
            if to_unit == "km/h":
                result = value * 1.852
            elif to_unit == "m/s":
                result = value * 0.514444
            elif to_unit == "mph":
                result = value * 1.15078
            elif to_unit == "ft/s":
                result = value * 1.68781
            elif to_unit == "mach":
                result = value / 661.471
        elif from_unit == "mach":
            if to_unit == "km/h":
                result = value * 1225.044
            elif to_unit == "m/s":
                result = value * 340.29
            elif to_unit == "mph":
                result = value * 767.269
            elif to_unit == "ft/s":
                result = value * 1116.437
            elif to_unit == "knots":
                result = value * 661.471
        else:
            result = "Ошибка" # Возвращаем ошибку, если не поддерживается указанная единица измерения
            
        # Очистка текстового поля ввода перед выводом результата
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ValueError:
         # Обработка исключений, связанных с неверным форматом вводимого значения
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Ошибка")
        
# Создание основного окна приложения
root = tk.Tk()
root.title("Калькулятор скорости")

# Создание текстового поля для ввода значений
entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)
def on_click(event):

  text = event.widget.cget("text") # Получение текста кнопки, по которой был совершен клик
  if text == "=":
    convert_speed()  # Вызываем конвертацию при нажатии "="
  elif text == "CE":
    entry.delete(0, tk.END)
  else:
    entry.insert(tk.END, text)
      
# Создание меток и выпадающих списков для выбора единиц измерения
from_label = tk.Label(root, text="Из:")
from_label.grid(row=5, column=0)
from_var = tk.StringVar(root)
from_var.set("km/h")
from_options = ["km/h", "m/s", "mph", "ft/s", "knots", "mach"]
from_menu = tk.OptionMenu(root, from_var, *from_options)
from_menu.grid(row=5, column=1)

to_label = tk.Label(root, text="В:")
to_label.grid(row=5, column=2)
to_var = tk.StringVar(root)
to_var.set("m/s")
to_options = ["km/h", "m/s", "mph", "ft/s", "knots", "mach"]
to_menu = tk.OptionMenu(root, to_var, *to_options)
to_menu.grid(row=5, column=3)

buttons = [
    '1', '2', '3',
    '4', '5', '6',
    '7', '8', '9',
    '0', '.',  'CE', '=',
]

row = 1
col = 0
for button_text in buttons:
    button = tk.Button(root, text=button_text, padx=20, pady=10)
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", on_click)  # Привязываем обработчик событий к каждой кнопке
    col += 1
    if col > 3:
        col = 0
        row += 1
        
# Запуск главного цикла обработки событий
root.mainloop()
