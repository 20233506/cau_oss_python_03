import math

class line:

     __width  = 0
     __height = 0
     def __init__(self, width, height):
         # 생성자 초기 width와 height 값을 입력
         # Args:
         #      width  (int or float) : 초기 선의 가로 길이
         #      height (int or float) : 초기 선의 세로 길이
          self.__width  = width
          self.__height = height

     def set_length(self,width,height):
          # 선의 길이를 수정
          # Args:
          #     width  (int or float) : 수정하고자 하는 가로 길이
          #     height (int or float) : 수정하고자 하는 세로 길이
          self.__width  = width
          self.__height = height

     def get_length(self):
          # 객체가 저장하고 있는 선의 길이를 반환
          # Returns:
          #     int or float : 저장하고 있는 선의 길이
          return self.__width, self.__height
     
     def area_rectangle(width,height):
          # 길이를 입력받아 직사각형의 넓이를 구하는 함수
          # Args:
          #     width  (int or float) : 밑변의 길이
          #     height (int or float) : 높이의 길이
          # Returns:
          #     int or float: 직사각형의 넓이를 반환
          if width <= 0 or height <= 0: raise ValueError
          return width * height
     
     def area_ellipse(width,height):
          # 길이를 입력받아 타원의 넓이를 구하는 함수
          # Args:
          #     width  (int or float) : 짧은쪽 반지름 길이
          #     height (int or float) : 긴쪽 반지름 길이
          # Returns:
          #     int or float : 원의 넓이를 반환
          if width <= 0 or height <= 0: raise ValueError
          return width * height * math.pi
     def area_right_triangle(width,height):
          # 길이를 입력받아 직각삼각형의 넓이를 구하는 함수
          # Args:
          #     width  (int or float) : 밑변의 길이
          #     height (int or float) : 높이의 길이
          # Returns:
          #     int or float: 직각삼각형의 넓이를 반환
          if width <= 0 or height <= 0: raise ValueError
          return width * height / 2
     