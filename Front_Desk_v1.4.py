from tkinter import *
from tkinter import messagebox
import tkinter.scrolledtext as st

# Lines 7 - 10 Have the setup for login screen
LogInScreen = Tk()
LogInScreen.geometry("1000x600")
LogInScreen.title("Front Desk")
LogInScreen.config(bg="black")


def exit_p():
    exit()


# The function starting from line 18 will be used to
# go to the main screen where the Check in buttons and etc are provided

# ==============Start of Global variables ====================================
guest_info_text = ""
guestInfoList = []
list_of_guests = []
global front_dsk_screen
global checkInScreen
global checkOutScreen


# ===============End of Global Variables======================================

# =======================Start of Front Desk Screen===========================
def front_screen():
    global front_dsk_screen

    front_dsk_screen = Tk()
    front_dsk_screen.geometry("1000x600")
    LogInScreen.withdraw()

    def close_main_screen():
        front_dsk_screen.destroy()
        LogInScreen.deiconify()
        labelUser1.configure(bg="gray95")
        labelUser2.configure(bg="gray95")
        entryBox1.delete(0, 'end')
        entryBox2.delete(0, 'end')

    front_dsk_screen.title("WELCOME TO THE FRONT DESK")
    front_dsk_screen.config(bg="white")

    welcome_label = Label(front_dsk_screen, text="Welcome to the S. B. D. Systems",
                          width=50, height=2,
                          bg="#ad6f5e", fg="#454e57", font=("Copperplate", 25, "bold", "italic", "underline"))

    check_in_button = Button(front_dsk_screen, font=("Times New Roman", 25), width=40,
                             height=2, text="Check-In Guest", command=open_check_in_screen)
    guest_list_button = Button(front_dsk_screen, font=("Times New Roman", 25), width=40,
                               height=2, text="Visitor's list", command=view_list_of_guests)
    check_out_button = Button(front_dsk_screen, font=("Times New Roman", 25), width=40,
                              height=2, text=" Check-Out Guest", command=open_check_out_screen)
    hotel_contents = Button(front_dsk_screen, font=("Times New Roman", 25), width=40,
                            height=2, text="Hotel Contents", command=open_hotel_contents)
    back_button = Button(front_dsk_screen, font=("Times New Roman", 25), width=40,
                         height=2, text="Log out", command=close_main_screen)

    welcome_label.pack()
    check_in_button.pack()
    check_out_button.pack()
    guest_list_button.pack()
    hotel_contents.pack()
    back_button.pack()
    front_dsk_screen.mainloop()


