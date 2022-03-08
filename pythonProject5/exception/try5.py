try:
    test_file3 = open('test.txt','w')
    #test.txt.를 읽겠다(r) , 쓰려면 r 대신 w쓰면 됨
    #기존에 있는 내용에 추가만 하려면 w대신 a(append)넣기!
    test_file3.write('hellow jijdi\n')#\n이 엔터를넣겠다는 의미
    test_file3.write('hellow2 jijdi2')
    result = test_file3.write('hihihi lunch i ')
    print(result)#이 배열값을 for문을 통해 꺼내보자.

    for line in result:
        print(line)
    # one = test_file2.readline()
    # print(one)
    # one2 = test_file2.readline()
    # print(one2)
# except NameError:
#     print('해당이름파일을 찾을 수 없음')
except FileNotFoundError:
    print('해당파일을 찾을 수 없음')
except IOError:
    print('읽고쓰는데 문제가 생김')
except:
    print('파일을 처리하는데 문제가 생김')
finally:
    try:
        test_file3.close()
    except:
        print('파일을 closing하는데 문제가 생김')
#램에 만들어진 connecion을 담당하는 stream객체를
#메모리에서 지우는 역할을 수행
#close함수를 호출하지 않으면 메모리에 계속 남아있어서
#반드시 메모리에서 지워주어야 한다.