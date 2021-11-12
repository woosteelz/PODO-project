// 모달로 게시글 생성
const myBtn = document.querySelectorAll('.myBtn')
    console.log(myBtn)
    myBtn.forEach((btn) => {
      btn.addEventListener('click', (e)=> {
        const boardPk = btn.dataset.boardPk
        console.log(boardPk)

        const form = document.querySelector('.container-form')
        form.addEventListener('submit', (e) => {
          e.preventDefault()

          const workspacePk = e.target.dataset.workspacePk
          const categoryPk = e.target.dataset.categoryPk
          e.target.action = `/articles/${workspacePk}/workspace/${categoryPk}/category/${boardPk}/board/create_article/`
          e.target.submit()
        })
      })
    })


// 보드 드롭 앤 다운
const articles = document.querySelectorAll(".article")
const all_status = document.querySelectorAll(".board-status")
let movedArticlePk = null
let movedBoardPk = null
let draggableArticle = null

articles.forEach((article) => {
  article.addEventListener("dragstart", dragStart)
  article.addEventListener("dragend", dragEnd)
});

function dragStart(e) {
  draggableArticle = this
  setTimeout(() => {
    this.style.display = "none"
  }, 0)
  // console.log("dragStart")
  movedArticlePk = e.target.dataset.articlePk
}

function dragEnd() {
  draggableArticle = null
  setTimeout(() => {
    this.style.display = "block"
  }, 0)
  // console.log("dragEnd")
  // console.log(e.target.dataset.articlePk)
}

function dragOver(e) {
  e.preventDefault()
}

function dragEnter() {
  this.style.border = "1px dashed #ccc"
  // console.log("dragEnter")
}

function dragLeave() {
  this.style.border = "none"
  // console.log("dragLeave")
}

function dragDrop(e) {
  this.style.border = "none"
  this.appendChild(draggableArticle)
  // console.log("dropped")
  // console.log(e.target.dataset.boardPk)
  movedBoardPk = e.target.dataset.boardPk
  // console.log(movedArticlePk)
  // console.log(movedBoardPk)

  const modifyUrl = `/articles/${movedArticlePk}/${movedBoardPk}/modify_article_board/`
  console.log(draggableArticle)
  console.log(modifyUrl)
  axios.get(modifyUrl)
    .then(res =>{
      setTimeout(function(){
        location.reload();
      },10);
    })
    .catch(err => {
      alert(err)
    })
}

all_status.forEach((status) => {
  status.addEventListener("dragover", dragOver)
  status.addEventListener("dragenter", dragEnter)
  status.addEventListener("dragleave", dragLeave)
  status.addEventListener("drop", dragDrop)
})