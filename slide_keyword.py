import tkinter as tk
from tkinter import font as tkfont
import random

def generate_random_string():
    """Generates a random string based on user input and displays it."""
    try:
        desired_length = int(entry_length.get())
        result_string = ""
        fixed_words = ["รถสไลด์", "รถยก", "รถลาก"]

         ## add-on fixed word
        for word in fixed_words:
                if len(result_string) + len(word) + 2 <= desired_length:  # +2 for ", "
                    result_string += word + ", "

        # Randomly select words and concatenate them with ", " until the desired length is reached
        while len(result_string) < desired_length:
            random_word = random.choice(words_list)
            if len(result_string) + len(random_word) + 2 <= desired_length:  # +2 for ", "
                result_string += random_word + ", "
            else:
                break

        # If the loop ends and the string is slightly shorter, fill with characters from another word
        if len(result_string) < desired_length:
            additional_chars = random.choice(words_list)[:desired_length - len(result_string)]
            result_string += additional_chars

        # Remove the trailing comma and space if necessary
        result_string = result_string.strip(', ')

        # Display the result in the text widget
        text_result.config(state=tk.NORMAL)
        text_result.delete(1.0, tk.END)
        text_result.insert(tk.END, result_string)
        text_result.config(state=tk.NORMAL)
        label_length.config(text=f"Total length: {len(result_string)}")
    except ValueError:
        tk.messagebox.showerror("Invalid input", "Please enter a valid number.")

def copy_to_clipboard():
    """Copies the selected text to the clipboard."""
    try:
        selected_text = text_result.get(tk.SEL_FIRST, tk.SEL_LAST)
        root.clipboard_clear()
        root.clipboard_append(selected_text)
    except tk.TclError:
        pass  # No text selected

def show_context_menu(event):
    """Displays the right-click context menu."""
    context_menu.post(event.x_root, event.y_root)

# Define the list of words
words_list = [
    "รถสไลด์ใกล้ฉัน","รถสไลด์ด่วน","รถสไลด์ ราคา","รถสไลด์ราคาถูก","รถสไลด์ฉุกเฉิน","เบอร์โทรรถสไลด์"
    ,"รถสไลด์ถึงที่","รถสไลด์ 24 ชั่วโมง","รถหกล้อสไลด์","รถหกล้อสไลด์ใกล้ฉัน","รถหกล้อสไลด์ด่วน"
    ,"รถหกล้อสไลด์ ราคา","รถหกล้อสไลด์ราคาถูก","รถหกล้อสไลด์ด่วนนอกสถานที่","รถหกล้อสไลด์ใกล้ๆ"
    ,"รถหกล้อสไลด์มีประกัน","รถสไลด์มีประกัน","เบอร์โทรรถหกล้อสไลด์","ช่างรถสไลด์มืออาชีพ","รถลากฉุกเฉิน"
    ,"รถลากด่วน","รถลากใกล้ฉัน","เบอร์โทรรถลาก","รถลากราคาถูก","รถลากมีประกัน","รถลากอุบัติเหตุ"
    ,"รถลากรถสไลด์","รถยกเล็ก","รถยกเล็กใกล้ฉัน","ราคารถยกเล็ก","รถยกอุบัติเหตุ","รถยกใหญ่","เบอร์โทรรถยกเล็ก"
    ,"เบอร์โทรรถยกใหญ่","ยกรถบรรทุก","ยกรถกระบะ","ยกรถส่งศูนย์","ยกรถพัง","รถกระบะสไลด์","กระบะสไลด์ใกล้ฉัน"
    ,"กระบะสไลด์ราคา","กระบะสไลด์เบอร์โทร","กระบะสไลด์ด่วน","กระบะสไลด์ส่งศูนย์","กระบะสไลด์รถอุบัติเหตุ"
    ,"กระบะสไลด์มีประกัน","กระบะสไลด์มืออาชีพ","กระบะสไลด์ช่างซ่อม","บริการรถฉุกเฉิน","บริการเคลื่อนย้ายรถยนต์"
    ,"เคลื่อนย้ายรถยนต์ใกล้ฉัน","เคลื่อนย้ายรถยนต์ราคาถูก","เบอร์โทรช่างมืออาชีพ","ซ่อมนอกสถานที่","เบอร์โทรช่างซ่อมนอกสถานที่"
    ,"รถยกรถสไลด์","บริการถึงที่","บริการ 24 ชั่วโมง","24 Carfix","รถสไลด์ถึงที่ 24 ชั่วโมง","แอดไลน์รถยกรถสไลด์"
    ,"เรียกรถสไลด์ผ่านแอป","เรียกช่างผ่านแอป","แอปรถสไลด์","แอปซ่อมนอกสถานที่","ศูนย์บริการรถยนต์","รถยก","รถลาก"
]

# Create the main window
root = tk.Tk()
root.title("Slide Keyword")

# Custom font settings for Thai text
custom_font = tkfont.Font(family="Tahoma", size=12)

# Create and place the input field for the desired length
label_prompt = tk.Label(root, text="Enter the str length :", font=custom_font)
label_prompt.pack(pady=10)

entry_length = tk.Entry(root, font=custom_font)
entry_length.pack(pady=5)

# Create and place the button to generate the random string
button_generate = tk.Button(root, text="Generate", command=generate_random_string, font=custom_font)
button_generate.pack(pady=10)

# Create and place a text widget to display the result
text_result = tk.Text(root, height=5, width=50, padx=20, pady=10,font=custom_font)
text_result.pack(pady=10)

# Create a context menu for the text widget
context_menu = tk.Menu(root, tearoff=0)
context_menu.add_command(label="Copy", command=copy_to_clipboard)

# Bind the right-click event to show the context menu
text_result.bind("<Button-3>", show_context_menu)

# Create and place a label to show the length of the generated string
label_length = tk.Label(root, text="Total length: 0", font=custom_font)
label_length.pack(pady=5)

# Start the main event loop
root.mainloop()
