from tkinter import *
window = Tk()

import random

WIDTH = 380
HEIGHT = 80

num_sides = IntVar()

status = BooleanVar()

window.title("Dice Roller")
window.geometry(f"{WIDTH}x{HEIGHT}")

sides = Label(window, text = "Number of sides: ")
sides.pack()
sides.place(x = WIDTH / 40)

#creates the radio buttons for selecting the number of sides
four = Radiobutton(window, text = "4", variable = num_sides, value = 4)
four.pack()
four.place(x = WIDTH / 40 * 14)

six = Radiobutton(window, text = "6", variable = num_sides, value = 6)
six.pack()
six.place(x = WIDTH / 40 * 19)
six.select()#sets the default number of sides to 6

eight = Radiobutton(window, text = "8", variable = num_sides, value = 8)
eight.pack()
eight.place(x = WIDTH / 40 * 24)

twelve = Radiobutton(window, text = "12", variable = num_sides, value = 12)
twelve.pack()
twelve.place(x = WIDTH / 40 * 29)

twenty = Radiobutton(window, text = "20", variable = num_sides, value = 20)
twenty.pack()
twenty.place(x = WIDTH / 40 * 34)

dice = Label(window, text = "Number of dice: ")
dice.pack()
dice.place(x = WIDTH / 40, y = HEIGHT / 4)

#creates an entry window to take the number of dice being rolled
num_dice = Entry(window, width = 5)
num_dice.pack()
num_dice.place(x = WIDTH / 40 * 13, y = HEIGHT / 4)
num_dice.insert(0, "2")#sets the default number of dice being rolled to 2

show = Label(window, text = "Show sum ")
show.pack()
show.place(x = WIDTH / 5 * 3, y = HEIGHT / 4)


#creates a check button to let the user choose between showing the sum of the results or not
check = Checkbutton(window, variable = status)
check.pack()
check.place(x = WIDTH / 5 * 4, y = HEIGHT / 4)

#creates a blank placeholder that will be updated with either the results or sums
caption = Label(window, text = "")
caption.pack()
caption.place(x = WIDTH / 40 * 19, y = HEIGHT / 5 * 3)

def roll():
  """Rolls the given number of dice with the set number of sides and either displays the results or the sum."""
  
  #initializes an empty list
  results=[]

  #rolls the appropriate number of dice with the number of sides selected and adds the results to a list
  for num in range(int(num_dice.get())):
    results.append(random.randint(1, num_sides.get()))
  
  #displays the sum of the numbers the different dice landed on if the option is selectedd
  if status.get():
    if num_dice.get() == "1":
      caption["text"] = f"You rolled {results[0]} = {sum(results)}"
    elif num_dice.get() == "2":
      caption["text"] = f"You rolled {results[0]} + {results[1]} = {sum(results)}"
    elif num_dice.get() == "3":
      caption["text"] = f"You rolled {results[0]} + {results[1]} + {results[2]} = {sum(results)}"
  
  #otherwise displays the numbers the different dice landed on
  else:
    if num_dice.get() == "1":
      caption["text"] = f"You rolled {results[0]}"
    elif num_dice.get() == "2":
      caption["text"] = f"You rolled {results[0]}, {results[1]}"
    elif num_dice.get() == "3":
      caption["text"] = f"You rolled {results[0]}, {results[1]}, {results[2]}"

#creates the button that will roll the dice
button = Button(window, text = "Roll dice", command = roll)
button.pack()
button.place(x = WIDTH / 40 * 2, y = HEIGHT / 9 * 5)

mainloop()
