// 모달로 게시글 생성
const myBtn = document.querySelectorAll('.myBtn')
    // console.log(myBtn)
    myBtn.forEach((btn) => {
      btn.addEventListener('click', (e)=> {
        const boardPk = btn.dataset.boardPk
        // console.log(boardPk)

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
  // console.log(draggableArticle)
  // console.log(modifyUrl)
  axios.get(modifyUrl)
    .then(res =>{
      setTimeout(function(){
        location.reload();
      }, 0);
    })
}

all_status.forEach((status) => {
  status.addEventListener("dragover", dragOver)
  status.addEventListener("dragenter", dragEnter)
  status.addEventListener("dragleave", dragLeave)
  status.addEventListener("drop", dragDrop)
})

// 각종 삭제
// 게시글 삭제
const deleteArticleBtn = document.querySelector('#delete-article-btn')
deleteArticleBtn.addEventListener('click', () => {
  const articlePk = deleteArticleBtn.dataset.articlePk
  // console.log(articlePk)
    const finalDeleteArticle = document.querySelector('.article_delete_modal_form')
    finalDeleteArticle.addEventListener('submit', (e) => {
      e.preventDefault()

      e.target.action = `/articles/${articlePk}/delete_article/`
      e.target.submit()
    })
})


// window.onload = function() {
//   // 댓글 삭제
//   const deleteCommentBtn = document.querySelector('#delete-comment-btn')
//   deleteCommentBtn.addEventListener('click', () => {
//     const articlePk = deleteCommentBtn.dataset.articlePk
//     const commentPk = deleteCommentBtn.dataset.commentPk
//     console.log(commentPk)
//       const finalDeleteComment = document.querySelector('.comment_delete_modal_form')
//       finalDeleteComment.addEventListener('submit', (e) => {
//         e.preventDefault()
  
//         e.target.action = `/articles/${articlePk}/article/${commentPk}/delete_comment/`
//         e.target.submit()
//       })
//   })
  
  // // 이미지 삭제
  // const deleteImageBtn = document.querySelector('#delete-image-btn')
  // deleteImageBtn.addEventListener('click', () => {
  //   const articlePk = deleteImageBtn.dataset.articlePk
  //   const imagePk = deleteImageBtn.dataset.imagePk
  //   console.log(imagePk)
  //     const finalDeleteImage = document.querySelector('.image_delete_modal_form')
  //     finalDeleteImage.addEventListener('submit', (e) => {
  //       e.preventDefault()
  
  //       e.target.action = `/articles/${articlePk}/article/${imagePk}/delete_image/`
  //       e.target.submit()
  //     })
  // })
  
  // // 파일 삭제
  // const deleteFileBtn = document.querySelector('#delete-file-btn')
  // deleteFileBtn.addEventListener('click', (e) => {
  //   const articlePk = deleteFileBtn.dataset.articlePk
  //   const filePk = deleteFileBtn.dataset.filePk
  //   console.log(articlePk, filePk)
  //   console.log(filePk)
  //     const finalDeleteFile = document.querySelector('.file_delete_modal_form')
  //     finalDeleteFile.addEventListener('submit', (e) => {
  //       e.preventDefault()
  
  //       e.target.action = `/articles/${articlePk}/article/${filePk}/delete_file/`
  //       e.target.submit()
  //     })
  // })