# ![25](https://user-images.githubusercontent.com/103415295/200451827-97c67713-e0d2-4558-bf6f-f2b9846c0829.png)내일배움캠프 Team 텔레토비태양

## 유화 제작 프로젝트 저장소


frontend repo = https://github.com/nhkmi1001/teletubbies_print_FE

# ![25](https://user-images.githubusercontent.com/103415295/200451827-97c67713-e0d2-4558-bf6f-f2b9846c0829.png)팀원 역할 및 약속
### 팀원 역할
  - **김남훈** 프론트엔드/백엔드 [블로그 링크](https://hunss.tistory.com/)
  - **김서영** 머신러닝/백엔드 [블로그 링크](https://velog.io/@ksykma)
  - **서장원** 프론트엔드/백엔드 [블로그 링크](https://sjw887.tistory.com/)
  - **최윤선** 머신러닝/백엔드 [블로그 링크](https://iced-coriander-f89.notion.site/TIL-WIL-Tistory-e8463c7836844157a40c2c76fbaf1c61)
  
### 우리팀의 약속
  - 프로젝트 진행사항 매일매일 다 같이 모여서 공유하기
     + 아침 : 뭘 진행할 예정인지(그날의 목표)
     + 저녁 : 어디까지 마무리되었고 코드 리뷰!
  - 컨디션 조절 잘하기!
  - TIL 밀리지 않기!
  - 커밋 약속: 생성 [Add], 수정 [Mod], 내용 자세하게 쓰기, 수시로 커밋하기, 브랜치 확인하기
  

# 프로젝트 주제
+ 유화 제작 프로젝트
  - 준비 된 Filter를 사용자가 선택하고 원하는 이미지를 삽입해 유화필터를 입힌 결과물을 보여줌. 

# 프로젝트 포함 사항
  - DRF의 CBV를 활용하여 구현
  - 프론트엔드와 백엔드를 별도의 레포지토리로 관리하기
  - 유화제작 인공지능 기술(NST)을 사용해서, 사용자가 이미지를 넣으면 유화스타일이 적용된 이미지로 변환되어 출력되는 서비스를 만들기
  - Django의 기본 user model이 아닌, custom user model을 사용
  - Frontend와 Backend 서버를 별도로 구축하고 구현
 

 # ![25](https://user-images.githubusercontent.com/103415295/200451837-221980f5-74f3-46f2-a56b-704e7c5ad91b.png)와이어프레임
![image](https://ifh.cc/g/RANmCz.jpg)

 # ![25](https://user-images.githubusercontent.com/103415295/200451854-3a9e805d-e24e-4035-a7b0-c6238b5c487b.png)API설계
![image](https://ifh.cc/g/SMxoGS.jpg)





 # ![25](https://user-images.githubusercontent.com/103415295/200451920-fa94cae7-f866-4c65-bbe0-3976fd8b350b.png)DB설계
![image](https://ifh.cc/g/ZqzvfR.png)


 # ![25](https://user-images.githubusercontent.com/103415295/200451928-7782261a-3148-4069-a03c-eb79678a59cb.png)프로젝트 기능 명세서
 ### 회원가입 & 로그인
   + 닉네임과 비밀번호 길이 최소치 지정
   + 빈 값으로 회원가입 시도시 경고창 생성
   
 ### 메인페이지
   + 유화제작 필터 이미지 보여주기

 ### 머신러닝페이지
   + 사용자가 이미지 업로드
   + 버튼 클릭 시 사용자가 업로드한 이미지를 머신러닝 함수를 통해 유화필터를 적용시키기

 ### Output_image리스트페이지
   + 서비스를 이용한 모든 결과이미지 보여주기
 
 ### Output_imgae상세보기
   + 결과이미지를 보여주기
   + 댓글을 작성하고 이전 댓글리스트 보여주기
  
 ### 앞으로 추가할 기능
   + 소셜 회원가입/로그인 기능
   + 좋아요 기능 -> 2/8 추가함
   + 댓글 기능 -> 2/7 추가 완료
   + 북마크 기능


# ![25](https://user-images.githubusercontent.com/103415295/200451936-b234dac2-a60a-4249-8a04-f03662eb0122.png)기술 스택

### 백엔드
<img alt="Python" src ="https://img.shields.io/badge/Python-3776AB.svg?&style=for-the-badge&logo=Python&logoColor=white"/> <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white">

### 프론트엔드
<img alt="JavaScript" src ="https://img.shields.io/badge/JavaScriipt-F7DF1E.svg?&style=for-the-badge&logo=JavaScript&logoColor=black"/> <img alt="Html" src ="https://img.shields.io/badge/HTML5-E34F26.svg?&style=for-the-badge&logo=HTML5&logoColor=white"/> <img alt="Css" src ="https://img.shields.io/badge/CSS3-1572B6.svg?&style=for-the-badge&logo=CSS3&logoColor=white"/>

### 데이터베이스
<img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=SQLite&logoColor=white">

### 머신러닝
<img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=OpenCV&logoColor=white"> <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=TensorFlow&logoColor=white">


### 협업
<img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
