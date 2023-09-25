import tkinter as tk
from tkinter import messagebox, simpledialog
import os

def append_data(file_name):
    try:
        continue_adding_data = True

        with open(file_name, 'a') as file_writer:
            while continue_adding_data:
                name = simpledialog.askstring("Input", "Enter name:")
                age = simpledialog.askinteger("Input", "Enter age:")
                street_number = simpledialog.askstring("Input", "Enter street number:")
                street_name = simpledialog.askstring("Input", "Enter street name:")
                city = simpledialog.askstring("Input", "Enter city:")
                zip_code = simpledialog.askstring("Input", "Enter zip code:")
                phone_number = simpledialog.askstring("Input", "Enter phone number")

                data = f"{name},{age},{street_number},{street_name},{city},{zip_code},{phone_number}\n"
                file_writer.write(data)
                file_writer.flush()

                messagebox.showinfo("Info", "Data added to " + file_name)

                response = messagebox.askyesno("Continue?", "Do you want to add more data?")
                if not response:
                    continue_adding_data = False

    except Exception as e:
        print(f"An error occurred while appending data: {str(e)}")
        messagebox.showerror("Error", "An error occurred. Check the console for details.")

def create_new_list():
    file_name = "user_data.csv"
    
    try:
        with open(file_name, 'w') as file_writer:
            file_writer.write("name,age,streetNumber,streetName,city,zipCode,phoneNumber\n")
            messagebox.showinfo("Info", "New list created in " + file_name)
            
        response = messagebox.askyesno("Fill List", "Do you want to fill the new list now?")
        if response:
            append_data(file_name)
    except Exception as e:
        print(f"An error occurred while creating a new list: {str(e)}")
        messagebox.showerror("Error", "An error occurred. Check the console for details.")

def main():
    window = tk.Tk()
    window.title("CSV Creator Menu")
    
    create_list_button = tk.Button(window, text="Create a New List", command=create_new_list)
    append_data_button = tk.Button(window, text="Append Elements to Existing List", command=lambda: append_data("user_data.csv"))
    
    create_list_button.pack(pady=10)
    append_data_button.pack(pady=10)
    
    window.mainloop()

if __name__ == "__main__":
    main()
