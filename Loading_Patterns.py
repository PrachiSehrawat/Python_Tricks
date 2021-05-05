#///////////////////////// LOADING PATTERN(1) /////////////////////////

# import time
# from yaspin import yaspin
#
# # Context manager:
# with yaspin():
#     time.sleep(3)  # time consuming code
#
# # Function decorator:
# @yaspin(text="Loading...")
# def some_operations():
#     time.sleep(3)  # time consuming code

# some_operations()


#///////////////////////////// LOADING PATTERN(2) /////////////////////////////////

# import time
# from yaspin import yaspin
#
# # Moon:
# with yaspin().moon:
#     time.sleep(5)  # time consuming code


#//////////////////////////// LOADING PATTERN(3) //////////////////////////////

# import time
# from yaspin import yaspin
#
# spinner = yaspin()
# spinner.start()
#
# time.sleep(3)  # time consuming tasks
#
# spinner.stop()


#//////////////////////////// LOADING PATTERN(4) ///////////////////////////////

# import time
# from yaspin import yaspin
# from yaspin.spinners import Spinners
#
# with yaspin(Spinners.earth, text="Earth") as sp:
#     time.sleep(3)                # time consuming code
#
#     # change spinner
#     sp.spinner = Spinners.moon
#     sp.text = "Moon"
#
#     time.sleep(3)



#///////////////////////////// LOADING PATTERN(5) //////////////////////////////////

# import time
# from yaspin import yaspin
#
# with yaspin(text="Loading...Please wait") as sp:
#     # Support all basic termcolor text colors
#     colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white",)
#
#     for color in colors:
#         sp.color, sp.text = color, color
#         time.sleep(2)



#/////////////////////////// LOADING PATTERN(6) ////////////////////////////////////

# import time
# from yaspin import yaspin
# from yaspin.spinners import Spinners
#
# text = "Loading....Please wait for a moment"
# with yaspin().bold.blink.red.bouncingBall.on_cyan as sp:
#     sp.text = text
#     time.sleep(5)
#
# # The same result can be achieved by passing arguments directly
# with yaspin(Spinners.bouncingBall, color="red", on_color="on_cyan", attrs=["bold", "blink"],) as sp:
#     sp.text = text
#     time.sleep(10)


#//////////////////////// LOADING PATTERN(7) /////////////////////////

# import time
# from yaspin import yaspin, Spinner
#
# # Compose new spinners with custom frame sequence and interval value
# sp = Spinner(["😸", "😹", "😺", "😻", "😼", "😽", "😾", "😿", "🙀"], 200)
#
# with yaspin(sp, text="Cat!"):
#     time.sleep(3)  # cat consuming code :)



#///////////////////////// LOADING PATTERN(8) {Noise spinner} /////////////////////////

# import time
# from yaspin import yaspin
# from yaspin.spinners import Spinners
#
# with yaspin(Spinners.noise, text="Loading...") as sp:
#     sp.color = "yellow"
#     time.sleep(5)

# /////////////////////// LOADING PATTERN(9) {Arc Spinner} /////////////////////////

# import time
# from yaspin import yaspin
# from yaspin.spinners import Spinners
#
# with yaspin(Spinners.arc, text="Loading") as sp:
#     sp.reversal = True
#     sp.side = "right"
#     sp.color = "red"
#     time.sleep(5)


# ////////////////////// LOADING PATTERN(10) {Elapsed Time} /////////////////////////


# import time
# from yaspin import yaspin
# from yaspin.spinners import Spinners
#
# with yaspin(Spinners.moon, text="Time Remaining", timer=True) as sp:
#     time.sleep(5.50)
#     sp.ok()



# /////////////////////// LOADING PATTERN(11) {Downloading} /////////////////////////


# import time
# from yaspin import yaspin
#
# with yaspin(color="cyan") as sp:
#     # task 1
#     time.sleep(2)
#     sp.write("> Image 1 download complete")
#
#     # task 2
#     time.sleep(3)
#     sp.write("> Image 2 download complete")
#
#     # finalize
#     sp.ok("✔ Images Downloaded")



# //////////////////////////// LOADING PATTERN(12) {loading} /////////////////////////

# import time
# from random import randint
# from yaspin import yaspin
#
# with yaspin(color="yellow") as spinner:
#     time.sleep(2)  # time consuming code
#
#     success = randint(0, 2)
#     # Fail = randint(3,8)
#     if success:
#         spinner.ok("Loading success ✅")
#     else:
#         spinner.fail("Loading Fail 💥")



# ////////////////////// LOADING PATTERN(13) {loading} /////////////////////////

# import time
# from yaspin import yaspin
#
# with yaspin().white.bold.shark.on_blue as sp:
#     sp.text = "Loading..."
#     time.sleep(5)



# /////////////////////////// LOADING PATTERN(14) {loading} /////////////////////////

# import time
# from yaspin import yaspin
#
# def white_shark():
#     # Set with attributes
#     with yaspin().red.bold.shark.on_blue as sp:
#         sp.text = "White bold shark in a blue sea 🦈"
#         time.sleep(5)
#
# def ping_pong():
#     # Set with attributes
#     with yaspin(text="Loading...").red.bold.underline.pong.on_grey:
#         time.sleep(5)
#
# def ball():
#     # Set with arguments
#     with yaspin(color="red",on_color="on_grey",attrs=["dark", "concealed"],).bouncingBall as sp:
#         sp.text = "Loading...please wait"
#         time.sleep(5)
#
# def main():
#     white_shark()
#     ping_pong()
#     ball()
#
# if __name__ == "__main__":
#     main()



