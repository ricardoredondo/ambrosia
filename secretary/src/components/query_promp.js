
import * as React from 'react';
import { useState } from 'react';
import TextField from '@mui/material/TextField';
import Article from '@mui/icons-material/Article';
import InputAdornment from '@mui/material/InputAdornment';


const QueryPrompt = (props) => {
  const [inputValue, setInputValue] = useState('');

  const handleKeyPress = (event) => {
    if (event.key === 'Enter') {
      const trimmedValue = inputValue.trim();
      if (trimmedValue === '') {
        return;
      }
      
      props.history.addRecord("inputValue inputValue inputValue inputValue inputValue inputValue inputValue inputValue inputValue inputValue inputValue inputValue inputValue inputValue inputValue inputValue inputValue inputValue inputValue inputValue inputValue inputValue inputValue inputValue inputValue inputValue inputValue inputValue inputValue inputValue inputValue inputValue inputValue inputValue inputValue inputValue inputValue inputValue inputValue inputValue ", 'respuesta respuesta respuesta respuesta respuesta respuesta respuesta respuesta respuesta respuesta respuesta respuesta respuesta respuesta respuesta respuesta respuesta respuesta respuesta respuesta respuesta respuesta respuesta respuesta respuesta respuesta respuesta respuesta respuesta respuesta respuesta respuesta respuesta respuesta respuesta respuesta respuesta respuesta respuesta respuesta respuesta respuesta ');
      setInputValue('');
    }
  };

  return (
    <TextField
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
  );
};

export default QueryPrompt