import * as React from 'react';
import Box from '@mui/material/Box';
import HideSource from '@mui/icons-material/HideSource';
import History from '@mui/icons-material/History';
import Divider from '@mui/material/Divider';
import Message from '@mui/icons-material/Message';
import ModeComment from '@mui/icons-material/ModeComment';
import Grid from '@mui/material/Grid2';


const TimeLine = (props) => {
  console.log(props);
  return (
    <Box sx={{ textAlign: 'left' }}>
      {props.history.isEmpty() ? (
        <>
          <Box  sx={{ textAlign: 'center' }}>
            <h2><HideSource /> Historial de consultas esta vacío</h2>
          </Box>
        </>
      ) : (
        <>
          <Box sx={{ textAlign: 'center' }}>
            <h2><History /> Historial de consultas </h2>
            {props.history.getFullHistory().reverse().map((item, index) => (
              <div key={index}>
                <Box sx={{ flexGrow: 1 }}>
                  <div style={{ textAlign: 'right', 'font-style': 'italic' }}  >{item['timestamp']}</div>
                  <Grid container spacing={0}>
                    <Grid size={1} className="header grid_block">
                      <Message/>
                    </Grid>
                    <Grid size={11} className="header grid_block" sx={{ textAlign: 'left' }}>
                      {item['question']}
                    </Grid>
                  </Grid>
                  <br />
                  <Grid container spacing={0}>
                    <Grid size={11} className="header grid_block" sx={{ textAlign: 'right', 'font-style': 'italic' }}>
                      {item['response']}
                    </Grid>
                    <Grid size={1} className="header grid_block">
                      <ModeComment/>
                    </Grid>
                  </Grid>
                </Box>
                <br />
                <Divider />
              </div>
            ))}
          </Box>
        </>
      )}
    </Box>
  );
};


export default TimeLine