import React, { Component } from 'react'

import Button from '@material-ui/core/Button'

const axios = require('axios')


export default class ControlBar extends Component {
  constructor(props) {
    super(props)

    this.handleCaptureClick = this.handleCaptureClick.bind(this)
    this.handPreviewClick = this.handPreviewClick.bind(this)
  }

  handleCaptureClick() {
    axios.get('/api/camera/capture')
      .then(res => {
        console.log(res.data)
      })
      .catch(err => {
        console.log(err)
      })
  }

  handPreviewClick() {
    axios.get('/api/camera/toggle_preview')
      .then(res => {
        console.log(res.data)
      })
      .catch(err => {
        console.log(err)
      })
  }

  render() {
    return (
      <div>
        <Button onClick={this.handleCaptureClick} variant="contained">Capture</Button>
        <Button onClick={this.handPreviewClick} variant="contained">Preview</Button>
      </div>
    )
  }
}
