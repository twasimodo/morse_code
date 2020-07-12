from ..models.light import Light

led = Light(11)

beeps = {
    ".": led.dot,
    "-": led.dash,
    " ": led.space
}