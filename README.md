## notion2gitblog

notion(ver 2.1.4)에서 작성하여 export한 페이지를 github blog에 포스팅하기 적합하게 변환 및 저장합니다.

터미널에서 python(ver 3.8.5) 명령어를 사용하여 실행합니다.

`python notion2gitBlog.py --title=<제목> --subtitle=<부제> --categories=<카테고리> --tags=<태그>` 

- 내보내기 한 zip 파일 압축해제 → zip 파일 삭제
- 이미지 폴더를 “오늘 날짜-<title>”로 변경 및 블로그 폴더로 이동
- md 파일 텍스트 수정
    - 헤더 “#” 하나 추가
    - 첨부 이미지 바뀐 경로로 변경
- md 파일 삭제 후 블로그 폴더에 “오늘 날짜-<title>.md”로 생성

---

현재 내 환경에 맞춰져 있음

추후 범용성 고려, 기능 추가 예정