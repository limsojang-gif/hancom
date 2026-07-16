# Claude로 웹사이트 설계 · 디자인하기 — 정리 가이드

> 원본: [hancom-nine.vercel.app/claude-make-web.html](https://hancom-nine.vercel.app/claude-make-web.html) 내용 + 개인 학습 노트를 함께 정리한 문서입니다.

![워크플로 다이어그램](workflow-diagram.png)

전체 흐름은 크게 세 단계입니다. **① Claude Code로 웹사이트 뼈대 만들기 → ② frontend-design 공식 스킬로 디자인 입히기 → ③ design.md로 디자인 시스템을 재사용/확장하기.** 아래에서 각 단계를 순서대로, 그리고 스킬 설치 방법까지 차근차근 정리했습니다.

---

## 1단계. Claude Code로 웹사이트 만들기

Claude Code는 터미널에서 자연어로 코드를 만드는 AI 도구입니다. HTML·CSS·JavaScript를 직접 타이핑하지 않아도, 요구사항을 문장으로 설명하면 동작하는 사이트를 완성할 수 있습니다.

**진행 순서**

1. **Plan Mode로 설계** — `Shift + Tab`을 눌러 Plan Mode로 전환한 뒤, 요구사항을 정리해서 전달합니다. Claude가 먼저 구현 계획을 제시하고, 이를 승인해야 실제 코드 작성이 시작됩니다.
2. **HTML/CSS/JS 생성 및 부분 수정** — 승인된 계획대로 코드가 생성되고, 이후 세부 요청으로 부분 수정을 이어갑니다.
3. **스크린샷 · 리뷰 반복** — 결과물을 캡처해서 보여주고 피드백을 주고받으며 다듬습니다.

**요청 예시**

```
포트폴리오 랜딩 페이지 만들어줘
- 히어로 섹션 + 소개 + 프로젝트 카드 3개 + 연락처 푸터
- 단일 HTML, CSS·JS 인라인, 모바일 반응형
```

> 💡 **핵심 팁**: 규모가 큰 작업일수록 코딩 전 Plan Mode 단계에서 시간을 들이는 것이 결과물 품질에 큰 차이를 만듭니다. "예쁘게 만들어줘"보다 구체적인 요구사항(대상, 목적, 구성 요소, 파일 구조)을 적을수록 결과가 좋아집니다.

---

## 2단계. frontend-design 공식 스킬 설치 및 사용

`frontend-design`은 Claude의 공식 UI 디자인 스킬입니다. 별도의 디자인 철학 문서 없이도, 웹사이트 관련 요구사항이 들어오면 자동으로 트리거됩니다.

### 2-1. 스킬 설치 (Claude Code / 터미널)

터미널 명령 앞에는 `!`를 붙여서 실행합니다 (셸 명령 실행 표시).

```
!npx skills add https://github.com/anthropics/skills --skill frontend-design
```

- 설치되는 것: 스킬 파일 — **프론트엔드 디자인(frontend-design)**

설치가 끝나면 반드시 스킬 목록을 다시 불러와야 합니다.

```
/reload-skills
```

### 2-2. 스킬 실행

```
/frontend-design
```

이때도 `Shift + Tab`으로 **Plan Mode**로 전환한 상태에서 작업하면, 세부 사항(색상, 톤, 레이아웃 등)을 조정하기 훨씬 수월합니다.

### 2-3. md 파일을 지정해서 실행하기

이미 만들어둔 디자인 명세(`.md`) 파일이 있다면, 파일을 직접 지정해서 스킬을 실행할 수 있습니다.

```
/frontend-design@파일명.md
```

### 2-4. Windows 환경 전역 설치법 (재정리)

Windows에서는 사용자 폴더(C드라이브) 기준으로 아래 순서를 따릅니다.

1. **C드라이브 사용자 폴더**에서 아래 명령 실행:
   ```
   npx skills add anthropics/skills --skill frontend-design
   ```
2. 설치된 스킬 폴더를 복사해서 Claude 설정 폴더에 붙여넣기:
   - 원본: `C:\Users\Har27\.agents\skills\frontend-design`
   - 붙여넣을 위치: `C:\Users\Har27\.claude`

> ⚠️ 사용자 폴더 이름(`Har27` 등)은 각자의 Windows 계정명으로 바뀌므로, 실제 경로는 본인 환경에 맞게 확인해야 합니다.

### 2-5. frontend-design의 4가지 토큰 시스템

스킬이 디자인을 잡을 때 기준으로 삼는 4가지 요소입니다.

| 토큰 | 내용 |
|---|---|
| 색(Color) | 4~6개의 이름 붙은 hex 팔레트 |
| 타이포(Typography) | 디스플레이·본문·유틸리티 서체 구분 |
| 레이아웃(Layout) | ASCII 와이어프레임으로 구조 표현 |
| 시그니처(Signature) | 그 페이지만의 기억에 남는 시그니처 요소 하나 |

**권장 파일 구조**

```
tokens.css   → 팔레트·글씨·간격을 :root 변수로 선언
styles.css   → var(--token)만 사용 (색상 코드 직접 하드코딩 금지)
index.html   → 시맨틱 마크업 구조만 담당
```

이렇게 분리해두면, **색상 하나만 tokens.css에서 수정해도 사이트 전체에 일괄 반영**되는 장점이 있습니다.

**요청 예시**

```
커피 원두 구독 서비스 랜딩 페이지 만들어줘
- 대상: 원두 마니아, 목적: 구독 전환
- tokens.css·styles.css·index.html 분리
```

> 💡 슬래시 명령(`/frontend-design`)을 직접 입력하지 않아도, 디자인 관련 요청이면 스킬이 자동으로 활성화되는 경우가 많습니다.

---

## 3단계. design.md로 디자인 시스템 재사용 · 확장하기

### 3-1. design.md란

`design.md`는 한 브랜드(또는 한 사이트)의 색·글씨·간격·구성 요소를 정리해 둔 **디자인 설계도** 파일입니다. 이 설계도 파일만 전달하면, Claude가 같은 무드(분위기)의 사이트를 새로 조립해낼 수 있습니다.

### 3-2. 참고할 수 있는 갤러리

- [getdesign.md](https://getdesign.md/) — design.md 형식으로 정리된 디자인 명세 모음
- [getdesign.kr](https://getdesign.kr/) — 토스·배달의민족·클래스101 등 한국 서비스 14개의 디자인 시스템을 정리한 사이트

### 3-3. design.md 작성 예시 (BMW M 스타일)

```
- 캔버스: 검은색 #000
- 포인트: 파랑·남색·빨강 M 삼색 띠
- 타이포: 제목 700 weight(굵은 대문자), 본문 300 weight(얇게)
- 모서리: 직각 (radius 0)
```

**요청 예시**

```
ex_design/bmw_design.md 기반으로 단일 HTML 만들어줘
- bmw-tokens.css·bmw-styles.css·bmw.html 분리
```

### 3-4. 마음에 드는 사이트로 design.md 직접 만들기

마음에 드는 사이트 링크가 있다면, 그 링크를 Claude Code에게 전달하고 **"이 사이트를 참고해서 디자인 명세서(design.md)를 만들어줘"** 라고 요청하면 됩니다. 이렇게 만든 design.md는 이후 다른 페이지 작업에도 그대로 재사용할 수 있습니다.

---

## 4. 모델 선택 팁

| 작업 성격 | 추천 모델 |
|---|---|
| 전체 설계 · 디자인 계획 수립 (Plan Mode 등 복잡한 판단이 필요한 작업) | **Opus** |
| 단순 반복 작업, 사소한 수정 | **Haiku** |

---

## 전체 흐름 한눈에 보기

1. `Shift+Tab`으로 Plan Mode 진입 → 요구사항 설명 → 계획 승인 → 웹사이트 뼈대 생성
2. `!npx skills add ...` 로 frontend-design 스킬 설치 → `/reload-skills` → `/frontend-design` 실행 (또는 자동 트리거) → 4대 토큰 기준으로 디자인 적용
3. 마음에 드는 사이트나 브랜드를 기반으로 `design.md` 작성 → 이후 프로젝트에 재사용
4. 복잡한 설계는 Opus, 단순 작업은 Haiku로 모델을 나눠 사용
