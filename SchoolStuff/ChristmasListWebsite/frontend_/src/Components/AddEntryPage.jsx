import React,{useState} from 'react'
import axios from 'axios'

export function AddEntryPage(){
    const [values,setState] = useState({
    name:"",
    itemName:"",
    itemPrice:0.0,
    itemLink:""
    });

  const handleChange = event => {
    setState({...values,[event.target.name]:event.target.value})
    //console.log(event.target.value)
  }
  const ResetInput = () =>{
    document.getElementById("name").value = "";
    document.getElementById("itemName").value = "";
    document.getElementById("itemPrice").value = "";
    document.getElementById("itemLink").value = "";
  }
  const handleSubmit = event =>{
    event.preventDefault();
    
    const input = {
      name:values.name,
      itemName:values.itemName,
      itemPrice:values.itemPrice,
      itemLink:values.itemLink
    };
    console.log(input)
    axios.post('http://localhost:8000/list/addEntry',input).then(res=>
      console.log(res)).catch(err =>
      console.log(err));
  }
    return (
    <div className="vh-100 bg-secondary text-center">
      <form onSubmit={handleSubmit}>
        <label htmlFor="NameInput" className="form-label fw-bold text-capitalize fs-4">Name</label>
        <div className="d-flex justify-content-center">
          <input name='name' type="name" className="form-control w-25" id="name" placeholder="Name" onChange={handleChange}></input>
        </div>

        <label htmlFor="ItemNameInput" className="form-label fw-bold text-capitalize fs-4">Item Name</label>
        <div className="d-flex justify-content-center">
          <input name='itemName' type="name" className="form-control w-25" id="itemName" placeholder="Item Name" onChange={handleChange}></input>
        </div>

        <label htmlFor="ItemPriceInput" className="form-label fw-bold text-capitalize fs-4">Item Price</label>
        <div className="d-flex justify-content-center">
          <input name='itemPrice' type="name" className="form-control w-25" id="itemPrice" placeholder="Item Price" onChange={handleChange}></input>
        </div>

        <label htmlFor="ItemLinkInput" className="form-label fw-bold text-capitalize fs-4">Item Link</label>
        <div className="d-flex justify-content-center">
          <input name='itemLink' type="name" className="form-control w-25" id="itemLink" placeholder="Item Link" onChange={handleChange}></input>
        </div>
        <div className="d-flex justify-content-center">
        <button type="submit" className="btn btn-primary mt-2" onClick={ResetInput}>Add Item</button>
        </div>
      </form>  
    </div>
  )
  
}
export default AddEntryPage
