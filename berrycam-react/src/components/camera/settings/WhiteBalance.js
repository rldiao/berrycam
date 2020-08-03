import React, { Fragment } from 'react'
import PropTypes from 'prop-types'
import { FormControl } from "@material-ui/core";
import OptionSelector from '../../common/OptionSelector'

function WhiteBalance(props) {
  return (
    <Fragment>
      <FormControl>
        <OptionSelector
          id="awb"
          label="AWB"
          labelId="awb-label"
          name="awb_mode"
          options={props.options}
          value={props.awbMode}
          onChange={props.onChange}
        />
      </FormControl>
    </Fragment>
  )
}

WhiteBalance.propTypes = {
  options: PropTypes.array.isRequired,
  awbMode: PropTypes.string.isRequired,
  onChange: PropTypes.func.isRequired
}

export default WhiteBalance