# ===============================End of Front Desk Screen==================================
# ====================Start of Check In Screen=============================================
def open_check_in_screen():
    global checkInScreen

    checkInScreen = Tk()
    checkInScreen.geometry("625x625")
    checkInScreen.title("Check-In List")
    checkInScreen.configure(bg="white")
    front_dsk_screen.withdraw()

    # --------------------- variables --------------------------------
    pay_var = StringVar(master=checkInScreen)

    # ------------------- Start of functions -------------------------
    def do_checking():
        global guest_info_text

        check_in_output_text.config(state='normal')
        check_in_output_text.delete('0.0', END)
        check_in_output_text.config(state='disabled')

        guest_info_text = "Name: " + name_entry.get() + "\n" + "Address: " + address_entry.get() + "\n" + \
                          "Phone Number: " + phone_entry.get() + "\n" + "Room Type: " + room_list.get() + "\n" + \
                          "Room Number: " + room_num_entry.get() + "\n" + "Number of Days: " + num_day_entry.get() + \
                          "\n" + "Payment Type: " + pay_var.get()

        guest_info_list = [name_entry.get(), address_entry.get(), phone_entry.get(), room_list.get(),
                           room_num_entry.get(), num_day_entry.get(), pay_var.get()]
        list_of_guests.append(guest_info_list)

        name_entry.delete(0, "end")
        address_entry.delete(0, "end")
        phone_entry.delete(0, "end")
        room_num_entry.delete(0, "end")
        num_day_entry.delete(0, "end")
        pay_var.set("Credit")
        room_list.set(room_types[0])

        check_in_output_text.configure(state='normal')
        check_in_output_text.insert(INSERT, guest_info_text)
        check_in_output_text.configure(state='disabled')

    def close_check_in_screen():
        checkInScreen.destroy()
        front_dsk_screen.deiconify()

    # --------------------End of Functions-----------------------------

    check_in_output_text = st.ScrolledText(checkInScreen, border=2, width=30, height=8, font=("Times New Roman", 15))
    check_in_output_text.insert(INSERT, "Check In Message goes here")
    check_in_output_text.configure(state='disabled')

    name_label = Label(checkInScreen, text="Name:", font=("Times New Roman", 25), bg="white")
    address_label = Label(checkInScreen, text="Address:", bg="white", font=("Times New Roman", 25))
    phone_label = Label(checkInScreen, text="Phone Number:", bg="white", font=("Times New Roman", 25))
    room_type_label = Label(checkInScreen, text="Room type:", bg="white", font=("Times New Roman", 25))
    room_number_label = Label(checkInScreen, text="Room number:", bg="white", font=("Times New Roman", 25))
    num_day_label = Label(checkInScreen, text="Number of Days:", bg="white", font=("Times New Roman", 25))
    pay_method_label = Label(checkInScreen, text="Method of Payment", bg="white", font=("Times New Roman", 25))

    radio_button_cash = Radiobutton(checkInScreen, fg="black", text="Cash", variable=pay_var, value="Cash",
                                    bg="white", border="1", font=("Times New Roman", 25))
    radio_button_credit_card = Radiobutton(checkInScreen, fg="black", text="Credit Card", variable=pay_var,
                                           value="Credit",
                                           bg="white", border="1", font=("Times New Roman", 25))
    pay_var.set("Credit")

    name_entry = Entry(checkInScreen, fg="black", bg="white", border="1", font=("Times New Roman", 25))
    address_entry = Entry(checkInScreen, fg="black", bg="white", border="1", font=("Times New Roman", 25))
    phone_entry = Entry(checkInScreen, fg="black", bg="white", border="1", font=("Times New Roman", 25))
    room_num_entry = Entry(checkInScreen, fg="black", bg="white", border="1", font=("Times New Roman", 25))
    num_day_entry = Entry(checkInScreen, fg="black", bg="white", border="1", font=("Times New Roman", 25))

    check_in_button = Button(checkInScreen, text="Complete check-in", font=("Times New Roman", 25), command=do_checking)
    back_button_2 = Button(checkInScreen, text="Back to front desk", font=("Times New Roman", 25),
                           command=close_check_in_screen)

    room_types = ["Basic", "Premium", "Deluxe"]
    room_list = StringVar(checkInScreen)
    room_list.set(room_types[0])
    room_options = OptionMenu(checkInScreen, room_list, *room_types)
    room_options.config(fg="black", bg="white", font=("Times New Roman", 25))
    room_options.grid(row=4, column=2)

    name_label.grid(row=1, column=1)
    address_label.grid(row=2, column=1)
    phone_label.grid(row=3, column=1)
    room_type_label.grid(row=4, column=1)
    room_number_label.grid(row=5, column=1)
    num_day_label.grid(row=6, column=1)

    name_entry.grid(row=1, column=2)
    address_entry.grid(row=2, column=2)
    phone_entry.grid(row=3, column=2)
    room_num_entry.grid(row=5, column=2)
    num_day_entry.grid(row=6, column=2)

    pay_method_label.grid(row=7, column=1, columnspan=3)
    radio_button_cash.grid(row=8, column=1)
    radio_button_credit_card.grid(row=8, column=2)

    check_in_output_text.grid(row=9, column=1, columnspan=3)
    check_in_button.grid(row=10, column=1)
    back_button_2.grid(row=10, column=2)


# ================================End of Check In Screen================================
# ===============================Start of Check Out Screen==============================

