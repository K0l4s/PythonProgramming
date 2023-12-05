import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk
def main():
    # Đọc dữ liệu từ DataFrame
    df = pd.read_csv('population.csv')
    # So sanh su phat trien giua hai hoac nhieu quoc gia
    def compare_countries():
        # Biến input thành chuỗi
        country_list = country_var.get().split(',')
        # Xoá khoảng trắng thừa ở đầu và cuối chuỗi
        country_list = [code.strip() for code in country_list]
        # Kiểm tra list rỗng hoặc chỉ có 1 quốc gia thì báo lỗi
        if country_list == [''] or len(country_list) == 1:
            tk.messagebox.showerror("Lỗi", "Vui lòng chọn ít nhất hai quốc gia.")
            return
        # Lay du lieu cua cac quoc gia duoc chon
        country_data = df[df['Country Code'].isin(country_list)]
        # Tao figure
        plt.figure(figsize=(12, 6))
        # Ve bieu do
        for country in country_list:
            plt.plot(country_data[country_data['Country Code'] == country]['Year'], country_data[country_data['Country Code'] == country]['Value'], marker='o', label=country)
        # Dat tieu de cho bieu do
        plt.title('So sánh dân số của các quốc gia trong giai đoạn 1960-2021')
        # Dat ten cho truc x va y
        plt.xlabel('Năm')
        plt.ylabel('Dân số')
        # Hien thi chu thich
        plt.legend()
        # Hien thi luoi
        plt.grid(True)
        # Hien thi bieu do
        # plt.show()
        # Tạo canvas
        canvas = FigureCanvasTkAgg(plt.gcf(), master=root)
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
            plt.gcf().savefig(file_path)
        # Tạo nút để vẽ biểu đồ khi nhấn
        plot_button = tk.Button(root, text="In đồ thị", command=print_graph)
        plot_button.grid(row=1, column=1, padx=10, pady=10)

    # Tạo giao diện
    root = tk.Tk()
    # Đặt kích thước và tiêu đề cho cửa sổ
    root.geometry("1280x720")
    root.resizable(False, False)
    root.protocol("WM_DELETE_WINDOW", False)
    root.title("Trực quan hoá dữ liệu dân số thế giới")
    # Tạo một input nhập vào chuỗi quốc gia
    country_var = tk.StringVar()
    country_label = tk.Label(root, text="Nhập mã code quốc gia, cách nhau bởi dấu phẩy(vd: AGO,ABW): ")
    country_label.grid(row=0, column=0, padx=10, pady=10)
    country_entry = tk.Entry(root, textvariable=country_var)
    country_entry.grid(row=1, column=0, padx=10, pady=10)


    # Tạo nút để so sánh
    compare_button = tk.Button(root, text="So sánh", command=lambda: compare_countries())
    compare_button.grid(row=2, column=0, padx=10, pady=10)

    def destroy():
        root.destroy()
        exit()
    # Tạo nút để thoát
    exit_button = tk.Button(root, text="Thoát", command=destroy)
    exit_button.grid(row=1, column=1, padx=10, pady=10)
    #Close window
    def close_window():
        root.destroy()
        import main
        main.main()
    # Tạo nút để bật main.py
    back_button = tk.Button(root, text="Quay lại", command=close_window)
    back_button.grid(row=2, column=1, padx=10, pady=10)
    root.mainloop()

