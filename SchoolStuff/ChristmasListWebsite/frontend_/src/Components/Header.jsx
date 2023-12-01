import React from 'react'

function Header() {

    return (
    <div className='container-fluid border border-2 border-dark rounded-bottom shadow'>
        <div className="row bg-primary text-black">
            <div className="col-md-4 mt-4">
                <a className="me-2 text-black fs-5"href='/'>Home</a>
                <a className="mx-2 text-black fs-5" href='/addEntry'>Add Entry</a>
                <a className="mx-2 text-black fs-5" href='/listView'>View List</a>
            </div>
            <div className="col-md-5">
                <h1>Friends and Family Wishlist Website</h1>
            </div>
        </div>
    </div>
  )
}
export default Header