def open_check_out_screen():
    global checkOutScreen

    checkOutScreen = Tk()
    checkOutScreen.geometry("520x565")
    checkOutScreen.title("Check-In List")
    checkOutScreen.configure(bg="white")
    front_dsk_screen.withdraw()

    # -----------------------Start of Functions------------------------------------------
    def close_check_out_screen():
        checkOutScreen.destroy()
        front_dsk_screen.deiconify()

    def find_guest_room():
        global guest_info_text

        room_info_text.config(state='normal')
        room_info_text.delete('0.0', END)
        room_info_text.config(state='disabled')

        for gst in list_of_guests:
            if gst[4] == room_num_entry.get():
                test = gst

                test.insert(0, 'Name:')
                test.insert(2, 'Address:')
                test.insert(4, 'Phone:')
                test.insert(6, 'Room:')
                test.insert(8, 'Number:')
                test.insert(10, 'Days:')

                room_info_text.configure(state='normal')
                room_info_text.insert(INSERT, test)
                room_info_text.configure(state='disabled')

                del test[0]
                del test[1]
                del test[2]
                del test[3]
                del test[4]
                del test[5]

    def complete_check_out():
        global guest_info_text

        check_out_output_text.config(state='normal')
        check_out_output_text.delete('0.0', END)
        check_out_output_text.config(state='disabled')

        for gst in list_of_guests:
            if gst[4] == room_num_entry.get():
                list_of_guests.remove(gst)

                check_out_output_text.config(state='normal')
                check_out_output_text.insert(INSERT, "The selected room has been deleted \nThank you for visiting our "
                                                     "hotel!")
                check_out_output_text.config(state='disabled')

    # ---------------------End of Functions ---------------------------------------------

    room_info_text = st.ScrolledText(checkOutScreen, border=2, width=30, height=8, font=("Times New Roman", 15))
    room_info_text.insert(INSERT, "Room info is shown here")
    room_info_text.configure(state='disabled')

    check_out_output_text = st.ScrolledText(checkOutScreen, border=2, width=30, height=8, font=("Times New Roman", 15))
    check_out_output_text.insert(INSERT, """Check Out Message goes here""")
    check_out_output_text.configure(state='disabled')

    room_num_label = Label(checkOutScreen, text="Enter room number:", font=("Times New Roman", 20), fg="black",
                           bg="white")
    room_num_entry = Entry(checkOutScreen, fg="black", bg="white", border="2", font=("Times New Roman", 20))
    check_room_button = Button(checkOutScreen, fg="black", bg="white", border="2", font=("Times New Roman", 20),
                               text="Check Room", command=find_guest_room)
    check_out_confirm_button = Button(checkOutScreen, fg="black", bg="white", border="2", font=("Times New Roman", 20),
                                      text="Confirm Check Out", command=complete_check_out)
    back_button_3 = Button(checkOutScreen, width=30, text="Back to front desk", bg="white", font=("Times New Roman", 20),
                           border="2", command=close_check_out_screen)

    room_num_label.grid(row=1, column=1)
    room_num_entry.grid(row=1, column=2)
    check_room_button.grid(row=2, column=1, columnspan=2)
    room_info_text.grid(row=3, column=1, columnspan=2)
    check_out_confirm_button.grid(row=4, column=1, columnspan=2)
    check_out_output_text.grid(row=5, column=1, columnspan=2)
    back_button_3.grid(row=6, column=1, columnspan=2)


# ==============================End of Check Out Screen=================================
# ==============================Start List Of Guests Page===============================

