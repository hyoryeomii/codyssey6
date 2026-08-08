사용자의 운동 목적, 체력 수준, 이용 가능한 시간에 맞춰 최적의 운동 루틴을 추천해 주는 웹 서비스

- **라이브 시연 주소**: https://codyssey6.vercel.app
- **GitHub 저장소**: https://github.com/hyoryeomii/codyssey6

---

## 1. 서비스 기획

### 1.1 기획 배경 및 목적

- **기획 배경**: 운동을 시작하고 싶지만 자신에게 맞는 루틴을 구성하기 어려워하는 운동 초보자 및 바쁜 현대인을 위해서 기획함
- **서비스 목적**: 복잡한 회원가입 과정 없이 운동 목적, 체력, 제약 시간을 입력받아 AI가 즉시 실행 가능한 1:1 맞춤형 피트니스 가이드라인 제공
- **타겟 사용자**:
    - 홈트레이닝을 시작하려 하나 루틴 작성이 막막한 운동 초보자
    - 짧은 시간(20~30분) 동안 효율적인 운동 계획이 필요한 직장인 및 학생

### 1.2 페이지 및 섹션 구조

본 서비스는 단일 페이지 내 3개의 독립된 섹션으로 구성되어 있으며, 메뉴 이동(네비게이션)을 지원함

| 섹션명 | 역할 및 기능 | 네비게이션 이동 방식 |
| --- | --- | --- |
| **Hero 섹션** | 서비스 타이틀, 주요 특징 소개 및 루틴 작성 유도 | `href="#generator"` 앵커 이동 |
| **Generator 섹션** | 운동 조건 입력 폼(Form) 및 AI 생성 결과 렌더링 영역 | 폼 제출 시 해당 영역으로 스크롤 이동 |
| **FAQ 섹션** | 서비스 이용 방법 및 자주 묻는 질문(FAQ) 3종 제공 | 하단 고정 안내 영역 |

### 1.3 AI 기능 정의

- **입력 (Input)**: 운동 목적(다이어트/근력 증가/체력 향상/유지), 현재 체력(초급/중급/고급), 운동 가능 시간(20분/30분/45분/60분 이상)
- **출력 (Output)**: 준비운동, 본운동(운동별 세트/횟수/휴식시간), 마무리 스트레칭이 포함된 마크다운 구조화 텍스트
- **사용자 제공 가치**: 데이터 기반의 체계적인 운동 계획을 즉시 생성하여 운동 루틴 구성에 소요되는 시간과 비용 절감

---

## 2. 🛠 기술 스택 및 프로젝트 구조

### 2.1 기술 스택

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla JS), Marked.js (CDN)
- **Backend**: Python (Vercel Serverless Function)
- **AI Integration**: OpenAI API (gpt-4o-mini)
- **Deployment**: Vercel

**Frontend (프론트엔드)**: 사용자가 직접 접하는 웹 화면(UI)을 구성하고, 입력받은 조건 데이터 전송 및 AI 응답 결과를 시각적으로 렌더링하는 역할 (HTML5, CSS3, Vanilla JS, Marked.js)

**Backend (백엔드)**: 프론트엔드로부터 전달받은 요청 데이터를 처리하고, OpenAI API와의 보안 통신을 담당하여 맞춤형 운동 루틴 데이터를 반환하는 역할 (Python, Vercel Serverless Function)

### 2.2 디렉토리 구조

```
├── api/
│   └── generate.py      # Vercel Serverless API (OpenAI 통신 백엔드)
├── css/
│   └── style.css        # 반응형 UI 및 마크다운 결과 스타일시트
├── js/
│   └── main.js          # 비동기 통신(fetch) 및 Marked.js 동적 파싱
├── images/
│   ├── preview.png      # 메인 캡처 이미지
│   └── mobile.png       # 모바일 검증 캡처 이미지
├── index.html           # 메인 페이지 (3개 섹션 구조)
├── requirements.txt     # 파이썬 서버리스 의존성 패키지
└── vercel.json          # Vercel 서버리스 라우팅 설정 파일
```

- generate.py(백엔드): 프론트엔드 요청 수신 및 OpenAI API 통신/응답을 처리하는 서버리스 함수
- style.css(프론트-디자인): 반응형 레이아웃, 마크다운 결과 스타일 및 마이크로 인터랙션 정의
- main.js(프론트-동작): 입력 데이터 수집, 백엔드 비동기 통신(fetch) 및 Marked.js 동적 파싱 제어
- index.html(프론트-구조): Hero, Generator, FAQ 3개 섹션으로 구성된 메인 단일 페이지
- requirements.txt(설정): 파이썬 서버리스 환경 실행에 필요한 패키지(requests 등) 명세
- vercel.json(배포): Vercel 서버리스 라우팅 및 API 경로 연결 설정 파일

