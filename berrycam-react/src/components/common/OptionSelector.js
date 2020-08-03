import React, { Fragment } from 'react'
import PropTypes from 'prop-types'
import InputLabel from "@material-ui/core/InputLabel";
import MenuItem from "@material-ui/core/MenuItem";
import Select from "@material-ui/core/Select";

function OptionSelector(props) {
  const options_menu = props.options.map((mode) => {
    return <MenuItem key={mode} value={mode}>{mode}</MenuItem>
  })

  return (
    <Fragment>
      <InputLabel shrink id={props.labelId}>{props.label}</InputLabel>
      <Select
        labelId={props.labelId}
        id={props.id}
        onChange={props.onChange}
        name={props.name}
        displayEmpty
        value={props.value}
      >
        {options_menu}
      </Select>
    </Fragment>
  )
}

OptionSelector.propTypes = {
  id: PropTypes.string,
  labelId: PropTypes.string,
  name: PropTypes.string.isRequired,
  value: PropTypes.any.isRequired,
  onChange: PropTypes.func.isRequired,
  options: PropTypes.array.isRequired
}

export default OptionSelector

