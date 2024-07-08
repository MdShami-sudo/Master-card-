import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageTk, ImageDraw, ImageFilter

Shami = "Shami"
expiry_date = "12/25"
account_number = "1234 5678 9012"
pin_number = "****"

root = tk.Tk()
root.title("MasterCard ATM Card Design")
root.geometry("400x250")

def create_glass_morphic_background():
    width, height = 400, 250
    background_color = (255, 255, 255, 0)  
    image = Image.new("RGBA", (width, height), background_color)

    draw = ImageDraw.Draw(image)
    for i in range(height):
        black_intensity = 255 - i // 2
        color = (black_intensity, black_intensity, black_intensity, 180)
        draw.line([(0, i), (width, i)], fill=color)

    blurred_image = image.filter(ImageFilter.GaussianBlur(10))

    final_image = Image.alpha_composite(blurred_image, image)
    
    return final_image

def load_earth_logo():
    earth_logo = Image.open("earth_logo.png")  
    earth_logo = earth_logo.resize((40, 40), Image.LANCZOS)
    return ImageTk.PhotoImage(earth_logo)

card_canvas = Canvas(root, width=400, height=250)
card_canvas.pack()

glass_morphic_image = create_glass_morphic_background()

background_image = ImageTk.PhotoImage(glass_morphic_image)
card_canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

earth_logo_image = load_earth_logo()
card_canvas.create_image(350, 30, anchor=tk.NW, image=earth_logo_image)

card_canvas.create_text(200, 30, text="MasterCard", font=("Helvetica", 24, "bold"), fill="white")
card_canvas.create_text(200, 70, text="ATM Card", font=("Helvetica", 18), fill="white")
card_canvas.create_text(200, 110, text="Cardholder Name:", font=("Helvetica", 14), fill="white")
card_canvas.create_text(200, 130, text=Shami, font=("Helvetica", 14, "bold"), fill="white")
card_canvas.create_text(200, 160, text="Account Number: " + account_number, font=("Helvetica", 12), fill="white")
card_canvas.create_text(200, 180, text="Expiry Date: " + expiry_date, font=("Helvetica", 12), fill="white")
card_canvas.create_text(200, 200, text="PIN: " + pin_number, font=("Helvetica", 12), fill="white")

root.mainloop()
