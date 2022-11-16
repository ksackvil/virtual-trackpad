import pyautogui
from datetime import datetime

class ActuatorInterface:
    def __init__(self):
        self.scroll_delta = 2.5
        self.image_width = 1280
        self.image_height = 720
        self.screen_width = 1680
        self.scree_height = 1050
        self.center_rect_x0 = int(self.image_width/2 - 100)
        self.center_rect_y0 = int(self.image_height/2 - 150)
        self.center_rect_x1 = int(self.image_width/2 + 100)
        self.center_rect_y1 = int(self.image_height/2)
        self.last_click_ts = 0
        self.click_debounce_ts = 1
        self.last_move_ts = 0
        self.move_debounce_ts = 0.1 

    def normalize(self, values, bounds):
        return [bounds['desired']['lower'] + (x - bounds['actual']['lower']) * (bounds['desired']['upper'] - bounds['desired']['lower']) / (bounds['actual']['upper'] - bounds['actual']['lower']) for x in values]


    def move_cursor_to(self, x, y):
        ''' moves cursor position toward x, y pixel location in t sec'''
        # Getting the current date and time
        dt = datetime.now()
        ts = datetime.timestamp(dt)

        # debounce number of clicks
        if abs(ts - self.last_move_ts) > self.move_debounce_ts:
            [x] = self.normalize(
                [x],
                {'actual': {'lower': self.center_rect_x0, 'upper': self.center_rect_x1}, 
                'desired': {'lower': 0, 'upper': self.screen_width}}
            )
            [y] = self.normalize(
                [y],
                {'actual': {'lower': self.center_rect_y0, 'upper': self.center_rect_y1}, 
                'desired': {'lower': 0, 'upper': self.scree_height}}
            )
            pyautogui.moveTo(x, y)
            self.last_move_ts = ts

    def cursor_click1(self, side):
        ''' single click at current cursor location'''
        '''     side is either left or right'''
        # Getting the current date and time
        dt = datetime.now()
        ts = datetime.timestamp(dt)

        # debounce number of clicks
        if abs(ts - self.last_click_ts) > self.click_debounce_ts:
            pyautogui.click(button=side)
            self.last_click_ts = ts

    def drag_cursor_to(self, x, y, side):
        ''' drags crusor toward x, y, pixel location in t sec  while holding down left mouse button
        scrolling can be done by dragging the side slide bar'''
        # Getting the current date and time
        dt = datetime.now()
        ts = datetime.timestamp(dt)
        
        if abs(ts - self.last_move_ts) > self.move_debounce_ts:
            [x] = self.normalize(
                [x],
                {'actual': {'lower': self.center_rect_x0, 'upper': self.center_rect_x1}, 
                'desired': {'lower': 0, 'upper': self.screen_width}}
            )
            [y] = self.normalize(
                [y],
                {'actual': {'lower': self.center_rect_y0, 'upper': self.center_rect_y1}, 
                'desired': {'lower': 0, 'upper': self.scree_height}}
            )
            pyautogui.dragTo(x, y, button=side)
            self.last_move_ts = ts

    def cursor_click2(self, side):
        ''' double click at current cursor location'''
        '''     side is either left or right'''
        pyautogui.doubleClick(button=side)

    def cursor_scroll(self, direction):
        ''' roll scroll wheel to move page [direc]'''
        '''     direc is either up or down'''
        pyautogui.scroll(direction*self.scroll_delta)

    def command_a(self):
        # Getting the current date and time
        dt = datetime.now()
        ts = datetime.timestamp(dt)
        
        if abs(ts - self.last_click_ts) > self.click_debounce_ts:
            pyautogui.hotkey('command', 'a')
            self.last_click_ts = ts

    def command_v(self):
        # Getting the current date and time
        dt = datetime.now()
        ts = datetime.timestamp(dt)
        
        if abs(ts - self.last_click_ts) > self.click_debounce_ts:
            pyautogui.hotkey('command', 'v')
            self.last_click_ts = ts

    def command_c(self):
        # Getting the current date and time
        dt = datetime.now()
        ts = datetime.timestamp(dt)
        
        if abs(ts - self.last_click_ts) > self.click_debounce_ts:
            pyautogui.hotkey('command', 'c')
            self.last_click_ts = ts