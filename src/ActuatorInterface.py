import pyautogui

class ActuatorInterface:
  def __init__(self):
    self.prev_pointer_landmark_x = 0
    self.prev_pointer_landmark_y = 0

  def move_cursor(self, x, y):
    ''' moves current cursor position by x_push and y_push pixels'''
    x_push = x - self.prev_pointer_landmark_x
    y_push = y - self.prev_pointer_landmark_y
    pyautogui.move(x_push, y_push)
    self.prev_pointer_landmark_x = x
    self.prev_pointer_landmark_y = y

  def move_cursor_to(self, x, y):
    ''' moves cursor position toward x, y pixel location in t sec'''
    t = 2
    pyautogui.moveTo(x, y, t)

  def drag_cursor_to(self, x, y):
    ''' drags crusor toward x, y, pixel location in t sec'''
    ''' while holding down left mouse button'''
    t = 3
    pyautogui.dragTo(x, y, t)

  def cursor_click1(self, side):
    ''' single click at current cursor location'''
    ''' side is either left or right'''
    pyautogui.click(button=side)

  def cursor_click2(self, side):
    ''' double click at current cursor location'''
    ''' side is either left or right'''
    pyautogui.doubleClick(button=side)