## 3. 상세 개발 과정

### 3.1 개발 진행 단계

```
[1단계: 환경 설정] ➔ [2단계: 백엔드 구축] ➔ [3단계: 프론트엔드 통신] ➔ [4단계: UI 파싱 개선] ➔ [5단계: 반응형 검증]
```

1. **1단계: 프로젝트 초기화 및 환경 구성**
    - 프로젝트 기본 폴더 구조 창설 (`index.html`, `css/`, `js/`, `api/`)
    - Git 저장소 생성 및 초기 커밋(`init commit`) 등록
    - Vercel 연동 및 `OPENAI_API_KEY` 환경변수 등록
2. **2단계: 백엔드 API 구현 (Vercel Serverless)**
    - Python 기반 `/api/generate.py` 개발
        - HTTP POST 요청 처리 및 프론트엔드 수신 데이터(목적/체력/시간) 파싱
    - OpenAI API 호출 프롬프트 엔지니어링 (준비운동-본운동-마무리 스트레칭 구조 규격화)
3. **3단계: 프론트엔드 비동기 통신 구현**
    - HTML/CSS 반응형 입력 폼 제작
    - `js/main.js` 내 `fetch()` 함수를 통한 백엔드 API 비동기 요청 처리
    - 로딩 안내 메시지 및 예외 처리(Error Handling) 구문 작성
4. **4단계: 마크다운 파싱 및 UX 개선** 
    - AI 응답 데이터에 포함된 마크다운 기호(`###`, `*`)가 웹 화면에 raw text로 노출되는 문제 발견
    - `Marked.js` 라이브러리를 도입하여 HTML 태그로 변환 렌더링
    - 생성 완료 후 결과 영역으로 자동 부드러운 스크롤(`scrollIntoView`) 추가
5. **5단계: 반응형 웹 검증 및 최종 배포**
    - Desktop, Tablet, Mobile 디바이스 화면 비율 검증
    - GitHub `main` 브랜치 푸시 및 Vercel 자동 배포(Continuous Deployment) 완료

### 3.2 AI 코딩 도구 활용

<img width="920" height="717" alt="image" src="https://github.com/user-attachments/assets/c804c637-7d00-4725-a9f8-fbc4071fcfc9" />


<img width="934" height="619" alt="image" src="https://github.com/user-attachments/assets/d4e456f6-707e-414d-949f-00b89b458af9" />


▲ openAI, gemini 활용하여 Vercel 파이썬 백엔드 작성에 대해 대화한 화면 (일부 캡쳐)

- **주요 활용 내용**:
    1. **백엔드 API 구축**: Vercel 서버리스 환경에 맞춘 Python 요청 핸들러 구조 설계 지원
    2. **마크다운 파싱**: Marked.js 라이브러리를 활용한 동적 HTML 렌더링 로직 작성 및 트러블슈팅
    3. **GA4 연동**: 구글 애널리틱스 추적 태그 이식 및 수집 검증 과정 안내

## 4. 트러블슈팅 및 Git 커밋 이력

개발 진행 과정에서 발생한 주요 문제점과 수정 내역, Git 커밋 로그 정리

| **구분** | **발생 이슈 / 개선 목적** | **해결 내용 (코드 수정)** | **Git 커밋 메시지 (Commit Msg)** |
| --- | --- | --- | --- |
| **백엔드** | Vercel 서버리스 파이썬 API 통신 오류 발생 | `http.server` 핸들러 구조 수정 및 JSON 파싱 처리 | `fix: update python backend API handler` |
| **렌더링** | AI 응답의 마크다운 기호(`###`, `**`) 원문 노출 | `Marked.js` 추가 및 `innerHTML = marked.parse()` 적용 | `style: apply markedjs for markdown rendering` |
| **UI/UX** | 생성 결과 글자 간격 및 리스트 들여쓰기 정돈 | `style.css` 내 `#resultContainer` 전용 스타일 추가 | `refactor: clean up result spacing and layout` |
| **모바일** | 스마트폰 화면 접속 시 입력 폼 가로 쏠림 현상 | CSS `@media` 쿼리 수정 및 Flex/Grid 레이아웃 최적화 | `design: fix mobile responsive view layout` |

## 5. 화면 검증 및 결과 (UI / Mobile Test)

