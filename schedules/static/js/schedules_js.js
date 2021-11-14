// 일정 수정 모달
var workspace_pk = ''
var schedule_pk = ''

$('#updateModal').on('show.bs.modal', function (event) {
  var button = event.relatedTarget
  schedule_pk = button.dataset.bsScheduleId
  workspace_pk = button.dataset.bsWorkspaceId
  console.log(button.dataset)
  const schedule_title = button.dataset.bsScheduleTitle
  const schedule_content= button.dataset.bsScheduleContent
  const schedule_priority = button.dataset.bsSchedulePriority
  const schedule_start_date = button.dataset.bsScheduleStartDate
  const schedule_end_date = button.dataset.bsScheduleEndDate
  const schedule_start_time = button.dataset.bsScheduleStartTime
  const schedule_end_time = button.dataset.bsScheduleEndTime
  const radioId = `id_priority_${schedule_priority - 1}`
  document.querySelector(`#updateModal #${radioId}`).checked=true

  var modal = $(this)
  modal.find('.schedules_update_modal_form .my-schedule-title').val(schedule_title)
  modal.find('.schedules_update_modal_form .my-schedule-content').val(schedule_content)
  modal.find('.schedules_update_modal_form .my-schedule-start_date').val(schedule_start_date)
  modal.find('.schedules_update_modal_form .my-schedule-end_date').val(schedule_end_date)
  modal.find('.schedules_update_modal_form .my-schedule-start_time').val(schedule_start_time)
  modal.find('.schedules_update_modal_form .my-schedule-end_time').val(schedule_end_time)

  document.querySelector('.schedules_update_modal_form').action = `/schedules/workspace/${workspace_pk}/schedule/${schedule_pk}/update/`
})


// 일정 삭제 모달
$('#deleteModal').on('show.bs.modal', function (event) {
  console.log(workspace_pk, schedule_pk)
  document.querySelector('.schedules_delete_modal_form').action = `/schedules/workspace/${workspace_pk}/schedule/${schedule_pk}/delete/`
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