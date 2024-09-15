import tkinter as tk
from tkinter import font as tkfont
import random

def generate_random_string():
    """Generates a random string based on user input and displays it."""
    try:
        desired_length = int(entry_length.get())
        result_string = ""
        fixed_words = ["ซ่อมกุญแจ","ซ่อมกุญแจนอกสถานที่","ซ่อมกุญแจใกล้ฉัน","ซ่อมกุญแจด่วน","ร้านกุญแจใกล้ฉัน","ช่างกุญแจใกล้ฉัน"]

       
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
    "ซ่อมกุญแจรถยนต์ด่วน","ช่างกุญแจรถยนต์","ช่างกุญแจรถยนต์ใกล้ฉัน","ช่างทำกุญแจรถยนต์","บริการทำกุญแจรถยนต์","เปลี่ยนกุญแจรีโมทรถยนต์",
    "ซ่อมรีโมทรถยนต์","รีเซ็ตกุญแจรถยนต์","แก้ไขปัญหากุญแจรีโมทรถยนต์","ทำกุญแจรถยนต์ใหม่","ปลดล็อครถยนต์","กุญแจรถยนต์หาย","กุญแจรถยนต์ล็อค",
    "กุญแจรีโมทเสีย","กุญแจรีโมทไม่ทำงาน","รีโมทรถยนต์ไม่ทำงาน","แบตเตอรี่รีโมทรถยนต์","กุญแจรีโมทเปิดไม่ได้","ทำกุญแจรีโมทรถยนต์","รีโมทรถยนต์ไม่ติด",
    "กุญแจรถยนต์หายทำยังไง","ซ่อมกุญแจรีโมทด่วน","ทำกุญแจรถยนต์ราคาถูก","ร้านทำกุญแจรถยนต์","ร้านซ่อมรีโมทรถยนต์","บริการซ่อมกุญแจรถยนต์","ซ่อมกุญแจรีโมท",
    "ช่างกุญแจมืออาชีพ","ทำกุญแจรถยนต์สำรอง","สั่งทำกุญแจรถยนต์","แก้ไขกุญแจรถยนต์มีปัญหา","ช่างกุญแจรถยนต์ 24 ชั่วโมง","ซ่อมรีโมทเปิดปิดรถยนต์","กุญแจรถยนต์เปิดไม่ได้",
    "กุญแจรถยนต์หัก","ช่างกุญแจ","ซ่อมกุญแจ","งานกุญแจ","กุญแจใกล้ฉัน","ร้านกุญแจด่วน","ทำกุญแจฉุกเฉิน","กุญแจหายเรียกช่าง","กุญแจเสียเรียกช่าง","ร้านกุญแจใกล้ฉัน"
]

# Create the main window
root = tk.Tk()
root.title("Tie Keyword")

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
