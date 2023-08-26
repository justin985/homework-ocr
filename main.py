import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import pytesseract
import openai
if __name__ == "__main__":
    def select_image():
        file_path = filedialog.askopenfilename()
        img_path_entry.delete(0, tk.END)
        img_path_entry.insert(tk.END, file_path)

    def process_image():
        openai.api_key = api_key_entry.get()
        img_path = img_path_entry.get()

        img = Image.open(img_path)
        text = pytesseract.image_to_string(img, lang='eng+chi_tra')

        res = openai.Completion.create(
            model="text-davinci-003",
            prompt="告訴我下方題目的正確答案，只需說出英文字母:"+text,
        )

        result = res["choices"][0]["text"]
        messagebox.showinfo("Result", result)


    root = tk.Tk()

    api_key_label = tk.Label(root, text="OpenAI API Key")
    api_key_label.pack()

    api_key_entry = tk.Entry(root)
    api_key_entry.pack()

    img_path_label = tk.Label(root, text="圖片路徑")
    img_path_label.pack()

    img_path_entry = tk.Entry(root)
    img_path_entry.pack()

    select_img_btn = tk.Button(root, text="選擇圖片", command=select_image)
    select_img_btn.pack()

    process_btn = tk.Button(root, text="Process Image", command=process_image)
    process_btn.pack()

    root.mainloop()


