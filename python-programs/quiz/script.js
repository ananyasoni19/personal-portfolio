
const questions = [
    {
      question: "Which language structures a web page?",
      options: ["HTML", "Python", "SQL"],
      answer: 0
    },
    {
      question: "Which function gives the length of a Python list?",
      options: ["size()", "len()", "countall()"],
      answer: 1
    },
    {
      question: "What does CSS control?",
      options: ["Styling", "Hardware", "Data storage"],
      answer: 0
    },
    {
      question: "Which data structure follows FIFO?",
      options: ["Stack", "Queue", "Tree"],
      answer: 1
    },
    {
      question: "Which symbol starts a Python comment?",
      options: ["//", "#", "<!--"],
      answer: 1
    }
  ];
  
  let currentQuestion = 0;
  let score = 0;
  let answered = false;
  
  const questionEl = document.getElementById("question");
  const answersEl = document.getElementById("answers");
  const feedbackEl = document.getElementById("feedback");
  const progressEl = document.getElementById("progress");
  const scoreEl = document.getElementById("score");
  const nextBtn = document.getElementById("next");
  
  function showQuestion() {
    answered = false;
    nextBtn.disabled = true;
    feedbackEl.textContent = "";
    answersEl.innerHTML = "";
  
    if (currentQuestion >= questions.length) {
      questionEl.textContent = "Quiz Completed!";
      progressEl.textContent = "Final Result";
      scoreEl.textContent =
        `Your final score: ${score}/${questions.length}`;
      nextBtn.hidden = true;
      return;
    }
  
    const item = questions[currentQuestion];
    questionEl.textContent = item.question;
    progressEl.textContent =
      `Question ${currentQuestion + 1} of ${questions.length}`;
    scoreEl.textContent = `Score: ${score}`;
  
    item.options.forEach((option, index) => {
      const button = document.createElement("button");
      button.textContent = option;
      button.className = "answer";
      button.onclick = () => checkAnswer(index, button);
      answersEl.appendChild(button);
    });
  }
  
  function checkAnswer(selected, button) {
    if (answered) return;
    answered = true;
  
    const correct = questions[currentQuestion].answer;
  
    [...answersEl.children].forEach((answerButton, index) => {
      answerButton.disabled = true;
      if (index === correct) {
        answerButton.classList.add("correct");
      }
    });
  
    if (selected === correct) {
      score++;
      feedbackEl.textContent = "Correct answer!";
    } else {
      button.classList.add("wrong");
      feedbackEl.textContent = "Incorrect. Check the green answer.";
    }
  
    scoreEl.textContent = `Score: ${score}`;
    nextBtn.disabled = false;
  }
  
  nextBtn.onclick = () => {
    currentQuestion++;
    showQuestion();
  };
  
  showQuestion();
  