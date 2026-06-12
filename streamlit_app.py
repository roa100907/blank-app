import streamlit as st

# 웹 페이지 제목 및 설명
st.title("📚 장르별 소설 추천 프로그램")
st.write("좋아하는 소설 장르를 선택하시면 딱 맞는 책을 추천해 드립니다.")

st.markdown("---")  # 화면 구분선

# 1. 데이터 정의 (장르와 도서 매칭)
genres = ("한국 고전 소설", "공포", "로맨스", "추리")
books = ("허생전", "드라큘라", "오만과 편견", "셜록 홈즈")

# 2. 스트림릿 위젯으로 입력 받기 (드롭다운 메뉴)
selected_genre = st.selectbox(
    "좋아하는 소설 장르를 선택해주세요:",
    genres
)

# 3. 로직 처리 및 화면 결과 출력
if selected_genre:
    # 선택한 장르가 몇 번째 인덱스인지 찾기
    idx = genres.index(selected_genre)
    recommended_book = books[idx]
    
    # 결과 출력
    st.subheader("💡 추천 결과")
    st.success(f"**[{selected_genre}]** 장르를 좋아하는 당신에게 추천하는 소설은 바로 **'{recommended_book}'** 입니다!")