#24-12-2021

barWidth = 1


def setup():
    size(800 , 800)
    colorMode(HSB,400)
    noStroke()
    background(255)


def draw():
    whichBar = mouseX 
    barX = whichBar 
    fill(mouseY, 800, 800)
    rect(barX, 0, barWidth, 800)
    lastBar = whichBar
