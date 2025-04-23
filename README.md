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

- [x] Django 프로젝트 및 가상환경 구성
- [x] 회원가입 / 로그인 / 로그아웃 기능 구현
- [x] 마이페이지 기능 구현 (내 정보, 등록 상품, 신고 내역)
- [x] 상품 등록 및 목록 조회 기능 구현
- [x] 전체 채팅방 기능 구현 (로그인 필요)
- [x] 사용자 / 상품 신고 기능 구현
- [x] 로그인 상태에 따라 메뉴 동적 표시
- [ ] 인증되지 않은 사용자 접근 제한 (`@login_required`)
- [ ] 모든 폼에 CSRF 토큰 적용
- [ ] 입력값 escape 처리 (XSS 방지)
- [ ] 비밀번호 해시 저장 처리 (Django 기본 제공)
- [ ] 이미지 업로드 기능 구현 (ImageField 사용)
- [ ] 관리자 페이지 활성화 및 확인 (`/admin/`)
- [ ] `.env`를 통한 민감정보 관리 (선택 적용)
- [ ] 404 페이지 및 예외 처리 확인
- [ ] 전체 기능 테스트 완료 (테스트 계정 사용)

## 실행 환경 구축
