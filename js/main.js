const form = document.getElementById("routineForm");
const message = document.getElementById("message");
const resultContainer = document.getElementById("resultContainer");

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
    
    // 생성 시작 시 이전 결과 숨기기
    resultContainer.style.display = "none";
    resultContainer.innerText = "";

    try {

        const response = await fetch("/api/generate", {

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

        message.style.color = "green";
        message.textContent = "운동 루틴 생성이 완료되었습니다!";

        // AI 응답 텍스트 화면 출력
        const routineText = result.routine || result.result;
        resultContainer.innerText = routineText;
        resultContainer.style.display = "block"; // 결과창 노출

    } catch (error) {

        console.error(error);

        message.style.color = "red";
        message.textContent = "서버와 통신 중 오류가 발생했습니다.";

    }

});