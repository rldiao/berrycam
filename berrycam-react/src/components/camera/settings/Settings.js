import React, { Component } from 'react'
import Grid from '@material-ui/core/Grid'
import Exposure from './Exposure'
import WhiteBalance from './WhiteBalance'
import Axios from 'axios'

export default class Settings extends Component {
  state = {
    "awb_modes": [],
    "awb_mode": "",
    "exposure_modes": [],
    "exposure_mode": ""
  }

  componentDidMount() {
    Axios.get("/api/camera/settings/options")
      .then(res => {
        this.setState(res.data)
      })
      .catch(e => {
        console.log(e)
      })
    
    Axios.get("/api/camera/settings")
      .then(res => {
        this.setState(res.data)
      })
      .catch(e => {
        console.log(e)
      })
  }

  handleSettingsChange(event) {
    const setting = event.target.name
    const value = event.target.value

    this.setState({ [setting]: value })
    Axios.post("/api/camera/settings", {
      [setting]: value
    }).catch(e => {
      console.log(e)
    })
  }
  handleSettingsChange = this.handleSettingsChange.bind(this)


  render() {
    return (
      <Grid container spacing={2}>
        <Grid item xs={12}>
          <Exposure
            exposureMode={this.state.exposure_mode}
            exposureOptions={this.state.exposure_modes}
            onChange={this.handleSettingsChange}
          />
        </Grid>
        <Grid item xs={12}>
          <WhiteBalance
            awbMode={this.state.awb_mode}
            awbOptions={this.state.awb_modes}
            onChange={this.handleSettingsChange}
          />
        </Grid>
      </Grid>
    )
  }
}
