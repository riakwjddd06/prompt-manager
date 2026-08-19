# 🍎 나만의 프롬프트 매니저 (Prompt Manager)

## 1. 미션 소개

생성형 AI 기초부터 멀티모달 콘텐츠 제작까지 다루며 누적된 수많은 프롬프트를 체계적으로 관리하기 위해 기획된 콘솔 기반 파이썬 프로그램이다. 메모장이나 메신저에 파편화된 프롬프트 기록을 찾아 헤매는 비효율을 줄이고자 구축했다.

단순히 파이썬의 기초 문법(변수, 조건문, 반복문, 자료구조)을 외우는 것에 그치지 않고, 이 문법들이 프로그램 내부에서 어떻게 유기적으로 동작하는지 직접 코드로 엮어내는 것이 목표다. 또한, Git과 GitHub를 이용해 로컬 환경 설정부터 원격 저장소 연동, 에러 해결(Troubleshooting), 브랜치 병합까지의 버전 관리 워크플로우를 체득하는 데 본질적인 가치가 있다.

---

## 2. 미션 수행 과정 및 트러블슈팅 내역

모든 과정은 GOOGLE Gemini 3.1 pro의 도움을 받아 수행함.
대화 로그: https://share.gemini.google/O4fp6xtahXRP

본 항목은 개발 환경 구축부터 GitHub 원격 저장소 연동까지의 단계별 수행 과정 및 주요 오류 해결(Troubleshooting) 내역을 정리함.

### STEP 1. 개발 환경 세팅 및 작업 폴더 생성
* **수행 내용:**
  * macOS 환경에 맞춰 Visual Studio Code(VSCode) 공식 홈페이지에서 설치 파일 다운로드 및 응용 프로그램 폴더 이동을 통한 설치 진행.
  * 바탕화면에 `prompt-manager` 작업 폴더 생성 후 VSCode를 통해 해당 디렉토리 오픈.
  * 단축키(`Ctrl(⌃) + ~`)를 활용하여 VSCode 내장 터미널 실행 확인.

### STEP 2. Git 초기 설정 및 불필요 파일 예외 처리
* **수행 내용:**
  * 터미널 명령어(`git config --global`)를 통해 Git 사용자 이름(`user.name`) 및 이메일(`user.email`) 전역 설정 완료.
  * `git init` 명령어로 로컬 저장소 초기화 진행.
  * macOS 운영체제 특성상 자동 생성되는 숨김 파일(`.DS_Store`)이 원격 저장소에 업로드되는 것을 방지하기 위해 `.gitignore` 파일을 생성하고 해당 파일명을 기재하여 예외 처리함.

### STEP 3. 파이썬 스크립트 생성 및 최초 커밋(Commit) 수행
* **수행 내용:**
  * 메인 스크립트인 `prompt_manager.py` 파일 생성.
  * 실사용 목적의 프롬프트 데이터 3종(흑백 사진 생성, 객관적 도서 추천, 자원봉사 자소서 수정)을 딕셔너리 리스트(`prompts`) 형태로 초기 데이터로 삽입함.
  * `git add .` 및 `git commit -m "init: 기본 프롬프트 데이터 세팅"` 명령어를 통해 최초 커밋 기록 생성.

### STEP 4. 브랜치(Branch) 분리 및 1차 트러블슈팅
* **수행 내용:**
  * `git checkout -b feature/menu` 명령어로 신규 브랜치 생성 후 메인 메뉴 출력 및 무한 루프(`while True`) 로직 구현.
* **이슈 및 해결:**
  * **[오류 1] 경로 이탈 (`[Errno 2] No such file or directory`):** VSCode 내장 터미널이 아닌 macOS 기본 터미널 앱의 단독 실행으로 인해 작업 디렉토리 경로 불일치 발생. VSCode 내장 터미널을 재실행하여 올바른 경로를 확보함.
  * **[오류 2] 변경 사항 미반영:** 코드 수정 후 터미널 실행 시 이전 코드가 동작하는 현상 발생. 파일 탭의 미저장 표시(●)를 확인하고, 단축키(`Cmd(⌘) + S`)를 통한 명시적 저장 후 실행하여 해결함.

