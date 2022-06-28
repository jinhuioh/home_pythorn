print_data='''
---------------
오늘에 대한 정보입니다.
---------------
'''
print(print_data)
weather1, hot1, night1 = input('날씨, 온도, 스케줄 입력').split(',')
print('오늘의 날씨는', weather1, '온도는', float(hot1)-1, '도이고,', night1 +'에 머물 예정입니다.') #float(hot1)은 hot1을 cpu에서
                                                                                            #float값으로 바꿔준 것이다.
print('---------------')
print('---------------')

weather = input('오늘의 날씨는? ')
hot = input('오늘의 온도는? ')
night = input('오늘 저녁 스케줄은? ')
print('---------------')

print('오늘의 날씨는', weather, '온도는', hot +'도이고,', night +'에 머물 예정입니다.')

