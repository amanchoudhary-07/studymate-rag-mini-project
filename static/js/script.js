async function askQuestion() {
    const question = document.getElementById("question").value;
    const answerDiv = document.getElementById("answer");

    answerDiv.innerText = "⏳ Thinking...";

    const response = await fetch("/ask", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ question: question })
    });

    const data = await response.json();
    answerDiv.innerText = data.answer;
}
