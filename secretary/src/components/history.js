import  {useState} from 'react';

const History = () => {
  // State to hold the list of text pairs
  const [history, setHistory] = useState([]); 

  // Method to add a new text pair to the list
  const addRecord = (question, response) => {
    setHistory([...history, { 'question': question, 'response': response, 'timestamp': new Date().toLocaleString() }]);
  };

  // Method to read the list of text pairs
  const getFullHistory = () => {
    return history;
  };

  const isEmpty = () => {
    return history.length === 0;
  };

  // Return null as this component is only for holding data
  return {history, addRecord, getFullHistory, isEmpty};
};

export default History;