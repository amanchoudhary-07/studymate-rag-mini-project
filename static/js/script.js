let lastQuestion = "";
let lastAnswer = "";
let helpful = null;

async function askQuestion() {
  const q = document.getElementById("question").value.trim();
  if (!q) return;

resetFeedbackUI();


  document.getElementById("loader").classList.remove("hidden");
  document.getElementById("answer-card").classList.add("hidden");
  document.getElementById("feedback-box").classList.add("hidden");

  const res = await fetch("/ask", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question: q })
  });

  const data = await res.json();

  document.getElementById("loader").classList.add("hidden");
  showAnswer(data.answer, q);
}

function showAnswer(answer, question) {
  document.getElementById("answer").innerText = answer;
  document.getElementById("answer-card").classList.remove("hidden");
  document.getElementById("feedback-box").classList.remove("hidden");

  lastQuestion = question;
  lastAnswer = answer;
}


function resetFeedbackUI() {
  helpful = null;

  // 👍 👎 button reset
  document.getElementById("yesBtn")?.classList.remove("active");
  document.getElementById("noBtn")?.classList.remove("active");

  // ⭐ rating reset
  const rating = document.getElementById("rating");
  if (rating) rating.value = "5";

  // feedback message clear
  const msg = document.getElementById("feedback-msg");
  if (msg) msg.innerText = "";
}





function setHelpful(val) {
  helpful = val;
  document.getElementById("yesBtn").classList.toggle("active", val);
  document.getElementById("noBtn").classList.toggle("active", !val);
}

function submitFeedback() {
  if (helpful === null) return alert("Please select 👍 or 👎");

  const rating = document.getElementById("rating").value;

  fetch("/feedback", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      question: lastQuestion,
      answer: lastAnswer,
      helpful,
      rating
    })
  });

  document.getElementById("feedback-msg").innerText =
    "✅ Feedback saved!";
}


