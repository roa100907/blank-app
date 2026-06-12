import streamlit as str

# 웹 페이지 제목 설정
st.title("📚 장르별 소설 추천 프로그램")
st.markdown("좋아하는 소설 장르를 선택하시면 딱 맞는 책을 추천해 드립니다!")

---

# 1. 장르 및 도서 데이터 정의
genres = ("한국 고전 소설", "공포", "로맨스", "추리")
books = ("허생전", "드라큘라", "오만과 편견", "셜록 홈즈")

# 2. 스트림릿 위젯을 이용한 입력 받기
# 사용자가 직관적으로 선택할 수 있도록 selectbox를 사용했습니다.
selected_genre = st.selectbox(
    "좋아하는 소설 장르를 선택해주세요:",
    genres
)

# 3. 로직 처리 및 결과 출력
# 선택된 장르의 인덱스를 찾아 매칭되는 책을 가져옵니다.
if selected_genre in genres:
    idx = genres.index(selected_genre)
    recommended_book = books[idx]
    
    # 구분선 추가 후 결과 출력
    st.divider()
    st.subheader("💡 추천 결과")
    st.success(f"**[{selected_genre}]** 장르를 좋아하는 당신에게 추천하는 소설은 **'{recommended_book}'** 입니다!")