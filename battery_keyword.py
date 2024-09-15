import tkinter as tk
from tkinter import font as tkfont
import random

def generate_random_string():
    """Generates a random string based on user input and displays it."""
    try:
        desired_length = int(entry_length.get())
        result_string = ""
        fixed_words = ["แบตเตอรี่","สตาร์ทไม่ติด","ไดสตาร์ทเสีย","จั๊มแบต","เปลี่ยนแบต","พ่วงแบต","ร้านแบตใกล้ฉัน","ไฟแบตโชว์"]

       
        if include_fixed.get():  # Only include fixed words if the checkbox is checked
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

        return result_string

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
    "เปลี่ยนแบตเตอรี่รถยนต์","แบตเตอรี่รถยนต์หมด","ชาร์จแบตเตอรี่รถยนต์","บริการเปลี่ยนแบตเตอรี่ถึงที่","แบตเตอรี่รถยนต์ใกล้ฉัน",
    "ซ่อมแบตเตอรี่รถยนต์","ตรวจเช็คแบตเตอรี่รถยนต์","แบตเตอรี่รถยนต์ราคาถูก","แบตรถราคาถูก","แบตเตอรี่รถยนต์ยี่ห้อไหนดี",
    "เปลี่ยนแบตเตอรี่รถยนต์ด่วน","เปลี่ยนแบตด่วน","แบตเตอรี่รถยนต์ไฟไม่เข้า","ไฟไม่เข้า","แบตเตอรี่รถยนต์ใช้นานแค่ไหน",
    "เลือกแบตยี่ห้อไหนดี","ร้านแบตเตอรี่รถยนต์ใกล้ฉัน","แบตเสื่อม","แบต 24 ชั่วโมง","ตรวจสภาพแบตเตอรี่","อาการแบตเสื่อม",
    "แบตเตอรี่ไม่เก็บไฟ","แบตเตอรี่มีปัญหา","ร้านขายแบตเตอรี่รถยนต์","แบตเตอรี่รถยนต์ยี่ห้อไหนทน","แบตยี่ห้อไหนทน","",
    "เปลี่ยนแบตเตอรี่รถยนต์ที่ไหนดี","ซ่อมแบตเตอรี่รถยนต์ถึงบ้าน","การบำรุงรักษาแบตเตอรี่รถยนต์","วิธีดูแลแบตเตอรี่รถยนต์",
    "การเลือกซื้อแบตเตอรี่รถยนต์","แบตหมด","เปลี่ยนแบตสำรองรถยนต์","ช่างแบตใกล้ฉัน","อายุแบตเตอรี่รถยนต์","ร้านแบตเตอรี่รถยนต์ใกล้ฉัน",
    "ร้านชาร์จแบตเตอรี่รถยนต์ใกล้ฉัน","แบตเตอรี่รถยนต์ใกล้ฉัน","เปลี่ยนแบตเตอรี่รถยนต์ใกล้ฉัน","เปลี่ยนแบตรถยนต์","แบตเตอรี่นอกสถานที่",
    "ร้านแบตเตอรี่รถยนต์ใกล้ฉัน","พ่วงแบตรถเก๋ง","เปลี่ยนแบต","ไฟชาร์จไม่เข้า","ไดสตาร์ทเสีย","ไดชาร์จเสีย","ไฟไม่เข้า","เปลี่ยนไดชาร์จ",
    "เปลี่ยน battery","battery ใกล้ฉัน","เปลี่ยน battery","battery นอกสถานที่","จั๊มแบต","จั๊มแบตนอกสถานที่","จั๊มแบตเตอรี่ใกล้ฉัน",
    "พ่วงแบตนอกสถานที่","พ่วงแบตกใกล้ฉัน","battery ราคา",
]

# Create the main window
root = tk.Tk()
root.title("Battery Keyword")

# Custom font settings for Thai text
custom_font = tkfont.Font(family="Tahoma", size=12)

# Create and place the input field for the desired length
label_prompt = tk.Label(root, text="Enter the str length :", font=custom_font)
label_prompt.pack(pady=10)

entry_length = tk.Entry(root, font=custom_font)
entry_length.pack(pady=5)

# Create a checkbox to include or exclude fixed words
include_fixed = tk.BooleanVar()
include_fixed.set(False)  # Ensure the checkbox is not selected by default
checkbox_fixed = tk.Checkbutton(root, text="Include fixed words", variable=include_fixed)
checkbox_fixed.pack(pady=5)

# Create and place the button to generate the random string
button_generate = tk.Button(root, text="Generate", command=generate_random_string, font=custom_font)
button_generate.pack(pady=10)

# Create and place a text widget to display the result
text_result = tk.Text(root, height=5, width=50, padx=20, pady=10,font=custom_font, wrap=tk.WORD)
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
