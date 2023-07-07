import datetime
import time
import curses

def mostrar_relogio(stdscr):
    agora = datetime.datetime.now()
    hora_formatada = agora.strftime("%H:%M:%S")
    stdscr.clear()
    stdscr.addstr(curses.LINES // 2, curses.COLS // 2 - len(hora_formatada) // 2, hora_formatada)
    stdscr.refresh()
    time.sleep(1)
curses.wrapper(mostrar_relogio)