# ///////////////////////////// LOADING PATTERN(15) {colours} /////////////////////////

# import time
# from yaspin import yaspin
#
# def all_colors():
#     with yaspin(text="Colors!").bouncingBar as sp:
#         time.sleep(2)
#
#         colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")
#         for color in colors:
#             sp.color, sp.text = color, color
#             time.sleep(2)
#
# def main():
#     all_colors()
#
# if __name__ == "__main__":
#     main()
#
#
#
# # //////////////////////// LOADING PATTERN(16) {highlights} /////////////////////////
#
#
# import time
# from yaspin import yaspin
#
# def all_highlights():
#     with yaspin(text="Highlights!").pong as sp:
#         time.sleep(2)
#
#         highlights = ("on_red","on_green","on_yellow","on_blue","on_magenta","on_cyan","on_white","on_grey",)
#         for highlight in highlights:
#             text = "On {0} color".format(highlight.split("_")[1])
#             sp.on_color, sp.text = highlight, text
#             time.sleep(2)
#
# def main():
#     all_highlights()
#
# if __name__ == "__main__":
#     main()
#
#
# #///////////////////////// LOADING PATTERN(17) {attributes} /////////////////////////
#
#
# import time
# from yaspin import yaspin
#
# def all_attributes():
#     with yaspin(text="Attributes!").point as sp:
#         time.sleep(2)
#
#     attrs = ("bold", "dark", "underline", "blink", "reverse", "concealed")
#     # New spinner instance should be created every iteration since
#     # multiple simultaneous color attributes are supported. Hence,
#     # updating attribute of the instance will add new attribute to
#     # the existing list of previous attributes.
#     for attr in attrs:
#         with yaspin().point as sp:
#             sp.attrs, sp.text = [attr], attr
#             time.sleep(2)
#
#
# def main():
#     all_attributes()
#
# if __name__ == "__main__":
#     main()


# /////////////////////// LOADING PATTERN(18) {finalizers} /////////////////////////

# import time
# from yaspin import yaspin
#
# def default_finalizers():
#     with yaspin(text="Downloading...") as sp:
#         time.sleep(2)
#         sp.ok()
#
#     with yaspin(text="Downloading...") as sp:
#         time.sleep(2)
#         sp.fail()
#
# def custom_finalizers():
#     with yaspin(text="Processing...") as sp:
#         time.sleep(2)
#         # Make finalizer green
#         sp.green.ok("✔")
#
#     with yaspin(text="Processing...") as sp:
#         time.sleep(2)
#         # Make finalizer red
#         sp.red.fail("✘")
#
# def main():
#     default_finalizers()
#     custom_finalizers()
#
# if __name__ == "__main__":
#     main()


# //////////////////////// LOADING PATTERN(19) {Clock} /////////////////////////

# import time
# from yaspin import yaspin
# from yaspin.spinners import Spinners
#
# def main():
#     with yaspin(Spinners.clock, text="Clockwise") as sp:
#
#         # Clockwise rotation
#         time.sleep(3)
#
#         # Reverse spin direction
#         sp.reversal = True
#         sp.text = "Anticlockwise"
#
#         # Counterclockwise rotation
#         time.sleep(3)
#
# if __name__ == "__main__":
#     main()



# /////////////////////// LOADING PATTERN(20) {left-right spinner} /////////////////////////

# import time
# from yaspin import yaspin
#
# def main():
#     with yaspin(text="Right spinner", side="right", color="cyan") as sp:
#         time.sleep(2)
#
#         # Switch to left spinner
#         sp.side = "left"  # or just ``sp.left``
#         sp.text = "Left spinner"
#
#         time.sleep(2)
#
# if __name__ == "__main__":
#     main()



# ///////////////////// LOADING PATTERN(21) {Spinner Types} /////////////////////////

# import time
# from yaspin import yaspin
# from yaspin.spinners import Spinners
#
# def manual_setup():
#     sp = yaspin(text="Default spinner")
#     sp.start()
#     time.sleep(2)
#
#     sp.spinner = Spinners.arc
#     sp.text = "Right arc yellow spinner"
#     sp.color = "yellow"
#     sp.side = "right"
#     time.sleep(3)
#
#     sp.text = "Resersed arc spinner"
#     sp.reversal = True
#     time.sleep(3)
#     sp.stop()
#
# def context_mngr_setup():
#     with yaspin(Spinners.noise, text="Noise spinner") as sp:
#         time.sleep(2)
#
#         sp.spinner = Spinners.simpleDotsScrolling
#         sp.text = "Scrolling Dots spinner"
#         sp.color = "magenta"
#         time.sleep(2)
#
# def main():
#     manual_setup()
#     context_mngr_setup()
#
# if __name__ == "__main__":
#     main()



# ///////////////////// LOADING PATTERN(22) /////////////////////////

# import time
# for i in range(6,0,-1):
#   print(i, end=" ")
#   time.sleep(0.3)
# print("loading done !!")


# ///////////////////// LOADING PATTERN(23) /////////////////////////

# import time
# while True:
#     print("\rLoading",end="")
#     print(".",end="")
#     time.sleep(0.3)
#     print(".", end="")
#     time.sleep(0.3)
#     print(".", end="")
#     time.sleep(0.3)
#     print(".", end="")
#     time.sleep(0.3)



#<<<<<<<<<<<<<<<<<<<<< Progress-Bar >>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
# import time
# import progressbar
#
# with progressbar.ProgressBar(max_value=30) as bar:
#     for i in range(30):
#         time.sleep(0.3)
#         bar.update(i)







