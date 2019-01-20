import requests
import csv

key = '34875d9adaa52a3ed167ba3472d72b01'

code = ['20184105','20176251', '20189463', '20180290', '20183915', '20185485', '20184574', '20186281', '20170658', '20175547', '20183785', '20184187', '20182421', '20168773', '20183479', '20183238', '20177552', '20179230', '20183375', '20189843', '20182082', '20178825', '20183745', '20177538', '20184481', '20181905', '20176814', '20183073', '20181171', '20183007', '20182966', '20183050', '20182935', '20182669', '20186822', '20170513', '20189869', '20174981', '20010291', '20179006', '20181404', '20180523', '20182693']

f = open('movie.csv', 'a', encoding='utf-8', newline = '')
writer = csv.writer(f)


for codenumber in code:
    final_movie = []
    URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd={codenumber}'
    
    data = requests.get(URL).json()
    moviedata = data['movieInfoResult']['movieInfo']

    actor = []
    movieinformation = [
        codenumber,
        moviedata['movieNm'],
        moviedata['movieNmEn'],
        moviedata['movieNmOg'],
        moviedata['openDt'],
        moviedata['showTm'],
        moviedata['genres'][0]['genreNm'],
        moviedata['directors'][0]['peopleNm'],
        moviedata['audits'][0]['watchGradeNm']
    ]
    if len(moviedata['actors']) != 0:
        for actornumber in range(len(moviedata['actors'])):
            actor += [moviedata['actors'][actornumber]['peopleNm']]
            if actornumber == 2:
                break
    else:
        actor += []
    final_movie += movieinformation + actor
    writer.writerow(final_movie)
f.close()