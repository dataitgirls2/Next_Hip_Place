# 특정단어가 언급된 트위터 개수 크롤링하기

* 코드는 [twitter_crawling_permonth.ipnyb](https://github.com/dataitgirls2/Next_Hip_Place/blob/master/code/twit_crawling/twitter_crawling_permonth.ipynb) 을 참고하세요 
* 참고 : [왕형준님 블로그](https://medium.com/@whj2013123218/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%9C-twitter-%ED%81%AC%EB%A1%A4%EB%A7%81-576f7b098daf) 갓형준님 감사합니다
* 중복되는 코드를 없앴고 연도별 데이터를 보는 우리 프로젝트에 맞게 코드를 조금 수정했습니다.

#### 먼저 코드를 실행시키기 위해서는

1) Firefox 브라우저가 깔려있어야 합니다.

2) geckodriver.exe가 현재 디렉토리에 있는지 확인해주세요.

## total_twitter_permonth 함수 설명
#### 트위터에서 제공하는 기존 twitter API의 문제점
 무료 API는 최근 7일치 트위터밖에 가져오지 못한다. <br>
 우리가 보려는 것은 2009년부터 현재까지 데이터이므로 twitter에서 제공하는 무료 API는 사용할 수 없었다.<br>
 과거 데이터를 가져오려면 상당한 액수를 지불해야 한다. (우리 프로젝트라면 $399 짜리를 써야 했다...)
<br>
####  그래서 만든것이 total_twitter_permonth함수
날짜, 지역(동), 트윗 수, 하트 수, 연도를 담아 데이터프레임으로 반환<br>
트위터에서 특정 기간동안 특정 단어를 포함한 트윗들을 검색<br>
스크롤을 내려 많은 트윗을 계속 로딩해 와야 하기 때문에 selenium으로 동적 크롤링을 했다.<br>
chrome은 느리다는 말이 있어서 firefox를 이용했고 geckodriver로 크롤링 시행했다<br>



**total_twitter_permonth 함수를 실행시키면 반환되는 데이터프레임**

연남동부터 망원동까지 358개 동을 크롤링 했을 때

|       | Date       | Frequency | Heart | Year | Dong   |
| ----- | ---------- | --------- | ----- | ---- | ------ |
| 0     | 2009-01-01 | 10        | 152   | 2009 | 연남동 |
| 1     | 2009-02-01 | 21        | 223   | 2010 | 연남동 |
| ...   | ...        | ...       | ...   | ...  | ...    |
| 38988 | 2017-11-01 | 63        | 51    | 2017 | 망원동 |
| 38989 | 2017-12-01 | 87        | 252   | 2017 | 망원동 |



#### 개발하면서 생긴 문제점들 
1. 트위터 크롤링 시 로딩 오류

   ```
   %%html
   <div class="js-stream-whale-end stream-whale-end stream-placeholder centered-placeholder">
     <div class="stream-end-inner">
       <h2 class="title">로딩하는데 시간이 지연되고 있습니다.</h2>
       <p>
         트위터의 트래픽이 폭주했거나 일시적인 문제가 발생했을 수 있습니다. <a role="button" href="#" class="try-again-after-whale">다시 시도</a>하거나 <a target="_blank" href="http://status.twitter.com" rel="noopener">트위터 상태 페이지</a>를 방문하여 자세한 내용을 확인해 보세요.
       </p>
     </div>
   </div>
   ```

      해결방안: 위 문구가 나타나면 **트윗수(Frequency)**를 **-1**로 저장하도록 함

2. 다음 날짜로 넘어갈 때 오류가 나서 datetime.timedelta대신 relativedelta 라이브러리 사용
