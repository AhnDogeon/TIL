import requests
import csv

key = '34875d9adaa52a3ed167ba3472d72b01'

date = [20190113, 20190106, 20181230, 20181223, 20181216, 20181209, 20181202, 20181125, 20181118, 20181111]

weeks_movie = []
for weekend in date:
    URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={weekend}&weekGb=0'


    data = requests.get(URL).json()
    movie_date = data['boxOfficeResult']['showRange']
    for i in range(10):
        movie_information=data['boxOfficeResult']['weeklyBoxOfficeList'][i]['movieCd']
        print(movie_information)


#     for i in range(10):
#         movie_list = []
#         results = {
#             'movie_code' : movie_information[i]['movieCd'],
#             'movie_name' : movie_information[i]['movieNm'],
#             'people' : movie_information[i]['audiAcc'],
#             'movie_cut_date' : movie_date[9:]
#         }

#         movie_list.append(results['movie_code'])
#         movie_list.append(results['movie_name'])
#         movie_list.append(results['people'])
#         movie_list.append(results['movie_cut_date'])
        
#         for n in range(len(weeks_movie)):
#             if movie_list[0] == weeks_movie[n][0]:
#                 break
#         else:
#             weeks_movie.append(movie_list)



# for i in range(43):
#     f_w = open('boxoffice.csv', 'a', encoding='utf-8', newline='')
#     writer = csv.writer(f_w)
#     writer.writerow(weeks_movie[i])
#     f_w.close()