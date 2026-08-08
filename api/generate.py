import json
import os
from http.server import BaseHTTPRequestHandler
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            # 1. 요청 데이터 읽기
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            body = json.loads(post_data.decode('utf-8'))

            goal = body.get("goal")
            level = body.get("level")
            time = body.get("time")

            # 2. 입력값 검증
            if not goal or not level or not time:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(json.dumps({"error": "모든 항목을 입력해주세요."}, ensure_ascii=False).encode('utf-8'))
                return

            # 3. 프롬프트 구성 및 OpenAI API 호출
            prompt = f"""
당신은 전문 퍼스널 트레이너입니다.

다음 정보를 참고하여 운동 루틴을 작성하세요.

운동 목적: {goal}
체력 수준: {level}
운동 가능 시간: {time}

아래 형식으로 작성하세요.

1. 준비운동
2. 본운동
3. 마무리 스트레칭

각 운동마다 세트 수와 횟수도 포함해주세요.
"""

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "당신은 전문 헬스 트레이너입니다."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )

            routine = response.choices[0].message.content

            # 4. 정상 응답 반환 (JS 프론트엔드 호환성을 위해 routine과 result 모두 포함)
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()

            response_body = json.dumps({"routine": routine, "result": routine}, ensure_ascii=False)
            self.wfile.write(response_body.encode('utf-8'))

        except Exception as e:
            self.send_response(500)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}, ensure_ascii=False).encode('utf-8'))

    def do_OPTIONS(self):
        # CORS 예비 요청 처리
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()