def view_list_of_guests():
    global checkInScreen

    list_of_guests_page = Tk()
    list_of_guests_page.geometry("750x400")
    list_of_guests_page.title("list Of Guests Page")
    list_of_guests_page.configure(bg="white")
    front_dsk_screen.withdraw()

    # ------------------- functions -------------------------
    def show_guest_list():
        global guest_info_text

        for gst in list_of_guests:
            y = str(gst) + ', \n'

            guest_information_text.configure(state='normal')
            guest_information_text.insert(INSERT, "\n")
            guest_information_text.insert(INSERT, y)
            guest_information_text.configure(state='disabled')

    def close_list_of_guests_page():
        guest_information_text.delete('0.0', END)
        guest_information_text.insert(INSERT, "Room info is shown here in the following format: \n['Name', 'Address',"
                                              " 'Phone Number',\n 'Room Type', 'Room Number',\n'Number of Days',"
                                              "\n'Method of Payment']\n")
        list_of_guests_page.destroy()
        front_dsk_screen.deiconify()

    # --------------------End of Functions------------------

    guest_information_text = st.ScrolledText(list_of_guests_page, border=2, width=70, height=8,
                                             font=("Times New Roman", 15))
    guest_information_text.insert(INSERT, "Room info is shown here in the following format: \n['Name', 'Address',"
                                          " 'Phone Number', 'Room Type', 'Room Number', 'Number of Days',"
                                          "\n'Method of Payment']\n")
    guest_information_text.configure(state='disabled')

    guest_info_filler_label_a = Label(list_of_guests_page, bg="white", font=("Times New Roman", 25))
    guest_info_filler_label_b = Label(list_of_guests_page, bg="white", font=("Times New Roman", 25))

    show_button = Button(list_of_guests_page, text="Show guest list", font=("Times New Roman", 25),
                         command=show_guest_list)
    close_button = Button(list_of_guests_page, text="Back to front desk", font=("Times New Roman", 25),
                          command=close_list_of_guests_page)
    current_visitor_list_label = Label(list_of_guests_page, text="Current List of Guests:",
                                       font=("Times New Roman", 25),
                                       bg="white", fg="black")

    current_visitor_list_label.grid(row=1, column=1, columnspan=2)
    guest_information_text.grid(row=2, column=1, columnspan=2)
    guest_info_filler_label_a.grid(row=3, column=1)
    guest_info_filler_label_b.grid(row=3, column=2)
    show_button.grid(row=4, column=1, columnspan=2)
    close_button.grid(row=5, column=1, columnspan=2)


# ================================End of List Of Guests Page================================
# ===================================Start of Hotel Contents================================

def open_hotel_contents():
    hotel_contents_screen = Tk()
    hotel_contents_screen.geometry("680x375")
    hotel_contents_screen.title("list Of Guests Page")
    hotel_contents_screen.configure(bg="white")
    front_dsk_screen.withdraw()

    # SELECT ROOM BUTTON
    def show_output(bob):
        tempt = option_var.get()
        if tempt == "Basic":
            room_cost_label.config(text="$10")
        if tempt == "Premium":
            room_cost_label.config(text="$25")
        if tempt == "Deluxe":
            room_cost_label.config(text="$99")

    def close_hotel_contents():
        hotel_contents_screen.destroy()
        front_dsk_screen.deiconify()

    # LABELS
    room_price_label = Label(hotel_contents_screen, text="Room Price:", bg="white", fg="black",
                             font=("Times New Roman", 25))
    per_person_label = Label(hotel_contents_screen, text="Per Person:", bg="white", fg="black",
                             font=("Times New Roman", 25))
    per_person_cost_label = Label(hotel_contents_screen, text="$20", bg="white", fg="black",
                                  font=("Times Now Roman", 25))
    hotel_note_label = Label(hotel_contents_screen, bg="white", fg="black", font=("Times New Roman", 25),
                             text="Note: The price of your chosen room is multiplied\nby the amount of days you chose "
                                  "to stay in this hotel")
    tax_rate_label = Label(hotel_contents_screen, text="Tax rate: 2%", bg="white", fg="black",
                           font=("Times New Roman", 25))
    room_cost_label = Label(hotel_contents_screen, text="$____", bg="white", fg="black", font=("Times New Roman", 25))

    option_var = StringVar(hotel_contents_screen)
    option_var.set("Select Room")
    room_option_menu = OptionMenu(hotel_contents_screen, option_var, "Basic", "Premium", "Deluxe",
                                  command=show_output)
    room_option_menu.config(bg="white", fg="black", font=("Times New Roman", 25), width=10)

    # Filler Labels to organize the window
    top_filler_spot = Label(hotel_contents_screen, bg="white", font=("Times New Roman", 25))
    filler_spot = Label(hotel_contents_screen, bg="white", font=("Times New Roman", 25))
    # Enter button
    back_to_meu_button = Button(hotel_contents_screen, text="Back to front desk",
                                bg="white", fg="black", font=("Times New Roman", 25), command=close_hotel_contents)
    room_price_label.grid(row=1, column=1)
    room_option_menu.grid(row=1, column=2)
    room_cost_label.grid(row=1, column=3)
    top_filler_spot.grid(row=2, column=1, columnspan=3)
    per_person_label.grid(row=3, column=1)
    per_person_cost_label.grid(row=3, column=2)
    tax_rate_label.grid(row=3, column=3)
    filler_spot.grid(row=4, column=1, columnspan=3)
    hotel_note_label.grid(row=5, columnspan=3, column=1)
    back_to_meu_button.grid(row=6, column=1, columnspan=3)


