def get_wind_class(speed):
    if speed > 0 and speed < 5:
      return('weak [1]')
    elif speed >= 5 and speed <= 10:
      return('moderate [2]')
    elif speed >= 11 and speed <=18:
      return('strong [3]')
    else:
      return('hurricane [4]')


print(get_wind_class(speed=2))