import React, { Fragment } from 'react'
import PropTypes from 'prop-types'
import { Slider, Typography, FormControl } from '@material-ui/core'

function Exposure(props) {
  return (
    <Fragment>
      <Typography>Exposure</Typography>
      <Typography id="shutterspeed-slider" gutterBottom>
        Shutter Speed
                </Typography>
      <Slider
        defaultValue={30}
        aria-labelledby="shutterspeed-slider"
        valueLabelDisplay="auto"
        step={10}
        marks
        min={10}
        max={110}
      />
      <Typography id="iso-slider" gutterBottom>
        ISO
                </Typography>
      <Slider
        defaultValue={30}
        aria-labelledby="iso-slider"
        valueLabelDisplay="auto"
        step={10}
        marks
        min={10}
        max={110}
      />
      <FormControl>
        {/* <OptionSelector
            id="awb"
            label="AWB"
            labelId="awb-label"
            name="awb_mode"
            options={this.state.AWB_MODES}
            value={this.state.awb_mode}
            onChange={this.handleSettingsChange}
          /> */}
      </FormControl>
    </Fragment>
  )
}

Exposure.propTypes = {

}

export default Exposure

