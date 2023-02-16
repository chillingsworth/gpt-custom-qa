import { useReducer } from 'react';
import styles from '../styles/Home.module.css'
import Feed from '../components/feed'

function reducer(state, action) {
  console.log(state)
  return {
    ...state,
    [action.q]: action.a
  };
}

export default function Search() {

  const [state, dispatch] = useReducer(reducer, {});

  function handleSubmit(e) {

    e.preventDefault();

    const question = e.target.search.value
    const qurl = "http://localhost:5004/"

    fetch(qurl, {
    method: 'POST',   
    mode: 'cors',
    headers: {
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Origin': 'http://localhost'
    },
    body: JSON.stringify({'text': question})})
    .then(response => response.json())
    .then(json => window.alert(json.response))
    
  }

  function handleChange(e) {
    // alert('A name was changed: ' + e.nativeEvent.data);
    e.preventDefault();
  }

  return (
    <div className={styles.searchcontainer}>
      <form display={'flex'} onSubmit={(e) => handleSubmit(e)}>
        <div className={styles.search}>
          <input className={styles.searchitem} type="text" name="search" defaultValue="Just Ask..." 
            onChange={handleChange} onClick={(e) => {e.currentTarget.value = ""}}/>
          <input className={styles.searchbutton} type="submit" name="submit" value="Search"/>
        </div>
      </form>
    </div>
  );
}