import React, { Component } from "react"
import FormControl from "@material-ui/core/FormControl"
import OptionSelector from '../common/OptionSelector'
import Axios from "axios"

export default class WhiteBalance extends Component {
  state = {
    "AWB_MODES": [],
    "awb_mode": ""
  }

  handleSettingsChange = this.handleSettingsChange.bind(this)

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

  render() {
    return (
      <div>
        <FormControl>
          <OptionSelector
            id="awb"
            label="AWB"
            labelId="awb-label"
            name="awb_mode"
            options={this.state.AWB_MODES}
            value={this.state.awb_mode}
            onChange={this.handleSettingsChange}
          />
        </FormControl>
      </div>
    )
  }
}