# =================================End of Hotel Contents================================

buttonOn = True


def button_click():
    global buttonOn
    buttonOn = buttonOn

    if buttonOn:
        x = entryBox1.get()
        y = entryBox2.get()
        if x == "admin" and y == "admin":
            labelUser1.config(bg="green")
            labelUser2.config(bg="green")
            LogInScreen.after(1)
            messagebox._show("Yay!", "USERNAME/PASSWORD MATCHED")
            front_screen()

        elif x != "admin" and y != "admin":
            labelUser1.config(bg="red")
            labelUser2.config(bg="red")
            LogInScreen.after(1)
            messagebox._show("Error!", "USERNAME/PASSWORD INCORRECT !!\n\n"
                                       "Hint:   Username: admin"
                                       "   Password: admin")
        elif x != "admin" and y != "":
            labelUser1.config(bg="red")
            labelUser2.config(bg="red")
            LogInScreen.after(1)
            messagebox._show("Oh no!", "USERNAME/PASSWORD INCORRECT !!\n\n"
                                       "Hint:   Username: admin"
                                       "   Password: admin")
        elif x != "" and y != "admin":
            labelUser1.config(bg="red")
            labelUser2.config(bg="red")
            LogInScreen.after(1)
            messagebox._show("Oh no!", "USERNAME/PASSWORD INCORRECT !!\n\n"
                                       "Hint:   Username: admin"
                                       "   Password: admin")
        elif x != "" and y != "":
            labelUser1.config(bg="red")
            labelUser2.config(bg="red")
            LogInScreen.after(1)
            messagebox._show("Oh no!", "USERNAME/PASSWORD INCORRECT !!\n\n"
                                       "Hint:   Username: admin"
                                       "   Password: admin")
        else:
            messagebox._show("Enter the Username and Password")


# This part of the code contains the basic things like labels for the
# home screen for the username and password

label1 = Label(LogInScreen, text="Welcome To The Front Desk", font=("Ariel", 30), fg="white",
               bg="Blue", height="2", width="25")

labelUser1 = Label(LogInScreen, text="Username", width=8, height=1, font=("Ariel", 25))

entryBox1 = Entry(LogInScreen, fg="black", bg="white", border="5",
                  font=("Ariel", 24))
labelUser2 = Label(LogInScreen, text="Password", width=8, height=1, font=("Ariel", 25))

entryBox2 = Entry(LogInScreen, fg="black", bg="white", border="5",
                  font=("Ariel", 24), show="*")

button1 = Button(LogInScreen, fg="black", bg="white", font="Ariel,10,bold", border="30",
                 width=8, height=3, text="ENTER",
                 command=button_click)

labelUser3 = Label(LogInScreen, text="PROJECT BY : \n\n DEEP BHAKTA \n\n SERGIO VALADEZ POLANCO \n\n BRIAN VALLADARES",
                   bg="grey", fg="Blue", height="8", width="150")

label1.grid(row=1, column=1)
labelUser1.grid(row=2, column=1)
entryBox1.grid(row=3, column=1)
labelUser2.grid(row=4, column=1)
entryBox2.grid(row=5, column=1)
button1.grid(row=6, column=1)
labelUser3.grid(row=7, column=1)

LogInScreen.mainloop()
# ===========================End of Log In Screen=====================================
# ===========================End of Program===========================================
