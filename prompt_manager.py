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


while True:
    show_menu()
    choice = input("선택: ")
    if choice == '0':
        print("종료합니다.")
        break
    elif choice == '1':
        add_prompt()  
    elif choice == '2':
        show_list()   