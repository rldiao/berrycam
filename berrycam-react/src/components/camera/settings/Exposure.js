import React, { Fragment } from 'react'
import PropTypes from 'prop-types'
import { Slider, Typography, FormControl } from '@material-ui/core'
// import OptionSelector from '../../common/OptionSelector'

function Exposure(props) {
  return (
    <Fragment>
      {/* <Typography>Exposure</Typography>
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
      /> */}
      {/* <FormControl>
        <OptionSelector
            id="metermode-optionselector"
            label="Mode Mode"
            labelId="metermode-label"
            name="meter_mode"
            options={props.meterOptions}
            value={props.meterValue}
            onChange={this.onChange}
          />
      </FormControl> */}
    </Fragment>
  )
}

Exposure.propTypes = {
  meterOptions: PropTypes.array.isRequired
}

export default Exposure

