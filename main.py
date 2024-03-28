from turtle import Turtle, Screen
import pandas

scr = Screen()
Writer = Turtle()
Writer.hideturtle()
Writer.penup()
Writer.color("black")
Scr_turtle = Turtle()
Scr_turtle.penup()

Found_states = []
file_content = pandas.read_csv("Cities.csv")
scr.title("Pakistan Cities Map Quiz")
image = "Princely_states_of_Pakistan_map.gif"
scr.addshape(image)
Scr_turtle.shape(image)
file_States = file_content.City.to_list()
X_Locations = file_content.X_coordinate.to_list()
y_Locations = file_content.Y_coordinate.to_list()

Score = 0

scr.setup(width=700, height=600)


def GiveUp():
    for i in range(len(file_States)):
        if file_States[i] in Found_states:
            pass
        else:
            Writer.goto(X_Locations[i], y_Locations[i])
            Writer.write(f"{file_States[i]}",align="center", font=("Arial", 9, "bold"))


for _ in range(50):
    Scr_turtle.shape(image)
    try:
        User_Answer = scr.textinput(f"Correct Cities {len(Found_states)}/{len(file_States)}",
                                    "Write the City name in Correct Spelling (Write gp if you give up.)")
        if not User_Answer:  # If the user cancels or leaves the textbox empty
            print("User left the textbox empty or canceled. Please try again.")
            continue
        User_Answer = User_Answer.capitalize()
    except AttributeError:
        print("Wrong user input. Please try again.")
        continue

    if User_Answer.lower() == "gp":
        GiveUp()
        break

    Found = False
    for state_char in file_States:
        if User_Answer != state_char:
            pass
        else:
            if User_Answer in Found_states:
                pass
            else:
                Found = True
                break
    if Found:
        Score += 1
        # print(f"Yes {User_Answer} is There")
        Row = [file_content[file_content["City"] == User_Answer]]
        location = Row[:]
        # for lc in location:
        #     print(f"Location{lc}")
        index_No = file_States.index(User_Answer)
        Writer.goto(X_Locations[index_No], y_Locations[index_No])
        Writer.write(f"{User_Answer}", align="center", font=("Arial", 9, "bold"))
        Found_states.append(User_Answer)

scr.mainloop()
