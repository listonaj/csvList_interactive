import tkinter as tk
import csv

def append_data():
    name = name_entry.get()
    age = age_entry.get()
    street_number = street_number_entry.get()
    street_name = street_name_entry.get()
    city = city_entry.get()
    zip_code = zip_code_entry.get()
    phone_number = phone_number_entry.get()

    with open('user_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(['name', 'age', 'street_number', 'street_name', 'city', 'zip_code', 'phone_number'])
        writer.writerow([name, age, street_number, street_name, city, zip_code, phone_number])

    result_label.config(text="Data added to user_data.csv")

def create_new_list():
    with open('user_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'age', 'street_number', 'street_name', 'city', 'zip_code', 'phone_number'])
    result_label.config(text="New list created in user_data.csv")

def exit_program():
    root.destroy()

root = tk.Tk()
root.title("CSV Creator")

menu_label = tk.Label(root, text="Choose an option:")
menu_label.pack()

append_button = tk.Button(root, text="Append data to an existing list", command=append_data)
append_button.pack()

create_button = tk.Button(root, text="Create a new list", command=create_new_list)
create_button.pack()

exit_button = tk.Button(root, text="Exit", command=exit_program)
exit_button.pack()

name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

age_label = tk.Label(root, text="Age:")
age_label.pack()
age_entry = tk.Entry(root)
age_entry.pack()

street_number_label = tk.Label(root, text="Street Number:")
street_number_label.pack()
street_number_entry = tk.Entry(root)
street_number_entry.pack()

street_name_label = tk.Label(root, text="Street Name:")
street_name_label.pack()
street_name_entry = tk.Entry(root)
street_name_entry.pack()

city_label = tk.Label(root, text="City:")
city_label.pack()
city_entry = tk.Entry(root)
city_entry.pack()

zip_code_label = tk.Label(root, text="Zip Code:")
zip_code_label.pack()
zip_code_entry = tk.Entry(root)
zip_code_entry.pack()

phone_number_label = tk.Label(root, text="Phone Number:")
phone_number_label.pack()
phone_number_entry = tk.Entry(root)
phone_number_entry.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
