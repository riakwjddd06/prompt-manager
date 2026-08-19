# 기본 프롬프트 3개 세팅
prompts = [
    {"title": "사실적인 흑백 사진", "content": "레퍼런스 이미지를 똑같이 베끼지 말고, 일러스트 느낌 없이 완전히 사실적인 흑백 사진 스타일로 독창적인 구도를 만들어 줘.", "category": "이미지 생성", "favorite": True},
    {"title": "객관적인 도서 추천", "content": "이전 대화 맥락은 무시하고, 쇼펜하우어 관련 도서들을 아주 객관적인 시각에서 추천해 줘.", "category": "텍스트 생성", "favorite": False},
    {"title": "자원봉사 자소서 수정", "content": "대구국제뮤지컬페스티벌 자원봉사 지원서 초안이야. 과장된 칭찬이나 미사여구는 전부 빼고, 내 경험 위주로 건조하고 사실적으로 수정해 줘.", "category": "텍스트 생성", "favorite": False}
]

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
    