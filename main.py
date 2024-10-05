import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Validate input to ensure only digits and decimal points are entered
def validate_input(char):
    return char.isdigit() or char == "."  # Allow decimal input

# Function to perform conversions based on the selected unit
def calc():
    # Fetch input values and try to convert to float; if error, show "Invalid input"
    try:
        input_value1 = float(input1.get())
        input_value2 = float(input2.get())
    except ValueError:
        output1.config(text="Invalid input")
        output2.config(text="Invalid input")
        return

    imglabel.config(image=img1, bg='lightgrey')  # Change image when calculation occurs

    # Perform conversions based on the selected converter
    if new.get() == 'Feet and Meters':
        answer1 = input_value1 * 0.3048  # Feet to meters
        answer2 = input_value2 * 3.281   # Meters to feet
        output1.config(text=f"--> {answer1:.2f} m")
        output2.config(text=f"--> {answer2:.2f} ft")
    elif new.get() == 'Inches and Centimeters':
        answer1 = input_value1 * 2.54  # Inches to centimeters
        answer2 = input_value2 / 2.54  # Centimeters to inches
        output1.config(text=f"--> {answer1:.2f} cm")
        output2.config(text=f"--> {answer2:.2f} in")
    elif new.get() == 'Miles and Kilometers':
        answer1 = input_value1 * 1.60934  # Miles to kilometers
        answer2 = input_value2 / 1.609  # Kilometers to miles
        output1.config(text=f"--> {answer1:.2f} km")
        output2.config(text=f"--> {answer2:.2f} mi")
    elif new.get() == 'Fahrenheit and Celsius':
        answer1 = (input_value1 - 32) * 5 / 9  # Fahrenheit to Celsius
        answer2 = (input_value1 * 9/5) + 32    # Celsius to Fahrenheit
        output1.config(text=f"--> {answer1:.2f} °C")
        output2.config(text=f"--> {answer2:.2f} °F")
    elif new.get() == 'Pounds and Kilograms':
        answer1 = input_value1 * 0.453592  # Pounds to kilograms
        answer2 = input_value2 * 2.205     # Kilograms to pounds
        output1.config(text=f"--> {answer1:.2f} kg")
        output2.config(text=f"--> {answer2:.2f} lbs")
    else:
        output1.config(text="")
        output2.config(text="")

main = tk.Tk()  # Create the main window
main.title("Global and Freedom Units Converter")
main.iconbitmap('penguin_icon.ico')  # Set window icon
main.geometry('600x400')  # Set window size
main.configure(bg="lightgrey")  # Set background color

# Load images for use in the UI
image = Image.open('shrug.jpg')
img = ImageTk.PhotoImage(image)
image1 = Image.open('approved.jpg')
img1 = ImageTk.PhotoImage(image1)

style = ttk.Style()  # Configure styles for buttons and labels
style.configure("TButton", font=("Helvetica", 12, "bold"), padding=10)
style.configure("TLabel", font=("Helvetica", 20, "bold"), background="lightgrey", foreground="darkblue")

# Create and place the label for the combobox (converter choices)
startlabel = ttk.Label(main, text="Choose a converter")
startlabel.grid(row=0, column=0, columnspan=3, pady=12, sticky='nsew')

# Combobox to select the conversion type
new = ttk.Combobox(main, values=['Feet and Meters', 'Inches and Centimeters', 'Miles and Kilometers',
                                 'Fahrenheit and Celsius', 'Pounds and Kilograms'], state="readonly", width=30)
new.grid(row=1, column=0, columnspan=3, pady=20, sticky='nsew')
new.set("Select a converter")  # Default text for the combobox

# Update the displayed units based on the selected converter
def get_comboboxvalue():
    if new.get() == 'Feet and Meters':
        unit1.config(text="ft")
        unit2.config(text="m")
    elif new.get() == 'Inches and Centimeters':
        unit1.config(text="in")
        unit2.config(text="cm")
    elif new.get() == 'Miles and Kilometers':
        unit1.config(text="mi")
        unit2.config(text="km")
    elif new.get() == 'Fahrenheit and Celsius':
        unit1.config(text="°F")
        unit2.config(text="°C")
    elif new.get() == 'Pounds and Kilograms':
        unit1.config(text="lb")
        unit2.config(text="kg")

# Button to submit the conversion type selection
submit = ttk.Button(main, text="Submit", command=get_comboboxvalue)
submit.grid(row=2, column=0, columnspan=3, pady=30, sticky='nsew')

# Input validation for entries
vcmd = (main.register(validate_input), '%S')

# Labels and entry fields for input and output values
label1 = tk.Label(main, text="Freedom value", bg='lightgrey')
label1.grid(row=3, column=0, padx=10, pady=10)

input1 = tk.Entry(main, validate="key", validatecommand=vcmd)  # Entry for first value
input1.grid(row=3, column=1, padx=10, pady=10)

unit1 = tk.Label(main, text="", bg='lightgrey')  # Display unit for first value
unit1.grid(row=3, column=2, pady=10)

output1 = tk.Label(main, text="", bg='lightgrey')  # Output for first value
output1.grid(row=3, column=3, padx=10, pady=10)

label2 = tk.Label(main, text="Global value", bg='lightgrey')
label2.grid(row=4, column=0, padx=10, pady=10)

input2 = tk.Entry(main, validate="key", validatecommand=vcmd)  # Entry for second value
input2.grid(row=4, column=1, padx=10, pady=10)

unit2 = tk.Label(main, text="", bg='lightgrey')  # Display unit for second value
unit2.grid(row=4, column=2, pady=10)

output2 = tk.Label(main, text="", bg='lightgrey')  # Output for second value
output2.grid(row=4, column=3, padx=10, pady=10)

# Button to trigger the calculation
calcbutton = ttk.Button(main, text="Calculate", command=calc)
calcbutton.grid(row=5, column=1, columnspan=1, padx=10, pady=10, stick="nsew")

# Label to display image
imglabel = tk.Label(main, image=img, bg='lightgrey')
imglabel.grid(row=0, column=4, rowspan=5, sticky="nsew")

main.mainloop()  # Run the main event loop
