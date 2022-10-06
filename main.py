
from gps import Gps
from data import Data




def main(time,num):
    num = int(num)
    if df['구분'].iloc[num] == '없음':
        print(df[['역명','거리', time]].iloc[num].to_frame(f'{num + 1}번째 가까운 역'))
    else:
        print(df[['역명','구분','거리',time]].iloc[num].to_frame(f'{num+1}번째 가까운 역'))
    print()
    print()






if __name__ == '__main__':
    address = input("주소를 입력하세요\n")
    time = input("시간을 입력하세요 (30분 간격으로 00시00분 형식으로 입력)\n")
    address = address.strip()
    x = Gps(address)
    df = Data(address, x)
    num = 0
    while True:
        main(time,num)
        page = input("N: 다음 역, S: 이전 역, R: 초기화, 0: 끝내기\n")
        if page.upper() == 'N':
            num+=1
        elif page.upper() == "S":
            if  num >= 1:
                num -= 1
            else:
                print("처음 역입니다.")
        elif page.upper() == "R":
            num = 0
        elif page == '0':
            break
        else:
            print("다시 답변해주세요")

