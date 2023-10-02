import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import phanTichInput as pt
import numpy as np

import numpy as np

# def chuanHoaHamSo(func):
#     func = func.replace(" ", "")
#     #Sec vaf csec
#     func = func.replace("csc", "1/sin")
#     func = func.replace("sec", "1/cos")
    
#     #sin cos tan và cotg
#     func = func.replace("sin", "np.sin")
#     func = func.replace("cos", "np.cos")
#     func = func.replace("tan", "np.tan")
#     func = func.replace("cotg", "1/np.tan") 

#     #căn bậc 2
#     func = func.replace("sqrt", "np.sqrt")
#     func = func.replace("√", "np.sqrt")
#     #logarit
#     func = func.replace("log2", "np.log2")
#     func = func.replace("log10", "np.log10")
#     func = func.replace("log", "np.log")

#     #exp
#     func = func.replace("exp", "np.exp")
#     func = func.replace("e", "np.e")
#     #pi
#     func = func.replace("pi", "np.pi")
#     #lũy thừa
#     func = func.replace("^", "**")
#     #arcsin, arccos, arctan
#     func = func.replace("arcnp.sin", "np.arcsin")
#     func = func.replace("arcnp.cos", "np.arccos")
#     func = func.replace("arcnp.tan", "np.arctan")
#     #arccotg
#     func = func.replace("arc1/np.tan", "np.arctan(1/np.tan")
    
#     if func.find("=") != -1:
#         func = func.split("=")
#         func = func[0] + "-(" + func[1] + ")"
#     print(func)
#     return func



# Hàm để vẽ đồ thị
def plot_graph():
    # Lấy biểu thức hàm số được nhập từ người dùng
    function_str = entry_function.get()
    new_str=pt.chuanHoaHamSo(function_str)
    try:
        # Tạo một mảng các giá trị x từ -10 đến 10
        x = np.linspace(-10, 10, 400)
        
        # Biểu thức hàm số
        y = eval(new_str)

        # Xóa đồ thị cũ (nếu có)
        ax.clear()

        # Vẽ đồ thị
        ax.plot(x, y, label=function_str)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.legend()
        ax.grid()
        ax.set_title('Biểu đồ của hàm số')

        # Cập nhật đồ thị trên giao diện
        canvas.draw()
    except Exception as e:
        error_label.config(text=f"Lỗi: {str(e)}")

# Tạo cửa sổ giao diện
root = tk.Tk()
root.title("Vẽ Đồ Thị Hàm Số")

# Label
label = tk.Label(root, text="Nhập hàm số (ví dụ: sin(x), cos(x), tan(x)):")
label.pack()

# Ô nhập liệu cho hàm số
entry_function = tk.Entry(root)
entry_function.pack()

# Nút vẽ đồ thị
plot_button = tk.Button(root, text="Vẽ Đồ Thị", command=plot_graph)
plot_button.pack()

# Label hiển thị lỗi (nếu có)
error_label = tk.Label(root, text="", fg="red")
error_label.pack()

# Tạo đối tượng Figure của Matplotlib
fig = Figure(figsize=(6, 4), dpi=100)
ax = fig.add_subplot(111)

# Tạo canvas để hiển thị đồ thị trong giao diện Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Chạy ứng dụng
root.mainloop()