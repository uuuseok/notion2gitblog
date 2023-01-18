## notion2gitblog

노션에서 작성한 글을 편하게 깃허브 블로그로 옮기기 위해 작성했습니다.

### notion2gitblog

notion(ver 2.1.4)에서 작성하여 export한 페이지를 github blog에 포스팅하기 적합하게 변환 및 지정된 경로에 저장합니다. 

---

### MUST READ

- 터미널에서 python(ver 3.8.5) 명령어를 사용하여 실행합니다.

- 명령어는 notion2gitblog 디렉토리에서 실행되어야 하며, notion2gitblog 디렉토리가 존재하는 경로에 exportNotionPage, {username}.github.io 까지 총 3개의 디렉토리만 존재해야 합니다.
    - notion2gitblog 디렉토리는 본 notion2gitBlog.py가 있는 디렉토리이고,
    - exportNotionPage는 notion에서 내보내기 한 zip 파일을 저장할 임시저장소 입니다.<br>
    (포스팅 할 zip 파일 하나만 있어야 합니다. 명령어 입력 후에는 항상 비워져 있어야 합니다.)
    ![image](https://user-images.githubusercontent.com/118060948/213067454-4b29af64-08de-44fd-94ad-d4f595f10a60.png)

- {username}.github.io/_assets/images 경로에 postImages 디렉토리를 생성해야 합니다.
위 경로에 이미지 디렉토리가 이동됩니다.

- 본 코드는 jykyll의 yat 테마를 기준으로 작성 됐습니다
    
    [https://github.com/jeffreytse/jekyll-theme-yat](https://github.com/jeffreytse/jekyll-theme-yat)
    
    - notion2gitblog/notion2gitBlog.py
    - {username}.github.io/_posts
    - {username}.github.io/assets/images
    
    위 경로에 맞게 디렉토리가 있어야 합니다.
    
    - (참고) yat 테마를 적용한 github pages 입니다.
        
        [https://github.com/uuuseok/uuuseok.github.io](https://github.com/uuuseok/uuuseok.github.io)
        

---

### 작동

- notion에서 내보내기 하여 exportNotionPage에 저장한 zip 파일 압축해제 및 zip 파일 삭제
- 이미지가 들어있는 폴더를 “%Y-%m-%d-%H%M%S-{title}”로 이름을 변경하여 {username}.github.io/assets/images/postImages에 이동
- md 파일 수정
    - 헤더 “#” 하나 추가
    - md 파일에 작성되어 있는 이미지 첨부 텍스트를 바뀐 경로로 변경
    - 작성한 yfm을 상단에 추가
- md 파일 삭제 후, {username}.github.io/_post에 수정된 md 파일을 “%Y-%m-%d-%H%M%S-{title}.md” 형식으로 생성

---

### 사용방법

- notion2gitblog의 부모 디렉토리에 “exportNotionPage”, “notion2gitblog”, “{username}.github.io” 세 디렉토리만 존재하는지 확인
- exportNotionPage 안이 비워져 있는지 확인
- {username}.github.io/_assets/images 경로에 postImages 디렉토리가 존재하는지 확인
- **exportNotionPage 디렉토리에 notion에서 “Markdown & CSV”로  내보내기 한 zip파일을 저장**
- **notion2gitblog 경로에서 python 명령어 입력**<br>
`python notion2gitBlog.py --title=<제목> --subtitle=<부제> --categories=<카테고리> --tags=<태그>`
    - 옵션 작성시 공백 등이 있을 때 정상적으로 적용되지 않는 경우가 있습니다. 쌍따옴표로 감싸서 작성하여야 합니다.
        - `python notion2gitBlog.py -t="titleTest" -s="subtitleTest" -c="catTest", -tag="tag1, tag2"`
    - jekyll의 yat 테마를 기준으로 yfm을 작성했습니다. 다른 옵션이 필요하다면 코드의 argparse와 yfm 부분을 수정하여 사용해야 합니다.
- {username}.github.io/_posts 경로에 md 파일이 생성되었는지 확인
- {username}.github.io/assets/images/postImages 경로에 이미지가 들어있는 디렉토리가 생겼는지 확인

---

**개인적인 사용을 위해 만들었기 때문에 오류가 많을 수 있습니다.**

추후 오류 수정과 범용성을 고려, 노션에서 블로그로 옮기면서 발생하는 문제들을 해결하기 위한 기능을 추가할 예정입니다.