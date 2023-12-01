import React from 'react'
import Image from '../Images/present.png';

export default function Home() {
  return (
    <div className="vh-100 bg-secondary text-center">
      <img src={Image} alt="Present Box" className="rounded mt-3" height="350"></img>
      <div className="w-75 mx-auto mt-3 bg-white border border-4 border-dark rounded">
      <p className="fw-bold text-capitalize fs-2">Use The Links In the Top left Of the Page to Navigate The Website!</p>
      </div>
    </div>
  )
}
