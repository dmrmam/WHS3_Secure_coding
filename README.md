## WHS 3기 - Secure coding demo market

### 기본 구조
```
tiny_second_hand_shopping_platform/
├── accounts/
│   ├── urls.py
│   └── views.py
├── chat/
│   ├── urls.py
│   └── views.py
├── core/
│   ├── urls.py
│   └── views.py
├── market/
│   ├── settings.py
│   └── urls.py
├── products/
│   ├── urls.py
│   └── views.py
├── reports/
│   ├── urls.py
│   └── views.py
├── templates/
│   ├── index.html
│   ├── accounts/
│   ├── chat/
│   ├── products/
│   └── reports/
├── static/
├── media/
├── manage.py
├── db.sqlite3
└── venv/
```

## 개발 체크리스트

##  사용자 인증/계정 기능
- [x] 회원가입 기능 (`CustomUser` 모델 적용)
- [x] 로그인/로그아웃 기능
- [x] 마이페이지 구현
- [x] 계좌번호 등록 및 수정
- [x] 로그인 시 정지 계정 차단

##  상품 기능
- [x] 상품 등록
- [x] 상품 목록 조회
- [x] 상품 검색 (이름/설명 기반)
- [x] 상품 구매 요청
- [x] 구매 요청 승인 처리
- [x] 판매자 계좌번호/가격 노출

##  신고 기능
- [x] 상품 신고 기능
- [x] 사용자 신고 기능
- [x] 신고 내역 조회 (내가 작성한 신고)

##  관리자 기능
- [x] 관리자 전용 대시보드
- [x] 전체 사용자 목록 조회
- [x] 사용자 밴 / 밴 해제
- [x] 사용자 탈퇴
- [x] 신고 내역 확인

## 채팅 기능 
- [x] 채팅방 생성
