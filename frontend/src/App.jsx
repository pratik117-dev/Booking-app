import { useContext, useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Navbar from './components/Navbar'
import { Outlet } from 'react-router-dom'
import { UserContext } from './components/UserContext'

function App() {

  const {user, setUser} = useContext(UserContext)
  const{loading, setLoading} = useState(true)

  useEffect(()=>{

    const storedUser = localStorage.getItem('user')
    if(storedUser){
      setUser(JSON.parse(storedUser));
    }
    else{
      setUser(null);
    }

  },[]);

  if(loading){
    return <div>loading ......</div>
  }

  return(
    <>
    <Navbar></Navbar>
    <Outlet></Outlet>
    
    </>
  )

  }

export default App
