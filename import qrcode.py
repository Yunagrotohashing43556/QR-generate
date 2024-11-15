import tkinter as tk
import pyqrcode
import pyperclip
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk

def generate_qr():
    # ดึงลิงก์จากคลิปบอร์ด
    link = pyperclip.paste()
    
    if link:
        # สร้าง QR code
        qr = pyqrcode.create(link)
        
        # เปิด dialog ให้ผู้ใช้เลือกที่เก็บไฟล์
        file_path = filedialog.asksaveasfilename(defaultextension=".png", 
                                                 filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            # บันทึก QR code เป็นไฟล์ PNG
            qr.png(file_path, scale=6)

            # แสดงผล QR code บนหน้าต่าง
            img = Image.open(file_path)
            img = img.resize((200, 200), Image.Resampling.LANCZOS)
            img = ImageTk.PhotoImage(img)
            qr_label.config(image=img)
            qr_label.image = img

            messagebox.showinfo("สำเร็จ", "QR Code ถูกบันทึกเรียบร้อยแล้ว!")
        else:
            messagebox.showwarning("ข้อผิดพลาด", "การบันทึกถูกยกเลิก")
    else:
        messagebox.showwarning("ข้อผิดพลาด", "ไม่มีข้อมูลในคลิปบอร์ด")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("แอปสร้าง QR Code")
root.geometry("300x350")

# ปุ่มวางลิงก์จากคลิปบอร์ด
paste_button = tk.Button(root, text="วางลิงก์จากคลิปบอร์ด", command=generate_qr)
paste_button.pack(pady=20)

# ปุ่มตกลงเพื่อสร้าง QR Code
qr_label = tk.Label(root)
qr_label.pack(pady=20)

root.mainloop()