### 5.1 Desktop & Mobile 화면 검증

- **PC 화면**: 3개 섹션(Hero, Generator, FAQ)이 넓은 화면에 균형 있게배치됨

<img width="1657" height="1063" alt="image" src="https://github.com/user-attachments/assets/bcb76172-428b-4e50-b30f-d3d4966f666c" />


▲ pc 전체 화면 스크린샷

- **Mobile 화면**: iPhone / Android 스마트폰 접속 시 화면 깨짐 없이 한눈에 들어오는 반응형 수직 레이아웃 구현 완료
    
<img width="460" height="1000" alt="image" src="https://github.com/user-attachments/assets/e48113c8-0a72-49dc-a043-3ef7ccfb057b" />

    
<img width="460" height="1000" alt="image" src="https://github.com/user-attachments/assets/44bf27db-9632-4d64-bc78-fd2a2cf09ee3" />

    

▲ 모바일 화면 스크린샷

### 5.2 결과 출력 화면

<img width="1027" height="998" alt="image" src="https://github.com/user-attachments/assets/7e790fd6-32d4-405c-8d22-eb7f5f6cf513" />


▲ AI가 출력한 운동 루틴이 `Marked.js`를 통해 볼드체, 제목, 불렛 포인트(•, ◦)로 정상 파싱되어 출력됨

## 6. 성과 및 향후 개선 계획

### 6.1 주요 성과

- 단일 페이지(Single Page) 안에서 3개 섹션 간 원활한 네비게이션 구현
- OpenAI API Key를 Vercel 서버리스 환경변수로 은닉하여 백엔드 보안성 확보
- `Marked.js` 라이브러리 연동으로 AI 생성 텍스트의 가독성 대폭 향상

### 6.2 향후 개선 계획 (사용자 피드백 기반)

실제 사용자(지인) 테스트를 실시하여 수집된 UI/UX 개선 피드백을 바탕으로 향후 아래 사항들을 고도화할 예정

1. **입력 폼 가이드라인 강화 (체력 수준)**
    - **피드백**: 초급/중급/고급 선택 시 직관적인 기준이 부족함
    - **개선안**: 각 선택지에 툴팁이나 보조 설명을 추가하여 사용자 선택 편의성 제공 (예: 초급 - 운동 입문자 / 중급 - 주 2~3회 운동 / 고급 - 주 4회 이상 운동)
2. **가독성 및 텍스트 레이아웃 최적화**
    - **피드백**: 생성된 결과물의 글자 크기 및 줄 간격 조정 필요
    - **개선안**: 결과 영역의 글자 크기를 확충하고 요소 간 간격을 좁혀 모바일 및 데스크톱 환경에서의 시각적 몰입도 향상
3. **운동 동작 이미지/시각 자료 제공**
    - **피드백**: 텍스트 형태의 루틴만으로는 정확한 운동 동작을 파악하기 아쉬움
    - **개선안**: 주요 운동 항목별 예시 동작 이미지 또는 gif 가이드를 함께 출력하여 루틴의 실행 가능성 증대
4. **부가 유틸리티 기능 추가**
    - **원클릭 복사**: 생성된 루틴을 클립보드로 즉시 복사하는 기능 제공
    - **로컬 저장소 연동**: `LocalStorage`를 활용해 최근 생성한 루틴 기록을 재확인할 수 있는 히스토리 기능 구현

## 7. 학습 성과 및 핵심 개념 정리

본 프로젝트를 진행하며 습득한 웹 기술의 핵심 개념과 동작 원리는 다음과 같습니다.

### 7.1 웹 삼총사(HTML/CSS/JS)의 역할 분담

- **HTML (뼈대)**: 웹 페이지의 기본 구조와 콘텐츠(헤더, 입력 폼, 버튼, 결과 영역 등)를 정의함
- **CSS (디자인)**: 레이아웃, 색상, 폰트, 반응형 미디어 쿼리, 클릭 및 등장 애니메이션(마이크로 인터랙션) 등 시각적 스타일링을 담당함
- **JavaScript (동작 및 통신)**: 사용자 입력 이벤트 감지, 백엔드 API와의 비동기 통신(fetch), DOM 객체 조작 및 Marked.js를 이용한 동적 UI 렌더링을 제어함

### 7.2 사용자 입력부터 화면 반영까지의 데이터 흐름

