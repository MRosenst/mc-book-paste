import pyautogui as pag
import sys
import time

MAX_PAGE_CHARS = 255

time.sleep(5)

def long_click(x, y, duration=0.1):
    pag.moveTo(x, y)
    pag.mouseDown()
    time.sleep(duration)
    pag.mouseUp()

def next_page():
    arrow = pag.locateOnScreen('arrow.png')
    left, top, width, height = arrow
    long_click(x=left + width // 2, y=top + height // 2)
    pag.moveTo(10, 10)

pages = ['']
with open(sys.argv[1], 'r') as f:
    page_chars = 0
    page_num = 0
    for line in f:
        for word in line.split():
            word += ' '
            if len(word) + page_chars + 2 > MAX_PAGE_CHARS:
                page_num += 1
                page_chars = 0
                pages.append('')

            pages[page_num] += word 
            page_chars += len(word)
        
        page_chars += 2
        pages[page_num] += '\r\n'            

for page in pages:
    pag.write(page)
    if page != pages[-1]:
        next_page()
