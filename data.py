
import pandas as pd
import numpy as np

def Data(address,x):
    df = pd.read_csv('./data/서울교통공사_지하철혼잡도정보_20211231.csv', index_col=0, encoding='cp949')
    df = df.sort_values(by='역명')
    lineG = pd.read_csv('./data/국가철도공단_경의중앙선_역위치_20211125.csv', index_col=0, encoding='cp949')
    lineB = pd.read_csv('./data/국가철도공단_분당선_역위치_20211119.csv', index_col=0)
    lineS = pd.read_csv('./data/국가철도공단_수인선_역위치_20211119.csv', index_col=0)
    lineSB = pd.read_csv('./data/국가철도공단_신분당선_역위치_20211119.csv', index_col=0)
    lineU = pd.read_csv('./data/국가철도공단_우이신설_역위치_20220624.csv', index_col=0, encoding='cp949')
    lineK = pd.read_csv('./data/국가철도공단_경강선_역위치_20211125.csv', index_col=0)
    lineC = pd.read_csv('./data/국가철도공단_경춘선_역위치_20211125.csv', index_col=0)
    lineA = pd.read_csv('./data/국가철도공단_공항철도_역위치_20211119.csv', index_col=0)
    line1 = pd.read_csv('./data/국가철도공단_수도권1호선_역위치_20211118.csv', index_col=0)
    line2 = pd.read_csv('./data/국가철도공단_수도권2호선_역위치_20220531.csv', index_col=0, encoding='cp949')
    line3 = pd.read_csv('./data/국가철도공단_수도권3호선_역위치_20211118.csv', index_col=0)
    line4 = pd.read_csv('./data/국가철도공단_수도권4호선_역위치_20211118.csv', index_col=0)
    line5 = pd.read_csv('./data/국가철도공단_수도권5호선_역위치_20211111.csv', index_col=0)
    line6 = pd.read_csv('./data/국가철도공단_수도권6호선_역위치_20211111.csv', index_col=0)
    line7 = pd.read_csv('./data/국가철도공단_수도권7호선_역위치_20211111.csv', index_col=0)
    line8 = pd.read_csv('./data/국가철도공단_수도권8호선_역위치_20211119.csv', index_col=0)
    line9 = pd.read_csv('./data/국가철도공단_수도권9호선_역위치_20211119.csv', index_col=0)
    line = pd.concat([line1, line2, line3, line4, line5, line6, line7, line8, line9, lineG,lineB,lineS,lineSB,lineU,lineK,lineC,lineA], axis=0)
    df = pd.merge(df, line, how='right', on='역명')
    df = df.dropna(how='all')
    df['구분'] = df['구분'].fillna('없음')
    df = df.fillna('혼잡도 없음')
    df = df.drop_duplicates(subset=['역명','구분'])
    df = df.sort_values(by='역명')
    df['거리'] = np.round(np.sqrt((np.abs((df['위도'] - x[address][0]))*(30*3600)) ** 2 + (np.abs(df['경도'] - x[address][1])*(24*3600)) ** 2))
    df = df.sort_values(by='거리')
    return df

