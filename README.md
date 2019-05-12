# SMALLSNU_BACKEND
## REST API guide
| path | function | method |
|:---|:---:|---:|
| `admin/` | 관리자 페이지 | GET |
| `map/` | 지도 정보 | GET |
| `building/` | 전체 건물 리스트 | GET |
| `building/<building_code>/` | 건물 세부정보 | GET |
| `building/<building_code>/post/` | 게시물 등록 | POST |
| `post/<int:postId>/` | 게시물 수정 | POST |
| `seminar/` | 전체 세미나 리스트 | GET |
| `restaurant/` | 전체 식당 리스트 | GET |
| `shuttle/` | 전체 셔틀 리스트 | GET |
| `lecture/` | 전체 강의 리스트 | GET |
| `route/?from=v1&to=v2` | 길 찾기 | GET |


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
- python3 manage.py runserver

