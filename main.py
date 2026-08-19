import streamlit as st
import random

st.set_page_config(page_title="MBTI 포켓몬 추천기", page_icon="✨", layout="centered")

# 포켓몬 공식 아트워크 이미지 (PokeAPI 스프라이트 저장소, 도감번호 기준)
IMG_BASE = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{}.png"

# MBTI별 추천 포켓몬 데이터 (유형별 여러 마리 중 랜덤 추천)
MBTI_POKEMON = {
    "INTJ": [
        {"name": "메타몽", "id": 132, "desc": "치밀한 전략가. 상황에 맞게 완벽하게 변신하는 모습이 INTJ의 계획성과 닮았어요."},
        {"name": "뮤츠", "id": 150, "desc": "혼자만의 세계에서 깊이 사고하는 강력한 전략가 타입이에요."},
    ],
    "INTP": [
        {"name": "메타그로스", "id": 376, "desc": "슈퍼컴퓨터급 두뇌로 문제를 분석하는 모습이 INTP와 닮았어요."},
        {"name": "후딘", "id": 65, "desc": "논리와 분석을 중시하는 이론가 스타일의 포켓몬이에요."},
    ],
    "ENTJ": [
        {"name": "리자몽", "id": 6, "desc": "카리스마 넘치는 리더십으로 무리를 이끄는 강력한 포켓몬이에요."},
        {"name": "망나뇽", "id": 149, "desc": "목표를 향해 거침없이 나아가는 강한 추진력을 가진 타입이에요."},
    ],
    "ENTP": [
        {"name": "또가스", "id": 109, "desc": "예측불가한 아이디어와 논쟁을 즐기는 자유로운 영혼이에요."},
        {"name": "피카츄", "id": 25, "desc": "번뜩이는 재치와 에너지로 주변을 놀라게 하는 타입이에요."},
    ],
    "INFJ": [
        {"name": "뮤", "id": 151, "desc": "신비롭고 깊은 통찰력을 가진 이상주의자 포켓몬이에요."},
        {"name": "라티아스", "id": 380, "desc": "따뜻한 공감능력과 직관력을 가진 포켓몬이에요."},
    ],
    "INFP": [
        {"name": "이브이", "id": 133, "desc": "무한한 가능성과 순수한 감성을 가진 몽상가 포켓몬이에요."},
        {"name": "폴리곤", "id": 137, "desc": "독특한 개성과 상상력이 돋보이는 포켓몬이에요."},
    ],
    "ENFJ": [
        {"name": "루카리오", "id": 448, "desc": "동료를 이끌고 성장시키는 따뜻한 리더 포켓몬이에요."},
        {"name": "가디안", "id": 282, "desc": "카리스마와 배려심을 동시에 가진 타입이에요."},
    ],
    "ENFP": [
        {"name": "피츄", "id": 172, "desc": "밝고 에너지 넘치는 자유로운 영혼의 포켓몬이에요."},
        {"name": "치코리타", "id": 152, "desc": "호기심 많고 사교적인 성격이 잘 어울려요."},
    ],
    "ISTJ": [
        {"name": "롱스톤", "id": 95, "desc": "묵묵히 자기 자리를 지키는 든든한 원칙주의자 포켓몬이에요."},
        {"name": "강철톤", "id": 208, "desc": "단단하고 신뢰할 수 있는 안정적인 타입이에요."},
    ],
    "ISFJ": [
        {"name": "푸린", "id": 39, "desc": "다정하고 헌신적으로 주변을 돌보는 포켓몬이에요."},
        {"name": "럭키", "id": 113, "desc": "따뜻하고 보호본능이 강한 포켓몬이에요."},
    ],
    "ESTJ": [
        {"name": "핫삼", "id": 212, "desc": "체계적이고 강한 실행력을 가진 관리자 타입이에요."},
        {"name": "뿔카노", "id": 111, "desc": "확고한 원칙과 추진력을 가진 타입이에요."},
    ],
    "ESFJ": [
        {"name": "고라파덕", "id": 54, "desc": "사교적이고 다정한 분위기 메이커 포켓몬이에요."},
        {"name": "라이츄", "id": 26, "desc": "친화력이 뛰어나고 주변을 잘 챙기는 타입이에요."},
    ],
    "ISTP": [
        {"name": "고우스트", "id": 92, "desc": "말없이 실력으로 증명하는 실용주의자 포켓몬이에요."},
        {"name": "깜까미", "id": 302, "desc": "냉철하고 독립적인 관찰자 타입이에요."},
    ],
    "ISFP": [
        {"name": "라프라스", "id": 131, "desc": "온화하고 감성적인 예술가적 감각을 가진 포켓몬이에요."},
        {"name": "에브이", "id": 196, "desc": "조용하지만 자기만의 색깔이 뚜렷한 타입이에요."},
    ],
    "ESTP": [
        {"name": "윈디", "id": 59, "desc": "즉흥적이고 대담하게 행동하는 모험가 포켓몬이에요."},
        {"name": "리오르", "id": 447, "desc": "에너지 넘치고 승부욕이 강한 타입이에요."},
    ],
    "ESFP": [
        {"name": "부스터", "id": 136, "desc": "열정적이고 즉흥적인 매력으로 주목받는 포켓몬이에요."},
        {"name": "파이리", "id": 4, "desc": "밝고 화려하게 주목받는 것을 즐기는 타입이에요."},
    ],
}

st.title("✨ MBTI 포켓몬 추천기")
st.write("당신의 MBTI를 선택하면 어울리는 포켓몬을 추천해드려요!")

mbti_list = list(MBTI_POKEMON.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요", mbti_list)

if st.button("포켓몬 추천받기 🎲"):
    pokemon = random.choice(MBTI_POKEMON[selected_mbti])
    st.success(f"**{selected_mbti}** 유형에게 어울리는 포켓몬은...")
    st.header(f"🎉 {pokemon['name']}")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(IMG_BASE.format(pokemon["id"]), use_container_width=True)
    st.write(pokemon["desc"])
    st.balloons()

st.markdown("---")
st.caption("MBTI 유형을 선택하고 버튼을 눌러 나만의 포켓몬을 만나보세요!")
