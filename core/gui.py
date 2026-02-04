import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2

class AppGUI:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Image Editor")

        self.image_label = tk.Label(root)
        self.image_label.pack()

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=30)

        tk.Button(btn_frame, text="Open Image", command=self.open_image).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Grayscale", command=self.apply_grayscale).pack(side=tk.LEFT, padx=5)

        self.tk_image = None

    def open_image(self):
        path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.jpg *.png *.bmp")]
        )
        if not path:
            return

        image = self.controller.load_image(path)
        self.display_image(image)

    def apply_grayscale(self):
        image = self.controller.apply_grayscale()
        if image is None:
            messagebox.showerror("Error", "No image loaded")
            return
        self.display_image(image)

    def display_image(self, cv_image):
        rgb = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(rgb).resize((500, 400))
        self.tk_image = ImageTk.PhotoImage(pil_image)
        self.image_label.config(image=self.tk_image)
