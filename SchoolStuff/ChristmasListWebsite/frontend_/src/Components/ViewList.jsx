import React,{useEffect,useState} from 'react'
import axios from 'axios'

export function ViewList(){
  const[dataResponse,setDataResponse] = useState([]);
  //const[selected,setSelected] = useState(0);

  useEffect(() =>{
    async function getData(){
        const response = await fetch('http://localhost:8000/list');
        const res = await response.json();
        console.log(res.results)
        setDataResponse(res.results)
    }
    getData();
  },[])

  const handleSubmit = event =>{
    event.preventDefault();
    var e = document.getElementById("select");
    var num = e.value;
    console.log(num)
    axios.post('http://localhost:8000/list/removeEntry',{num}).then(res=>
      console.log(res)).catch(err =>
      console.log(err));
      window.location.reload();
  }
  
  var listItems = dataResponse.map((item) =>
    <li key={item.num} className='list-group-item text-capitalize fs-6 fw-bold p-1'>
      {item.name}: {item.itemName}, Price: ${item.itemPrice}, Link: <a href={item.itemLink} target='_blank' rel='noreferrer'>Link To Item</a>
    </li>
  )
  var selectableList = dataResponse.map((item)=>
    <option key={item.num} value={item.num}>{item.name}: {item.itemName}</option>
  )
  return (
  <div className="vh-100 bg-secondary text-center">
    <div className="d-flex justify-content-center">
      <ul className='list-group w-50 text-capitalize fw-bold mt-2'>{listItems}</ul>
      </div>
    <div className="d-flex justify-content-center">
      <select className='form-select mt-2 w-25' aria-label='Default select example' id='select'>
      <option value={-1}>Select Entry To Remove</option>
      {selectableList}
      </select>
      </div>
      <button type="submit" className="btn btn-primary mt-2" onClick={handleSubmit}>Remove Selected Item</button>
  </div>
  )
}
export default ViewList