1. **사용자 입력 수진**: 사용자가 운동 목적, 체력 수준, 가능 시간을 선택하고 생성 버튼 클릭
2. **이벤트 감지 및 비동기 요청**: JS가 `submit` 이벤트를 가로채 데이터를 JSON 형태로 변환 후 `fetch('/api/generate', { method: 'POST' })` 호출
3. **백엔드 처리**: Python API가 요청을 수신하여 OpenAI API로 프롬프트 전송 및 응답(운동 루틴) 생성
4. **응답 수신 및 UI 반영**: JS가 백엔드의 JSON 응답을 받아 Marked.js로 마크다운을 HTML로 파싱한 후, `innerHTML`을 통해 화면에 동적 렌더링 및 자동 스크롤 적용

### 7.3 Vercel Serverless Function 및 프론트-백엔드 호출 구조

- **Serverless Function이란**: 별도의 24시간 상시 가동 서버를 구축·관리할 필요 없이, 요청이 들어올 때만 개별 함수(코드)가 실행되는 cloud 아키텍처임
- **호출 구조**: 프론트엔드(`main.js`)는 동일한 도메인 내의 `/api/generate` 상대 경로로 HTTP POST 요청을 보냅니다. Vercel 내부 라우팅(`vercel.json`)이 이를 받아 Python 백엔드 환경(`api/generate.py`)을 순간적으로 실행하여 OpenAI 통신을 처리하고 결과를 반환함

### 7.4 API 키 환경 변수 관리의 필요성

- **보안 위험성**: OpenAI API 키를 프론트엔드 JavaScript 파일에 직접 작성할 경우, 웹 브라우저의 '소스 보기'나 개발자 도구를 통해 누구에게나 API 키가 노출됩니다.
- **해결 방안**: API 키를 Vercel 서버리스 서버의 환경 변수(`OPENAI_API_KEY`)로 등록하고 백엔드(Python)에서만 접근하도록 설계하여, 외부 노출 및 도용으로 인한 무단 비용 청구를 방지합니다.

### 7.5 로컬 환경 vs 배포 환경 및 수정·재배포 흐름

- **로컬 환경**: 개발자 개인 컴퓨터 내부에서 동작하는 테스트 환경으로, 빠른 수정과 디버깅이 가능함
- **배포 환경**: Vercel 등 cloud 인프라에 올려 실제 전 세계 사용자가 접속 가능한 인터넷 서비스 상태임
- **수정 및 재배포 흐름**:
`[로컬 코드 수정/테스트]` ➔ `[Git 저장소로 커밋]` ➔ `[GitHub 푸시 (git push origin main)]` ➔ `[Vercel CI/CD 트리거 및 자동 빌드/배포]`

### 7.6 AI 코딩 도구 디버깅 및 문제 해결 능력

- AI 도구가 생성한 코드라도 완벽하지 않으므로, 오류의 원인(원인 파싱)을 정확히 분석하는 능력이 필수적임
- **실제 트러블슈팅 경험**:
    - Python 서버리스 실행 시 HTTP 핸들러 파싱 방식 오류 발생 ➔ Vercel 공식 규격에 맞춰 `BaseHTTPRequestHandler` 구조로 수정 요구
    - AI 응답 문맥이 raw text 마크다운 기호로 노출 ➔ 렌더링 방식의 한계를 파악하고 `Marked.js` 라이브러리를 직접 도입하여 해결

## 8. 보너스 과제: 사용자 경험(UX) 및 측정 고도화

### 8.1 마이크로 인터랙션 (Micro-interaction) 적용

- **버튼 터치 반응**: 생성 버튼 클릭 시 `transform: scale(0.96)`의 압축 애니메이션을 적용하여 직관적인 클릭 피드백 제공
- **결과 페이드인(Fade-in) 애니메이션**: AI 생성 결과가 출력될 때 `@keyframes fadeIn` 효과를 적용하여 부드럽고 자연스러운 화면 전환 UX 선사

### 8.2 데이터 측정 고도화 (Google Analytics 4)

- **방문자 분석 환경 구축**: Google Analytics 4(GA4) 스크립트를 `index.html` 상단에 이식.
- **측정 및 개선 계획**: 일간 방문자 수, AI 루틴 생성 버튼 클릭 이벤트를 수집하여 서비스 이탈율과 사용자 반응성을 지속적으로 모니터링 가능한 기반 마련

<img width="1902" height="563" alt="image" src="https://github.com/user-attachments/assets/b68cae40-4ff1-4268-a7ea-3746a694cf0e" />


▲ 실시간 데이터 수집 검증: GA4 실시간 보고서를 통해 웹사이트 접속자의 조회수(Page View) 및 활성 사용자 이벤트가 실시간으로 정상 수집됨을 확인
