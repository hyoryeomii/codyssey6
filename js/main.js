const form = document.getElementById("routineForm");
const message = document.getElementById("message");

form.addEventListener("submit", async function (e) {

    e.preventDefault();

    const goal = document.getElementById("goal").value;
    const level = document.getElementById("level").value;
    const time = document.getElementById("time").value;

    // 입력값 검증
    if (!goal || !level || !time) {
        message.style.color = "red";
        message.textContent = "모든 항목을 입력해주세요.";
        return;
    }

    message.style.color = "#333";
    message.textContent = "AI가 운동 루틴을 생성하는 중입니다...";

    try {

        const response = await fetch("/api/generate.py", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                goal,
                level,
                time
            })

        });

        if (!response.ok) {
            throw new Error("서버 요청 실패");
        }

        const result = await response.json();

        console.log(result);

        message.style.color = "green";
        message.textContent = "운동 루틴 생성이 완료되었습니다!";

        // 추후 결과 출력 영역에 result를 표시하면 됩니다.
        // 예:
        // document.getElementById("result").innerText = result.routine;

    } catch (error) {

        console.error(error);

        message.style.color = "red";
        message.textContent = "서버와 통신 중 오류가 발생했습니다.";

    }

});