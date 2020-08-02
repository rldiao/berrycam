const captureBtn = document.getElementById('captureBtn')
const previewBtn = document.getElementById('previewBtn')

function captureBtnClick() {
    // Get value on button click and show alert

    let capture = $.ajax('/api/camera/capture', {
        type: 'GET'
    })

    capture.done((data) => {
        console.log(JSON.stringify(data))
    })
}

function previewBtnClick() {
    // Get value on button click and show alert

    let capture = $.ajax('/api/camera/toggle_preview', {
        type: 'GET'
    })

    capture.done((data) => {
        console.log(JSON.stringify(data))
    })
}

function main() {
    captureBtn.addEventListener('click', captureBtnClick)
    previewBtn.addEventListener('click', previewBtnClick)
}

main()
