def on_button_pressed_a():
    global manual_on
    manual_on = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global manual_on
    manual_on = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

line = ""
manual_on = 0
serial.write_line("started")
manual_on = 0
basic.clear_screen()

def on_forever():
    global line
    line = serial.read_string()
    if manual_on == 1 or line == "1":
        serial.write_line("received")
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
    elif manual_on == 0 or line == "0":
        basic.clear_screen()
basic.forever(on_forever)
