import json
import os

from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)


def handler(request):
    # POST만 허용
    if request.method != "POST":
        return {
            "statusCode": 405,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "error": "Method Not Allowed"
            }, ensure_ascii=False)
        }

    try:
        body = request.get_json()

        goal = body.get("goal")
        level = body.get("level")
        time = body.get("time")

        # 입력값 검증
        if not goal or not level or not time:
            return {
                "statusCode": 400,
                "headers": {
                    "Content-Type": "application/json"
                },
                "body": json.dumps({
                    "error": "모든 항목을 입력해주세요."
                }, ensure_ascii=False)
            }

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
                {
                    "role": "system",
                    "content": "당신은 전문 헬스 트레이너입니다."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7
        )

        routine = response.choices[0].message.content

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "routine": routine
            }, ensure_ascii=False)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "error": str(e)
            }, ensure_ascii=False)
        }