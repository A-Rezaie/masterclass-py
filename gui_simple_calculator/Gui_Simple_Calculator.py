# import and global variables
import tkinter as tk

window = tk.Tk()
window.title("Python Calculator")
window.geometry("300x220")
window.resizable(width=False, height=False)

for col in range(4):
    window.columnconfigure(col, weight=1)

for row in range(1,5):
    window.rowconfigure(row, weight=1)



# calculator functions
def on_button_click(button_text):
    current_text = display_entry.get()
    operators = ["+", "-", "*", "/"]

    if current_text == "Error":
        display_entry.delete(0, last="end")
        current_text = ""
    
    if button_text == "c":
        display_entry.delete(0, last="end")
        return

    if button_text == "=":

        if not current_text:
            return
        
        if current_text[-1] in operators:
            return
        try:
            result = do_calculate(current_text)

        except ZeroDivisionError:
            display_entry.delete(0, last="end")
            display_entry.insert("end", "Error")
            return

        display_entry.delete(0, last="end")
        text_result = str(result)
        display_entry.insert("end", text_result)
        return 
    
    if button_text in operators and current_text and current_text[-1] in operators:
        return
    
    if not current_text and button_text in operators:
        return 
    
    display_entry.insert("end", button_text)

def do_calculate(expression):
    return eval(expression)

    
    
    


# ui design
display_entry = tk.Entry(window, justify="right")
display_entry.grid(row=0, column=0, columnspan=4, sticky="ew", padx=10, pady=10, ipady=8)

buttons = [["7","8","9","+"],["4","5","6","-"],["1","2","3","*"],["c","0","=","/"]]

for row in range(4):
    for col in range(4):
        button_text= buttons[row][col]
        tk.Button(
            window,command= lambda x= button_text:on_button_click(x), text= button_text, width=2,
            height=1,
        ).grid(row=row+1, column=col, sticky="nsew", padx=1, pady=1, ipady=2)

# running application

window.mainloop()
