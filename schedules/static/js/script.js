// 일정 수정 모달

$('#updateModal').on('show.bs.modal', function (event) {
  var button = event.relatedTarget
  const schedule_pk = button.dataset.scheduleId
  const workspace_pk = button.dataset.workspaceId
  const schedule_title = button.dataset.scheduleTitle
  const schedule_content= button.dataset.scheduleContent
  const schedule_priority = button.dataset.schedulePriority
  const schedule_start_date = button.dataset.scheduleStartDate
  const schedule_end_date = button.dataset.scheduleEndDate
  const schedule_start_time = button.dataset.scheduleStartTime
  const schedule_end_time = button.dataset.scheduleEndTime

  const radioId = `id_priority_${schedule_priority - 1}`
  document.querySelector(`#updateModal #${radioId}`).checked=true

  var modal = $(this)
  modal.find('.my-schedule-title').val(schedule_title)
  modal.find('.my-schedule-content').val(schedule_content)
  modal.find('.my-schedule-start_date').val(schedule_start_date)
  modal.find('.my-schedule-end_date').val(schedule_end_date)
  modal.find('.my-schedule-start_time').val(schedule_start_time)
  modal.find('.my-schedule-end_time').val(schedule_end_time)

  const updateForm = document.querySelector('#schedules_updateForm')
  updateForm.action = `/schedules/workspace/${workspace_pk}/schedule/${schedule_pk}/update/`

  const deleteForm = document.querySelector('#schedules_deleteForm')
  deleteForm.action = `/schedules/workspace/${workspace_pk}/schedule/${schedule_pk}/delete/`

  const updatemodalP = document.querySelectorAll('#updateModal p')
  const priorityp = document.querySelector('#updateModal ul')


  updatemodalP[0].setAttribute('class','schedule-title-p')
  updatemodalP[1].setAttribute('class','schedule-content-p')
  updatemodalP[4].setAttribute('class','schedule-start_date-p')
  updatemodalP[5].setAttribute('class','schedule-end_date-p')
  updatemodalP[6].setAttribute('class','schedule-start_time-p')
  updatemodalP[7].setAttribute('class','schedule-end_time-p')
  priorityp.setAttribute('class','schedule-priority-p')

})


// 이전달 달력 버튼

const leftArrow = document.querySelector('.schedules_left-arrow')
const rightArrow = document.querySelector('.schedules_right-arrow')
leftArrow.addEventListener('click', (e) => {
  e.preventDefault()
  const workspace_pk = leftArrow.dataset.workspaceId
  const scheduleNowYear = leftArrow.dataset.year
  const scheduleNowMonth = leftArrow.dataset.month

  requestUrl = `/schedules/workspace/${workspace_pk}/left_month/?month=${scheduleNowYear}-${scheduleNowMonth}`
  console.log(requestUrl)

  axios.get(requestUrl)
    .then(res => {
      const nowYear = document.querySelector('.schedule_now_year')
      const nowMonth = document.querySelector('.schedule_now_month')
      const nowCalendar = document.querySelector('.schedules_main')
      nowYear.innerText = `${res.data.left_year}년`
      nowMonth.innerText = `${res.data.left_month}월`
      leftArrow.dataset.year = res.data.left_year
      leftArrow.dataset.month = res.data.left_month
      rightArrow.dataset.year = res.data.left_year
      rightArrow.dataset.month = res.data.left_month
      nowCalendar.innerHTML = res.data.calendar
    })
    .catch(err => {
      console.log(err)
    })
  }
)


// 다음달 달력 버튼
rightArrow.addEventListener('click', (e) => {
  e.preventDefault()
  const workspace_pk = rightArrow.dataset.workspaceId
  const scheduleNowYear = rightArrow.dataset.year
  const scheduleNowMonth = rightArrow.dataset.month

  requestUrl = `/schedules/workspace/${workspace_pk}/right_month/?month=${scheduleNowYear}-${scheduleNowMonth}`
  console.log(requestUrl)

  axios.get(requestUrl)
    .then(res => {
      const nowYear = document.querySelector('.schedule_now_year')
      const nowMonth = document.querySelector('.schedule_now_month')
      const nowCalendar = document.querySelector('.schedules_main')
      nowYear.innerText = `${res.data.right_year}년`
      nowMonth.innerText = `${res.data.right_month}월`
      leftArrow.dataset.year = res.data.right_year
      leftArrow.dataset.month = res.data.right_month
      rightArrow.dataset.year = res.data.right_year
      rightArrow.dataset.month = res.data.right_month
      nowCalendar.innerHTML = res.data.calendar
    })
    .catch(err => {
      console.log(err)
    })
  }
)