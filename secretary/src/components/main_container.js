
import { styled } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid2';
import Container from '@mui/material/Container';

import History from './history';
import QueryPrompt from './query_promp';
import TimeLine from './timeline';

const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: '#f0f1e8',
  ...theme.typography.body2,
  padding: theme.spacing(1),
  // textAlign: 'center',
  color: theme.palette.text.secondary,
  ...theme.applyStyles('dark', {
    backgroundColor: '#f0f1e8',
  }),
}));


const buildHistory = () => {
  return (
    <History />
  )
}

const MainContainer = () => {
  const hty =  History();

  return (
    <Container maxWidth="md" className='main_container'>
      <Box sx={{ flexGrow: 1 }}>
        <Grid container spacing={1}>
          <Grid size={12} className="header grid_block">
            <Item >
              <Box sx={{textAlign: 'right'}}>
                <img  src={`/images/banner_main_logo.png`} alt="Logo" height='40px'/>
              </Box>
              <Box maxWidth="lg">
                <QueryPrompt  history={hty} />
              </Box>
            </Item>
          </Grid>
          <Grid size={12}>
            <Item>
              <TimeLine history={hty} />
            </Item>
          </Grid>

        </Grid>
      </Box>
    </Container>
  );
};


export default MainContainer;