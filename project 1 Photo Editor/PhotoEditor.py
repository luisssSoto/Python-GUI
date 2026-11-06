import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont

# CONSTANTS
BLUE = "#306998"
LIGHT_BLUE = "#4B8BBE"
YELLOW = "#FFD43B"
LIGHT_YELLOW = "#FFE873"
GRAY = "#646464"
FONT_NAME = "Courier"


class PhotoEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Photo Editor")
        self.root.geometry("850x700")
        self.root.config(padx=100, pady=50, bg=LIGHT_YELLOW)

        self.original_image = None
        self.edited_image = None
        self.logo_image = None
        self.preview_photo = None

        # ---------- CONTROLS ----------
        controls = tk.Frame(root)
        controls.pack(pady=20)
        controls.config(bg=BLUE)

        tk.Button(
            controls, text="Upload Photo",
            command=self.upload_photo,
            bg=YELLOW
        ).grid(row=0, column=0, padx=5, pady=5)

        tk.Button(
            controls, text="Upload Logo",
            command=self.upload_logo,
            bg=YELLOW
        ).grid(row=0, column=1, padx=5, pady=5)

        self.text_entry = tk.Entry(controls, width=25)
        self.text_entry.grid(row=0, column=2, padx=5, pady=5)
        self.text_entry.insert(0, "Your text here")

        tk.Button(
            controls, text="Add Text",
            command=self.add_text,
            bg=YELLOW
        ).grid(row=0, column=3, padx=5, pady=5)

        tk.Button(
            controls, text="Add Logo",
            command=self.add_logo,
            bg=YELLOW
        ).grid(row=1, column=0, padx=5, pady=5)

        tk.Button(
            controls, text="Reset",
            command=self.reset_image,
            bg=YELLOW
        ).grid(row=1, column=1, padx=5, pady=5)

        tk.Button(
            controls, text="Save Photo",
            command=self.save_photo,
            bg=YELLOW
        ).grid(row=1, column=2, padx=5, pady=5)

        # ---------- IMAGE PREVIEW ----------
        self.image_label = tk.Label(
            root,
            text="Upload a photo to get started",
            bg=LIGHT_BLUE,
            width=80,
            height=25,
            fg=GRAY
        )
        self.image_label.pack(padx=15, pady=15)

    def upload_photo(self):
        '''upload an image to edit'''
        path = filedialog.askopenfilename(
            title="Choose a photo",
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.webp *.bmp")])
        if not path:
            return
        try:
            with Image.open(path) as image:
                self.original_image = image.convert("RGBA")
            self.reset_image()
            messagebox.showinfo("Success", "Your photo was uploaded successfully!")
        except (OSError, ValueError) as error:
            messagebox.showerror("Error", f"Could not open your image:\n{error}")

    def upload_logo(self):
        '''upload a logo'''
        path = filedialog.askopenfilename(
            title="Choose a logo",
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.webp")])
        if not path:
            return
        try:
            with Image.open(path) as image:
                self.logo_image = image.convert("RGBA")
            messagebox.showinfo("Success", "Logo uploaded successfully!")
        except (OSError, ValueError) as error:
            messagebox.showerror("Error", f"Could not open logo:\n{error}")

    def show_preview(self):
        '''show the image's preview to edit'''
        if self.edited_image is None:
            return
        preview = self.edited_image.copy()
        preview.thumbnail((760, 480))
        self.preview_photo = ImageTk.PhotoImage(preview)
        self.image_label.config(
            image=self.preview_photo,
            text="Preview: ",
            width=1200,
            height=1200
            )

    def add_text(self):
        '''add text to the image'''
        if self.edited_image is None:
            messagebox.showwarning("Warning", "Upload a photo first.")
            return
        text = self.text_entry.get().strip()
        if not text:
            messagebox.showwarning("Warning", "Enter some text first.")
            return
        image = self.edited_image.copy()
        draw = ImageDraw.Draw(image)
        font_size = max(20, image.width // 25)
        try:
            font = ImageFont.truetype(FONT_NAME, font_size)
        except OSError:
            font = ImageFont.load_default(size=font_size)
        x = int(image.width * 0.04)
        y = int(image.height * 0.88)
        draw.text(
            (x, y),
            text,
            font=font,
            fill="white",
            stroke_width=max(1, font_size // 15),
            stroke_fill="black"
        )
        self.edited_image = image
        self.show_preview()

    def add_logo(self):
        '''add the logo to add to the image'''
        if self.edited_image is None:
            messagebox.showwarning("Warning", "Upload a photo first.")
            return
        if self.logo_image is None:
            messagebox.showwarning("Warning", "Upload a logo first.")
            return
        image = self.edited_image.copy()
        logo = self.logo_image.copy()
        logo_width = max(1, image.width // 5)
        logo_height = max(1, round(logo.height * logo_width / logo.width))
        logo.thumbnail((logo_width, logo_height), Image.Resampling.LANCZOS)
        margin = max(10, image.width // 40)
        x = image.width - logo.width - margin
        y = image.height - logo.height - margin
        image.alpha_composite(logo, (x, y))
        self.edited_image = image
        self.show_preview()

    def reset_image(self):
        '''reset any changes on your image to the original version'''
        if self.original_image is None:
            return
        self.edited_image = self.original_image.copy()
        self.show_preview()

    def save_photo(self):
        if self.edited_image is None:
            messagebox.showwarning("Warning", "Upload a photo first.")
            return
        path = filedialog.asksaveasfilename(
            title="Save edited photo",
            defaultextension=".png",
            filetypes=[
                ("PNG image", "*.png"),
                ("JPEG image", "*.jpg")])
        if not path:
            return
        try:
            image = self.edited_image
            if path.lower().endswith((".jpg", ".jpeg")):
                image = image.convert("RGB")
            image.save(path)
            messagebox.showinfo("Success", "Photo saved successfully!")
        except (OSError, ValueError) as error:
            messagebox.showerror("Error", f"Could not save photo:\n{error}")
