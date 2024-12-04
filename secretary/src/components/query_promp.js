
import * as React from 'react';
import { useState } from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Article from '@mui/icons-material/Article';
import InputAdornment from '@mui/material/InputAdornment';
import LinearProgress from '@mui/material/LinearProgress';
import Computer from '@mui/icons-material/Computer';
import ApiHook from './api_hook';
import ReactMarkdown from 'react-markdown';



const QueryPrompt = (props) => {
  const [inputValue, setInputValue] = useState('');
  const [outputValue, setOutputValue] = useState('');
  const [loading, setLoading] = useState(false);

  const initRequest = (data) => {
    setLoading(true);
  };
    
  const doneRequest = (data) => {
    console.log("done")
  
    props.history.addRecord(data.question, data.response);
    setInputValue('');
    setOutputValue(data.response);
    setLoading(false); 
  }

  const handleKeyPress = (event) => {
    if (event.key === 'Enter') {
      const trimmedValue = inputValue.trim();
      if (trimmedValue === '') {
        return;
      }
      
      const api =  ApiHook({
        setLoading: setLoading, 
        init: initRequest, 
        done: doneRequest
      });
      
      api.ask(trimmedValue);
      // props.history.addRecord(inputValue, "data.response");
    }
  };

  
  return (
    <Box>
      <TextField
        disabled={loading}
        sx={{width: '100%', backgroundColor: 'white'}}
        id="outlined-multiline-static"
        label="Has tu consulta..."
        placeholder="Preguuuunteme"
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        onKeyDown={handleKeyPress}
        slotProps={{
          input: {
            startAdornment: (
              <InputAdornment position="start">
                <Article />
              </InputAdornment>
            ),
          },
        }}
      />
      {loading && <>
        <LinearProgress />
        Wait for it....... wait for it.....
      </>} 
      
      {outputValue && <>
        <Box sx={{ marginTop: '25px', textAlign: 'left', padding: '15px' }}>
          <Computer sx={{ marginRight: '10px' }} /> 
          <ReactMarkdown>{outputValue}</ReactMarkdown>
        </Box>
      </>}
    </Box>
  );
};

export default QueryPrompt