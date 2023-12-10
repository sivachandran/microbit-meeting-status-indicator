input.onButtonPressed(Button.A, function () {
    manual_on = 1
})
input.onButtonPressed(Button.B, function () {
    manual_on = 0
})
let instruction = ""
let manual_on = 0
serial.writeLine("started")
manual_on = 0
basic.clearScreen()
basic.forever(function () {
    instruction = serial.readString()
    if (manual_on == 1 || instruction == "1") {
        serial.writeLine("received")
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
    } else if (manual_on == 0 || instruction == "0") {
        basic.clearScreen()
    }
})
