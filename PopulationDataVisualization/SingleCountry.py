import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

# Đọc dữ liệu từ DataFrame
df = pd.read_csv('population.csv')

# Tạo danh sách các quốc gia unique và loại bỏ dấu ' ' để khi thêm dropbox vào GUI sẽ không bị lỗi
country_list = [code.strip() for code in df['Country Code'].unique()]
def main(): # Hàm main
    def plot_data():
        # Kiểm tra xem người dùng đã chọn quốc gia hay chưa
        if country_var.get() == '':
            tk.messagebox.showerror("Lỗi", "Vui lòng chọn một quốc gia.")
            return
        # Lấy quốc gia được chọn từ dropdown menu
        selected_country = country_var.get()
        # Lọc dữ liệu của quốc gia được chọn
        country_data = df[df['Country Code'] == selected_country]
        # Chỉnh kích thước biểu đồ
        fig, ax = plt.subplots(figsize=(12, 6))
        # Vẽ biểu đồ đường
        ax.plot(country_data['Year'], country_data['Value'], marker='o')
        # Đặt tiêu đề cho biểu đồ
        ax.set_title(f'Sự phát triển dân số của {selected_country} - {df[df["Country Code"] == selected_country]["Country Name"].values[0]} giai đoạn 1960-2021')
        # Đặt tên cho trục x và y
        ax.set_xlabel('Năm')
        ax.set_ylabel('Dân số')
        # Hiển thị lưới
        ax.grid(True)

        # Tạo FigureCanvasTkAgg để embed biểu đồ vào Tkinter
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=3, column=0, padx=10, pady=10)
        canvas.draw()
        def print_graph():
            # Chọn địa chỉ lưu
            file_path = tk.filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG File", "*.png")])
            # Nếu không chọn địa chỉ lưu thì không làm gì cả
            if not file_path:
                return
            # Lưu biểu đồ
            fig.savefig(file_path)

        # Tạo nút để vẽ biểu đồ khi nhấn
        plot_button = tk.Button(root, text="In đồ thị", command=print_graph)
        plot_button.grid(row=1, column=1, padx=10, pady=10)

        

    # Tạo cửa sổ chính
    root = tk.Tk()

    # Đặt kích thước và tiêu đề cho cửa sổ
    root.geometry("1280x720")
    root.resizable(False, False)
    root.title("Trực quan hoá dữ liệu dân số thế giới")

    # Tạo text label
    label = tk.Label(root, text="Xin vui lòng chọn quốc gia bạn muốn vẽ đồ thị:")
    label.grid(row=0, column=0, padx=0, pady=0)

    # Tạo dropdown menu cho việc chọn quốc gia
    country_var = tk.StringVar()
    country_dropdown = ttk.Combobox(root, textvariable=country_var, values=country_list)
    country_dropdown.grid(row=1, column=0, padx=0, pady=0)
    country_dropdown.current(0)

    # Tạo nút để vẽ biểu đồ khi nhấn
    plot_button = tk.Button(root, text="Xem", command=plot_data)
    plot_button.grid(row=2, column=0, padx=10, pady=10)
    #Close window
    def close_window():
        root.destroy()
        import main
        main.main()
    # Tạo nút để bật main.py
    back_button = tk.Button(root, text="Quay lại", command=close_window)
    back_button.grid(row=2, column=1, padx=10, pady=10)
    # Hiển thị cửa sổ chính
    def destroy():
        root.destroy()
        exit()
    # Tạo nút để thoát
    exit_button = tk.Button(root, text="Thoát", command=destroy)
    exit_button.grid(row=0, column=1, padx=10, pady=10)
    root.mainloop()
