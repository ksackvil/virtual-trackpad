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
