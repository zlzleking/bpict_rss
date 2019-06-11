# bpict_rss
bpict 트위터를 rss 형식으로 변환해 주는 서비스

## 의존성
1. bs4
2. requests
3. flask

## 설명
이건 아주 간단한 앱입니다. 트위터 bpict 계정의 데이터를 받아다가 적절하게 처리한 다음 rss 형식으로 변환해서 보내 줍니다.
기본적으로는 2분에 1회, 요청이 들어올 시 데이터를 업데이트 합니다.

출력되는 데이터는 RSS 2.0 규격의 XML 문서입니다.

## 예시
[https://bpict.zlzleking.tk](https://bpict.zlzleking.tk)에 들어오시면 데이터 예시를 보실 수 있습니다.