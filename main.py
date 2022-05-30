
import random
import tkinter as tk

BASE_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
CAPITAL_ALPHABET = BASE_ALPHABET.upper()
NUMBERS = "1234567890"
SPECIAL_CHARS = "!@#$%^&*()_+-=/?.,"


def generate_password(length, with_capital=False, with_numbers=False, with_special_chars=False):
    passw = ""
    alphabet = "" + BASE_ALPHABET
    if with_capital:
        alphabet += CAPITAL_ALPHABET
    if with_numbers:
        alphabet += NUMBERS
    if with_special_chars:
        alphabet += SPECIAL_CHARS

    for _ in range(length):
        passw += random.choice(alphabet)

    return passw


def main():
    root = tk.Tk()
    root.title("Password Generator")
    root.resizable(0, 0)

    options_frame = tk.Frame(root)

    # Password length
    tk.Label(options_frame, text="Pass length: ").grid(column=0, row=0)

    iv_length = tk.IntVar()
    iv_length.set(10)
    options = list(range(5, 21))
    length = tk.OptionMenu(options_frame, iv_length, *options)
    length.grid(column=1, row=0, columnspan=2)

    # Capitals
    bv_capitals = tk.BooleanVar()
    capitals = tk.Checkbutton(options_frame, text="A/a", variable=bv_capitals)
    capitals.grid(column=0, row=1)

    # Numbers
    bv_numbers = tk.BooleanVar()
    numbers = tk.Checkbutton(options_frame, text="123", variable=bv_numbers)
    numbers.grid(column=1, row=1)

    # Spectials
    bv_specials = tk.BooleanVar()
    spectials = tk.Checkbutton(options_frame, text="@!#", variable=bv_specials)
    spectials.grid(column=2, row=1)

    options_frame.pack(padx=25, pady=10)

    btn_generate = tk.Button(root, text="Generate!")
    btn_generate.pack(padx=15, pady=15)

    sv_password = tk.StringVar()
    et_password = tk.Entry(root, textvariable=sv_password, width=50)
    et_password.pack(padx=15, pady=25)

    def on_btn_generate_command():
        passw = generate_password(
            iv_length.get(),
            bv_capitals.get(),
            bv_numbers.get(),
            bv_specials.get()
        )

        sv_password.set(passw)

    btn_generate.configure(command=on_btn_generate_command)

    root.mainloop()


if __name__ == '__main__':
    main()
