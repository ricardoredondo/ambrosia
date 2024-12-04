import axios from 'axios';

const ApiHook = (props) => {

  const ask = async (question) => {
    const url = `http://jenkins.localtest.me/api/ask?q=${question}`;
    
      props.init({question: question});
      const response =  axios.post(url, new URLSearchParams({ q: question }).toString(), {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      }).then((response) => {
        props.done({question: question, response: response.data.response});
      })
      .catch((error) => {
        console.error("Error: ")
        console.error(error)
      });
  };  

  return {
    ask
  };
};

export default ApiHook;