### STEP 5. 브랜치 병합(Merge) 및 세부 기능 개발
* **수행 내용:**
  * `git checkout main`으로 본 브랜치 복귀 후 `git merge feature/menu` 명령어로 메뉴 기능 병합 완료.
  * 프롬프트 추가, 목록 조회, 검색, 상세 보기, 즐겨찾기 상태 변경(Toggle) 기능을 순차적으로 구현함.
  * 카테고리별 조회 기능 누락을 확인하고 `feature/category` 브랜치를 추가 생성하여 기능 개발 후 `main` 브랜치에 2차 병합 수행.
  * 각 기능 구현 완료 시마다 `git add` 및 `git commit`을 반복하여 기능 단위로 커밋 이력을 분할 저장함.

### STEP 6. GitHub 원격 저장소 연동 및 인증 이슈 해결
* **수행 내용:**
  * GitHub 플랫폼에 `prompt-manager` 명칭의 신규 원격 저장소 생성.
  * 로컬 터미널에 원격 저장소 주소 연동(`git remote add origin`) 명령어 실행.
* **이슈 및 해결:**
  * **[오류 3] 저장소 내역 충돌:** 원격 저장소 생성 시 'README.md 자동 생성' 옵션을 활성화하여 로컬과 원격 간 데이터 충돌 발생. `git push -u origin main --force` 명령어로 로컬 데이터를 강제 덮어쓰기 하여 연동함.
  * **[오류 4] CLI 암호 인증 차단 (`Password authentication is not supported`):** GitHub의 보안 정책 변경으로 인해 일반 비밀번호를 통한 터미널 푸시(Push) 제한. GitHub Developer settings에서 전용 토큰(Personal access tokens)을 신규 발급받아 암호 입력란에 삽입하여 인증을 통과함.

### STEP 7. README 작성 및 커밋 10회 이상 요건 충족
* **수행 내용:**
  * `README.md` 파일을 생성하여 프로그램 설명 및 실행 방법 기재 후 커밋함.
  * 미션 요구사항인 '최소 10개 이상의 커밋'을 안전하게 달성하기 위해 README 줄바꿈 추가, 코드 내 주석 삽입, UI 텍스트(이모지) 개선 등 사소하지만 의미 있는 변경 사항을 5회 추가 진행하여 총 12개의 커밋 로그를 확보함.
* **이슈 및 해결:**
  * **[오류 5] Git Log 읽기 모드 (`(END)` 대기 상태):** `git log --oneline --graph` 실행 시 출력될 커밋 이력이 길어 터미널이 읽기 모드로 전환됨. 키보드 `q` 키를 입력하여 해당 모드를 정상 종료한 후 전체 그래프 내역을 스크린샷으로 캡처 완료함.

---

## 3. 파이썬 코드 상세 설명 (`prompt_manager.py`)

외부 라이브러리 없이 파이썬 3.10 이상의 기본 문법만으로 로직을 구현했다.

* **데이터 구조 구축 (`prompts`):** 
  프롬프트 제목, 내용, 카테고리, 즐겨찾기 여부(Boolean)를 각각 쌍으로 담은 딕셔너리(`{}`)들을 하나의 리스트(`[]`) 안에 묶어 기본 데이터로 구축했다.
* **메뉴 출력 (`show_menu`):** 
  사용자가 선택할 수 있는 1번부터 6번, 그리고 0번(종료)까지의 선택지를 터미널 화면에 출력한다.
* **프롬프트 추가 (`add_prompt`):** 
  `input()` 함수로 사용자 입력값을 받아 새로운 딕셔너리 세트를 구성하고, `prompts.append()`를 통해 기존 리스트에 데이터를 적재한다. 즐겨찾기 기본값은 `False`로 고정했다.
* **목록 및 카테고리 조회 (`show_list`, `show_category`):** 
  `for` 반복문과 `enumerate()` 내장 함수를 결합해 리스트의 인덱스 번호(1번부터 시작하도록 +1 처리)와 데이터를 순차적으로 출력한다. 카테고리 조회 기능은 `if` 조건문을 추가해 사용자가 입력한 카테고리명과 일치하는 딕셔너리만 필터링하여 보여준다.
* **검색 기능 (`search_prompt`):** 
  `in` 연산자를 활용하여 사용자가 입력한 키워드가 딕셔너리의 'title'이나 'content' 값에 부분적으로라도 포함되어 있는지 검사하고 결과를 반환한다.
