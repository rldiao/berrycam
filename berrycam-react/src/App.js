import React from 'react';
import Grid from '@material-ui/core/Grid'

import ControlBar from './components/camera/ControlBar'

import styles from './App.module.css'
import Settings from './components/camera/settings/Settings'

function App() {
  return (
    <div className={styles.app}>
      <Grid container spacing={2}>
        <Grid item xs={12}>
          <Settings></Settings>
        </Grid>
        <Grid item xs={12}>
          <ControlBar></ControlBar>
        </Grid>
      </Grid>
    </div>
  );
}

export default App;
