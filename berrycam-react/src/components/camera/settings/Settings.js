import React, { Component } from 'react'
import Grid from '@material-ui/core/Grid'
import Exposure from './Exposure'
import WhiteBalance from './WhiteBalance'
import Axios from 'axios'

export default class Settings extends Component {
  state = {
    "AWB_MODES": [],
    "awb_mode": ""
  }

  componentDidMount() {
    Axios.get("/api/camera/settings/options")
      .then(res => {
        this.setState({"AWB_MODES": res.data.awb_modes})
      })
      .catch(e => {
        console.log(e)
      })
    
    Axios.get("/api/camera/settings")
      .then(res => {
        this.setState({"awb_mode": res.data.awb_mode})
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
          <Exposure></Exposure>
        </Grid>
        <Grid item xs={12}>
          <WhiteBalance
            options={this.state.AWB_MODES}
            onChange={this.handleSettingsChange}
            awbMode={this.state.awb_mode}
          />
        </Grid>
      </Grid>
    )
  }
}
