# SMALLSNU_BACKEND
## REST API guide
| path | function | method |
|:---|:---:|---:|
| `admin/` | 관리자 페이지 | GET |
| `map/` | 지도 정보 | GET |
| `building/` | 전체 건물 리스트 | GET |
| `building/<building_code>/` | 건물 세부정보 | GET |
| `building/<building_code>/post/` | 게시물 등록 | POST |
| `building/<building_code>/post/` | 건물별 게시물 리스트 | GET |
| `building/<building_code>/restaurant/` | 건물별 식당 리스트 | GET |
| `building/<building_code>/cafe/` | 건물별 카페 리스트 | GET |
| `building/<building_code>/conv/` | 건물별 편의점 리스트 | GET |
| `building/<building_code>/bank/` | 건물별 은행 리스트 | GET |
| `building/<building_code>/atm/` | 건물별 ATM 리스트 | GET |
| `building/<building_code>/seminar/` | 건물별 세미나 리스트 | GET |
| `post/<int:postId>/` | 게시물 수정 | POST |
| `post/<int:postId>/` | 게시물 조회 | GET |
| `post/<int:postId>/` | 게시물 삭제 | DELETE |
| `post/<int:postId>/like/` | 게시물 좋아요 | POST |
| `post/<int:postId>/comment/` | 댓글 등록 | POST |
| `post/<int:postId>/comment/` | 게시물별 댓글 리스트 | GET |
| `post/` | 전체 게시물 리스트 | GET |
| `comment/<int:commentId>/` | 댓글 수정 | POST |
| `comment/<int:commentId>/` | 댓글 조회 | GET |
| `comment/<int:commentId>/` | 댓글 삭제 | DELETE |
| `comment/<int:commentId>/like/` | 댓글 좋아요 | POST |
| `seminar/` | 전체 세미나 리스트 | GET |
| `seminar/<int:pk>/` | 세미나 조회 | GET |
| `restaurant/` | 전체 식당 리스트 | GET |
| `restaurant/<int:pk>/` | 식당 조회 | GET |
| `cafe/` | 전체 카페 리스트 | GET |
| `cafe/<int:pk>/` | 카페 조회 | GET |
| `conv/` | 전체 편의점 리스트 | GET |
| `conv/<int:pk>/` | 편의점 조회 | GET |
| `bank/` | 전체 은행 리스트 | GET |
| `bank/<int:pk>/` | 은행 조회 | GET |
| `atm/` | 전체 ATM 리스트 | GET |
| `atm/<int:pk>/` | ATM 조회 | GET |
| `shuttle/` | 전체 셔틀 리스트 | GET |
| `lecture/` | 전체 강의 리스트 | GET |
| `lecture/<int:pk>` | 강의 조회 | GET |
| `route/?from=v1&to=v2` | 길 찾기 | GET |
| `search/?q=keyword` | 통합검색 | GET |


## Dependency
1. virtualenv .env
1. source .env/bin/activate
1. pip3 install -r requirements.txt
- virtualenv 를 이용(.env)
- 새로 virtualenv에 의존성을 추가할 경우 
    - pip3 freeze > requirements.txt

## Git Branch
- 기능을 추가 할 시 'feature/your_feature_name' 브랜치로 checkout하여 작업 후 develop브랜치로 merge

## Initial DB Setting
- python3 manage.py migrate
- python3 manage.py shell < db_seed.py
- python3 manage.py shell < crawler.py
- python3 manage.py shell < pathFinder.py
- python3 manage.py runserver

## Crontab 등록
- crontab -e
- 0 19 * * * /절대경로/.env/bin/python3 /절대경로/manage.py shell < /절대경로/crawler.py

