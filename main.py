import math
import tkinter as tk
import ttkbootstrap as ttk

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("ich keine usen chatgpt")


        self.label = tk.Label(master, text="Input number")
        self.label.pack(padx=5, pady=5)

        self.parity = tk.Label(master)
        self.parity.pack()

        self.is_prime = tk.Label(master)
        self.is_prime.pack()

        self.is_square = tk.Label(master)
        self.is_square.pack()

        self.dividors = tk.Label(master)
        self.dividors.pack()

        self.entry = tk.Entry(master)
        self.entry.pack(padx=5, pady=5)

        self.button = tk.Button(master, text="Check parity", command=self.check_parity)
        self.button.pack(padx=5, pady=5)

        self.button2 = tk.Button(master, text="Check prime", command=self.check_if_prime)
        self.button2.pack(padx=5, pady=5)

        self.button3 = tk.Button(master, text="Check if squared", command=self.check_if_squared)
        self.button3.pack(padx=5, pady=5)

        self.button4 = tk.Button(master, text="Find dividors", command=self.find_dividors)
        self.button4.pack(padx=5, pady=5)

    def check_parity(self):
        try:
            number = int(self.entry.get())
            if number % 2 == 0:
                self.parity.config(text="Even")
            elif number % 2 == 1:
                self.parity.config(text="Odd")
        except ValueError:
            self.parity.config(text="Invalid input")

    def check_if_prime(self):
        try:
            number = int(self.entry.get())
            is_prime = self.is_prime_number(number)
            if is_prime:
                self.is_prime.config(text="Prime")
            elif not is_prime:
                self.is_prime.config(text="Not prime")
        except ValueError:
            self.is_prime.config(text="Invalid input")

    def check_if_squared(self):
        try:
            number = int(self.entry.get())
            sqrt_number = math.sqrt(number)
            if sqrt_number % 1 == 0:
                self.is_square.config(text="A square")
            elif sqrt_number % 1 != 0:
                self.is_square.config(text="Not a square")
        except ValueError:
            self.is_square.config(text="Invalid input")

    def find_dividors(self):
        try:
            number = int(self.entry.get())
            dividors = []
            prime_dividors = []
            for i in range(1, number + 1):
                if number % i == 0:
                    dividors.append(i)
                    if self.is_prime_number(i):
                        prime_dividors.append(i)
            result = "Dividors: "
            for i in range(len(prime_dividors)):
                result += str(prime_dividors[i]) + ", "
            self.dividors.config(text=result.strip(", "))
        except ValueError:
            self.dividors.config(text="Invalid input")

    def is_prime_number(self, num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True


root = ttk.Window(themename="solar")
gui = GUI(root)
root.mainloop()
