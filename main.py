import customtkinter as ctk
import json
import pygame
import pyautogui
import threading
import keyboard

buttons_List = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
"J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


#save the profile status
def SaveStatus():
    global buttons_data
    data = []
    for i in range(22):
        data.append(buttons_data[i].get())
    
    json_data = json.dumps(data)
    with open("profiles/game.json", "w") as f:
        f.write(json_data)

#load the profile status
def LoadStatus():
    global buttons_data
    
    with open("profiles/game.json", "r") as f:
        json_data = f.read()

    data = json.loads(json_data)
    for i in range(22):
        buttons_data[i].set(data[i])


#controller section setting
def ControlsSECTION():
    global tabV, buttons_data
    x, y = 30, 120

    label = ctk.CTkLabel(master=tabV.tab("Controls"), text="Profile", width=49,height=10)
    label.place(x = 30, y = 40)
    sts1 = ctk.CTkLabel(master=tabV.tab("Controls"), text="Profile Set")
    sts1.place(x = 0, y = 0)
    ButSet1 = ctk.CTkButton(master=tabV.tab("Controls"), text="Load Profile", command=LoadStatus)
    ButSet1.place(x = 250, y = 35)
    ButSet2 = ctk.CTkButton(master=tabV.tab("Controls"), text="Save Profile", command=SaveStatus)
    ButSet2.place(x = 30, y = 35)

    li = [["A", "B", "X", "Y"],
          ["RT", "RB", "LT", "LB",],
          ["x+_Right_Analog", "x-_Right_Analog",
        "y+_Right_Analog", "y-_Right_Analog",
        "x+_Left_Analog", "x-_Left_Analog",
        "y+_Left_Analog", "y-_Left_Analog"],
        ["Up_Pad", "Right_Pad",
        "Down_Pad", "Left_Pad"],
        ["Start", "Select"] ]

    count = 0
    splace = []
    ctrlbut = []
    for i in range(5):
        for _ in li[i]:
            splace.append(ctk.CTkLabel(master=tabV.tab("Controls"), text=_))
            splace[count].place(x = x, y = y)
            ctrlbut.append(ctk.CTkComboBox(master=tabV.tab("Controls"), values=buttons_List, variable=buttons_data[count]))
            ctrlbut[count].place(x = x, y = y + 20)
            y = y + 49
            count = count + 1
        x = x + 160
        y = 120

def check(strv):
    for _ in range(97,122):
        if strv == chr(_):
            return chr(_)

    for _ in range(65,90):
        if strv == chr(_):
            return chr(_)
    
    #in any case so the program don't crash if the asserted value was null
    return 'a'
     
#do while loop
def do_while():
    global buttons_data

    # Get the first joystick
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


            elif event.type == pygame.JOYBUTTONUP:
                if event.button == 12:  # A button
                    keyboard.press(check(buttons_data[0].get()))
                elif event.button == 13:  # B button
                    keyboard.press(check(buttons_data[1].get()))
                elif event.button == 14:  # X button
                    keyboard.press(check(buttons_data[2].get()))
                elif event.button == 15:  # Y button
                    keyboard.press(check(buttons_data[3].get()))


                elif event.button == 11:  # RT button
                    keyboard.press(check(buttons_data[4].get()))
                elif event.button == 9:  # RB button
                    keyboard.press(check(buttons_data[5].get()))
                elif event.button == 10:  # LT button
                    keyboard.press(check(buttons_data[6].get()))
                elif event.button == 8:  # LB button
                    keyboard.press(check(buttons_data[7].get()))


                #Padburrons
                elif event.button == 4:  # Up button
                    keyboard.press(check(buttons_data[16].get()))
                elif event.button == 5:  # Right button
                    keyboard.press(check(buttons_data[17].get()))
                elif event.button == 6:  # Down button
                    keyboard.press(check(buttons_data[18].get()))
                elif event.button == 7:  # Left button
                    keyboard.press(check(buttons_data[19].get()))

                
                elif event.button == 3:  # Start button
                    keyboard.press(check(buttons_data[20].get()))
                elif event.button == 0:  # Select button
                    keyboard.press(check(buttons_data[21].get()))
                


            elif event.type == pygame.JOYBUTTONDOWN:
                print(f"Button {event.button} pressed")
            elif event.type == pygame.JOYBUTTONUP:
                print(f"Button {event.button} released")




ctk.set_appearance_mode("Dark")

    
#main app window
app = ctk.CTk()
app.title("Controll Mapper")
app.geometry("900x650")
app.resizable(False, False)

tabV = ctk.CTkTabview(app, width=850, height=600)
tabV.place(x = 30, y = 20)
tabV.add("Controls")

buttons_data = []

for i in range(22):
    buttons_data.append(ctk.StringVar(value="Null"))

ControlsSECTION()

pygame.init()
pygame.joystick.init()


if pygame.joystick.get_count() == 0:
    print("ERROR, no controller is detected")
else:
    thread = threading.Thread(target=do_while, daemon=True)
    thread.start()

    app.mainloop()