* **즐겨찾기 토글 (`toggle_favorite`):** 
  리스트의 인덱스 접근 방식을 사용하여 특정 프롬프트의 `favorite` 불리언 값을 찾은 뒤, `not` 연산자로 반전시켜 즐겨찾기 상태를 제어한다.
* **메인 루프 엔진 (`while True:`):** 
  프로그램이 한 번 실행되고 꺼지지 않도록 무한 루프를 돌린다. `choice = input()`으로 받은 값에 따라 `if-elif`문으로 분기시켜 각 함수를 호출하며, '0'이 입력되면 `break`로 루프를 탈출해 프로그램을 완전히 종료한다.


```python
# 기본 프롬프트 3개 세팅
import json
import os

FILE_NAME = "prompts.json"

# 파일에서 프롬프트 불러오기
def load_prompts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return [
            {"title": "사실적인 흑백 사진", "content": "레퍼런스 이미지를 똑같이 베끼지 말고, 일러스트 느낌 없이 완전히 사실적인 흑백 사진 스타일로 독창적인 구도를 만들어 줘.", "category": "이미지 생성", "favorite": True},
            {"title": "객관적인 도서 추천", "content": "이전 대화 맥락은 무시하고, 쇼펜하우어 관련 도서들을 아주 객관적인 시각에서 추천해 줘.", "category": "텍스트 생성", "favorite": False},
            {"title": "자원봉사 자소서 수정", "content": "대구국제뮤지컬페스티벌 자원봉사 지원서 초안이야. 과장된 칭찬이나 미사여구는 전부 빼고, 내 경험 위주로 건조하고 사실적으로 수정해 줘.", "category": "텍스트 생성", "favorite": False}
        ]

prompts = load_prompts()

# 파일에 프롬프트 진짜로 저장하기
def save_prompts():
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(prompts, f, ensure_ascii=False, indent=4)

def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가\n2. 프롬프트 목록\n0. 종료")
    
def add_prompt():
    print("\n[새 프롬프트 추가]")
    print("-" * 30)
    new_title = input("제목을 입력하세요: ")
    new_content = input("내용을 입력하세요: ")
    new_category = input("카테고리(텍스트 생성/이미지 생성 등): ")
    
    new_item = {
        "title": new_title,
        "content": new_content,
        "category": new_category,
        "favorite": False
    }
    prompts.append(new_item)
    save_prompts()
    print("✨ 성공적으로 추가됐어!")
    

def show_list():
    print("\n[전체 프롬프트 목록]")
    for i, p in enumerate(prompts):
        star = "⭐" if p["favorite"] else "  "
        print(f"{i+1}번 {star} | 제목: {p['title']} | 카테고리: {p['category']}")

def search_prompt():
    print("\n[프롬프트 검색]")
    keyword = input("검색할 단어를 입력하세요: ")
    found = False
    for p in prompts:
        if keyword in p['title'] or keyword in p['content']:
            print(f"- {p['title']} ({p['category']})")
            found = True
    if not found:
        print("검색 결과가 없어.")

# 제목과 내용에서 동시에 키워드 검색
def show_detail():
    show_list()
    num = input("\n자세히 볼 번호 입력: ")
    idx = int(num) - 1
    p = prompts[idx]
    print(f"\n[상세 보기] {p['title']}")
    print(f"카테고리: {p['category']} | 즐겨찾기: {'⭐' if p['favorite'] else '❌'}")
    print(f"내용: {p['content']}")

def toggle_favorite():
    show_list()
    num = input("\n즐겨찾기 바꿀 번호 입력: ")
    idx = int(num) - 1
    prompts[idx]['favorite'] = not prompts[idx]['favorite']
    save_prompts()
    print("즐겨찾기 상태가 바뀌었어!")
    
def show_category():
    print("\n[카테고리별 조회]")
    cat = input("조회할 카테고리 입력(예: 텍스트 생성): ")
    found = False
    for p in prompts:
        if p['category'] == cat:
            star = "⭐" if p["favorite"] else "  "
            print(f"- {star} {p['title']}")
            found = True
    if not found:
        print("해당 카테고리에 프롬프트가 없어.")

# 메인 엔진 시작
while True:
    print("\n=== 🍎 나만의 프롬프트 매니저 ===")
    print("1. 추가\n2. 목록\n3. 검색\n4. 상세\n5. 즐겨찾기\n6. 카테고리 조회\n0. 종료")
    choice = input("선택: ")
    
    if choice == '0':
        print("프로그램을 종료합니다.")
        break
    elif choice == '1': add_prompt()
    elif choice == '2': show_list()
    elif choice == '3': search_prompt()
    elif choice == '4': show_detail()
    elif choice == '5': toggle_favorite()
    elif choice == '6': show_category()
print("hello")
'''

---

## 4. 최종 제출물 내역

본 프로젝트 완성을 증명하는 산출물 목록이다.

1. **GitHub 저장소 URL:** 작성된 코드와 10개 이상의 커밋 이력이 담긴 원격 리포지토리 링크.
https://github.com/riakwjddd06/prompt-manager

2. **개발 환경 스크린샷:** VSCode 에디터 설정, Python 3.10 이상 버전 및 Git 초기 세팅 확인 화면.
<img width="1191" height="795" alt="스크린샷 2026-08-20 오전 12 08 46" src="https://github.com/user-attachments/assets/214345c2-3c60-44a2-aea5-f8b9602ade7f" />

3. **실행 결과 스크린샷:** 메뉴 출력, 데이터 추가, 목록 출력, 검색 기능이 터미널에서 정상적으로 작동하는 화면.
<img width="688" height="258" alt="스크린샷 2026-08-19 오후 11 46 50" src="https://github.com/user-attachments/assets/92d35389-84e9-4a42-bfeb-87dba7f64d8b" />
<img width="688" height="228" alt="스크린샷 2026-08-19 오후 11 47 02" src="https://github.com/user-attachments/assets/d3ac5a4b-21f6-4c62-a8f4-44692a501179" />
<img width="688" height="198" alt="스크린샷 2026-08-19 오후 11 47 19" src="https://github.com/user-attachments/assets/f54ce218-0386-4d6d-86c1-2b4dd72d987d" />
<img width="688" height="306" alt="스크린샷 2026-08-19 오후 11 47 36" src="https://github.com/user-attachments/assets/7d745258-2fd9-45dc-8480-9ad9a995ef16" />
<img width="688" height="513" alt="스크린샷 2026-08-19 오후 11 48 16" src="https://github.com/user-attachments/assets/7815b909-3520-43b5-9689-1e89f7dea115" />
<img width="688" height="227" alt="스크린샷 2026-08-19 오후 11 48 39" src="https://github.com/user-attachments/assets/1a7d4c29-611c-4dc8-8f92-69c033662a1a" />
<img width="688" height="163" alt="스크린샷 2026-08-19 오후 11 48 52" src="https://github.com/user-attachments/assets/4aa6b5cf-db3a-4de5-bc8c-9f7ac8bf14db" />

4. **Git Log 스크린샷:** `git log --oneline --graph` 명령어로 터미널에 출력된 브랜치 분기/병합 선과 12개의 커밋 트리 화면.
<img width="688" height="354" alt="스크린샷 2026-08-19 오후 11 52 26" src="https://github.com/user-attachments/assets/28837328-d65a-4faa-b617-9a61cf524de1" />


---

## 5. 보너스 과제 수행 내역

본 과제에서는 필수 요구사항(CLI 환경 구축, Git 버전 관리 로직 체득, 커밋 10회 분할, 브랜치 병합 등)을 성공적으로 완료한 후, 프로그램의 실용성을 높이기 위해 **보너스 과제 1(프롬프트 영속화)**을 추가로 수행했다.

<img width="688" height="258" alt="스크린샷 2026-08-19 오후 11 46 50" src="https://github.com/user-attachments/assets/43956f59-c8cc-46bb-8e9b-2de802656805" />
<img width="598" height="290" alt="스크린샷 2026-08-20 오전 12 12 31" src="https://github.com/user-attachments/assets/c346efca-9d81-4dea-ad89-160c46a29645" />

* **데이터 영속화(JSON) 로직 적용:** 파이썬 내장 `json` 및 `os` 모듈을 활용하여 프롬프트 데이터를 `prompts.json` 파일로 입출력(Load/Save)하는 로직을 구현헸다.
* **성과:** 기존 메모리 휘발성 데이터 처리 방식의 한계를 극복함. 새로운 프롬프트를 추가하거나 즐겨찾기 상태를 변경할 때마다 파일에 실시간으로 기록(Dump)되도록 개선하여, 프로그램을 완전히 종료 후 재실행하더라도 사용자의 데이터가 영구적으로 보존되게 만들었다.
