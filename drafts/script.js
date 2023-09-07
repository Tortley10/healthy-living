const startButton = document.getElementById('start-btn')
const nextButton = document.getElementById('next-btn')
const questionContainerElement = document.getElementById('question-container')
const questionElement = document.getElementById('question')
const answerButtonsElement = document.getElementById('answer-buttons')
const pointsElement = document.getElementById('points')

var points = 0
let shuffledQuestions, currentQuestionIndex

startButton.addEventListener('click', startGame)
nextButton.addEventListener('click', () => {
  currentQuestionIndex++
  setNextQuestion()
})

function startGame() {
  startButton.classList.add('hide')
  shuffledQuestions = questions.sort(() => Math.random() - .5)
  currentQuestionIndex = 0
  questionContainerElement.classList.remove('hide')
  starttitle.classList.add('hide')
  setNextQuestion()
}

function setNextQuestion() {
  resetState()
  showQuestion(shuffledQuestions[currentQuestionIndex])
}

function showQuestion(question) {
  questionElement.innerText = question.question
  question.answers.forEach(answer => {
    const button = document.createElement('button')
    button.innerText = answer.text
    button.classList.add('btn')
    if (answer.correct) {
      button.dataset.correct = answer.correct
      points = points + 1
      pointsElement.innerText = points
    }
    button.addEventListener('click', selectAnswer)
    answerButtonsElement.appendChild(button)
  })
}

function resetState() {
  clearStatusClass(document.body)
  nextButton.classList.add('hide')
  while (answerButtonsElement.firstChild) {
    answerButtonsElement.removeChild(answerButtonsElement.firstChild)
  }
}

function selectAnswer(e) {
  const selectedButton = e.target
  const correct = selectedButton.dataset.correct
  setStatusClass(document.body, correct)
  Array.from(answerButtonsElement.children).forEach(button => {
    setStatusClass(button, button.dataset.correct)
  })
  if (shuffledQuestions.length > currentQuestionIndex + 1) {
    nextButton.classList.remove('hide')
  } else {
    startButton.innerText = 'Restart'
    startButton.classList.remove('hide')
  }
}

function setStatusClass(element, correct) {
  clearStatusClass(element)
  if (correct) {
    element.classList.add('correct')
  } else {
    element.classList.add('wrong')
  }
}

function clearStatusClass(element) {
  element.classList.remove('correct')
  element.classList.remove('wrong')
}

const questions = [
  {
    question: 'How much water should a male adult drink per day?',
    answers: [
      { text: '3.7 Litres', correct: true },
      { text: '2.7 Litres', correct: false },
      { text: '4.0 Litres', correct: false },
      { text: '3.0 Litres', correct: false }
    ]
  },
  {
    question: 'What is the recommended amount of excercise for the average adult?',
    answers: [
      { text: '150 minutes of moderate aerobic activity a week', correct: true },
      { text: '75 minutes of moderate aerobic activity a week', correct: false },
      { text: '250 minutes of moderate aerobic activity a week', correct: false },
      { text: '100 minutes of moderate aerobic activity a week', correct: false }
    ]
  },
  {
    question: 'What is the recommended daily Calcium intake for adults?',
    answers: [
      { text: '500 mg', correct: false },
      { text: '800 mg', correct: true },
      { text: '100 mg', correct: false },
      { text: '600 mg', correct: false }
    ]
  },
  {
    question: 'What is a healthy BMI for adults 20 years old and older?',
    answers: [
      { text: '21.4 - 25.9', correct: false },
      { text: '18.5 – 24.9', correct: true },
      { text: '17.6 - 23.8', correct: false },
      { text: '18.5 - 26.7', correct: false }
    ]
  },
  {
    question: 'Which of the following food items are rich in protein?',
    answers: [
      { text: 'White Rice', correct: false },
      { text: 'Brocolli', correct: false },
      { text: 'Eggs', correct: true },
      { text: 'Ice Cream', correct: false }
    ]
  }
]