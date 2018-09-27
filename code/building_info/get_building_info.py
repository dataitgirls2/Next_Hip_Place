from urllib2 import Request, urlopen
from urllib import urlencode, quote_plus

url = "http://openapi.nsdi.go.kr/nsdi/BuildingUseService/wfs/getBuildingUseWFS"
queryParams = '?' + urlencode({ quote_plus('authkey') : '인증키'
                               , quote_plus('typename') : 'F253' #* 질의 대상인 하나 이상의 피처 유형 이름의 리스트, 값은 쉼표로 구분화면 하단의 [레이어 목록] 참고 */
                               , quote_plus('bbox') : '217694,448235,218608,449094,EPSG:5174' #/* 좌표로 이루어진 사각형 안에 담겨 있는 (또는 부분적으로 걸쳐 있는) 피처를 검색. 좌표 순서는 사용되는 좌표 시스템을 따름.일반적 표현은 하단좌표, 상단좌표, 좌표체계 순서입니다.(lc1,lc2,uc1,uc2,좌표체계) */
                               , quote_plus('pnu') : '414501080010325' #/* 필지고유번호 19자리중 최소 8자리(시도[2]+시군구[3]+읍면동[3])(입력시 bbox값은 무시) */
                               , quote_plus('maxFeatures') : '10' #/* 요청에 대한 응답으로 WFS가 반환해야하는 피처의 최대 값(최대 허용값 : 100) */
                               , quote_plus('resultType') : 'results' #/* 요청에 대하여 WFS가 어떻게 응답할 것인지 정의.results 값은 요청된 모든 피처를 포함하는 완전한 응답이 생성되어야 함을 나타내며, hits 값은 피처의 개수만이 반환되어야 함을 의미 */
                               , quote_plus('srsName') : 'EPSG:5174' #/* 반환되어야 할 피처의 기하에 사용되어야 할 WFS가 지원하는 좌표체계 */
                               , quote_plus('srsName') : 'EPSG:5179' #/* 반환되어야 할 피처의 기하에 사용되어야 할 WFS가 지원하는 좌표체계 */
                               , quote_plus('srsName') : 'EPSG:5186' #/* 반환되어야 할 피처의 기하에 사용되어야 할 WFS가 지원하는 좌표체계 */
                                })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print response_body

var_dump($response);
