#!/usr/bin/env python3


LAST_NAME = "장"


# 대법원 인명용 한자표
# 대한민국에서 사람 이름으로 사용할 수 있는 한자 목록
# https://hanja.dict.naver.com/category/name
# https://help.scourt.go.kr/nm/min_17/min_17_3/min_17_3l/index.html
NAME_CHARS_LEGAL = """
	가 각 간 갈 감 갑 강 개 객 갱 
	갹 거 건 걸 검 겁 게 격 견 결 
	겸 경 계 고 곡 곤 골 공 곶 과 
	곽 관 괄 광 괘 괴 괵 굉 교 구 
	국 군 굴 궁 권 궐 궤 귀 규 균 
	귤 극 근 글 금 급 긍 기 길 김 
	끽 

	나 난 날 남 납 낭 내 녁 년 념 
	녑 녕 노 농 뇌 뇨 누 눈 눌 뉴 
	니 닉 닐 

	다 단 달 담 답 당 대 댁 덕 도 
	독 돈 돌 동 두 둔 둘 등 

	라 락 란 랄 람 랍 랑 래 략 량 
	려 력 련 렬 렴 렵 령 례 로 록 
	롱 뢰 료 룡 루 류 륙 륜 률 륭 
	륵 름 릉 리 린 림 립 

	마 막 만 말 망 매 맥 맹 멱 면 
	멸 명 몌 모 목 몰 몽 묘 무 묵 
	문 물 미 민 밀 박 반 발 방 배 
	백 번 벌 범 법 벽 변 별 병 보 
	복 볼 봉 부 분 불 붕 비 빈 빙 

	사 삭 산 살 삼 삽 상 새 색 생 
	서 석 선 설 섬 섭 성 세 소 속 
	손 솔 송 쇄 쇠 수 숙 순 술 숭 
	쉬 슬 습 승 시 식 신 실 심 십 
	쌍 

	아 악 안 알 암 압 앙 애 액 앵 
	야 약 양 어 억 언 얼 엄 업 에 
	엔 여 역 연 열 염 엽 영 예 오 
	옥 온 올 옹 와 완 왕 왜 외 요 
	욕 용 우 욱 운 울 웅 원 월 위 
	유 육 윤 율 융 은 을 음 읍 응 
	의 이 익 인 일 임 입 잉 

	자 작 잔 잠 잡 장 재 쟁 저 적 
	전 절 점 접 정 제 조 족 존 졸 
	종 좌 주 죽 준 줄 중 즉 즐 즙 
	증 지 직 진 질 짐 집 징 

	차 착 찬 찰 참 창 채 책 처 척 
	천 철 첨 첩 청 체 초 촉 촌 총 
	촬 최 추 축 춘 출 충 췌 취 측 
	치 칙 친 칠 침 칩 칭 

	쾌 

	타 탁 탄 탈 탐 탑 탕 태 탱 터 
	토 톤 통 퇴 투 퉁 특 틈 

	파 판 팔 패 팽 퍅 편 폄 평 폐 
	포 폭 표 품 풍 피 픽 필 핍 

	하 학 한 할 함 합 항 해 핵 행 
	향 허 헌 헐 험 혁 현 혈 협 형 
	혜 호 혹 혼 홀 홍 화 확 환 활 
	황 회 획 횡 효 후 훈 훌 훙 훤 
	훼 휘 휴 휼 흉 흔 흘 흠 흡 희 
	힐
	"""
NAME_CHARS_LEGAL = NAME_CHARS_LEGAL.split()


import unicodedata
def len_nfd(c):
    return len(unicodedata.normalize("NFD", c))


# 받침 없는 한글은 외국인도 따라하기 쉬움
# 받침 없는 한글
# = 초성 중성 종성 중 종성이 없는 한글
# = 유니코드 조합형(NFD)로 변환하면 초성+중성+종성으로 나뉘는데
#   이 때, 종성이 없는 한글
NAME_CHARS_2 = [x for x in NAME_CHARS_LEGAL if len_nfd(x) < 3]


# 직접 선택한 한글
NAME_CHARS_LIKED = """
    가 고 기 거 구 규
    나 내 노
    다 대 도 두
    라 래 려 례 로 리 루 료
    마 모 무 미
    보 부 비 배
    새 서 세 소 수 시
    아 어 여 예 오 요 우 유 의 이
    자 재 저 제 조 주 지
    차 초 치 채 추
    태
    하 해 허 혜 호 후
    """
NAME_CHARS_LIKED = NAME_CHARS_LIKED.split()


NAME_CHARS = NAME_CHARS_LIKED


print("# 아이 이름 후보\n\n")

n = 0
for i in NAME_CHARS:
	print("## %s%s* "%(LAST_NAME,i))
	for j in NAME_CHARS:
		print("%s%s%s "%(LAST_NAME,i,j), end='')
		n = n+1
	print("\n\n")


print("## 통계")
print("총 %d개 이름" % n)
