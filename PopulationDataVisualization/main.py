import tkinter as tk
from tkinter import ttk

def main():

    # Tạo giao diện
    root = tk.Tk()
    root.geometry("1280x100")
    root.resizable(False, False)
    root.protocol("WM_DELETE_WINDOW", False)
    root.title("Trực quan hoá dữ liệu dân số thế giới")

    # Hàm select_function
    def select_function(selected_option):
        # Placeholder for your functionality based on the selected option
        if selected_option == 'Biểu đồ đường thời gian cho một quốc gia cụ thể':
            root.destroy()
            import SingleCountry as sc
            sc.main()
            pass
        elif selected_option == 'So sánh sự phát triển giữa hai hoặc nhiều quốc gia theo biểu đồ đường thời gian':
            root.destroy()
            import CompareRegions as cr
            cr.main()
            pass

    # Tạo dropdown menu để chọn chức năng
    function_var = tk.StringVar()
    function_label = tk.Label(root, text="Chọn chức năng:")
    function_label.grid(row=0, column=0, padx=10, pady=10)

    function_dropdown = ttk.Combobox(root, width=100, textvariable=function_var)
    function_dropdown['values'] = ('Biểu đồ đường thời gian cho một quốc gia cụ thể',
                                'So sánh sự phát triển giữa hai hoặc nhiều quốc gia theo biểu đồ đường thời gian')
    function_dropdown.grid(row=0, column=1, padx=10, pady=10)
    function_dropdown.current(0)

    # Nút để chọn chức năng
    function_button = tk.Button(root, text="Chọn", command=lambda: select_function(function_var.get()))
    function_button.grid(row=0, column=2, padx=10, pady=10)
    def destroy():
        root.destroy()
        exit()
    # Tạo nút để thoát
    exit_button = tk.Button(root, text="Thoát", command=destroy)
    exit_button.grid(row=1, column=1, padx=10, pady=10)
    root.mainloop()

if __name__ == '__main__':
    main()