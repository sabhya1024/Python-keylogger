import mss

def capture_screenshot():
    with mss.mss() as sct:
        screenshot = sct.shot(output="screenshot.png")
    return screenshot
