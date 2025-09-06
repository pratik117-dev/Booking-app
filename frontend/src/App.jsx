import { useContext, useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Navbar from './components/Navbar'
import { Outlet } from 'react-router-dom'
import { UserContext } from './components/UserContext'
import TextType from './components/TextType'

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
    <button>

    <TextType 
  text={["Text typing effect", "for your websites", "Happy coding!"]}
  typingSpeed={75}
  pauseDuration={1500}
  showCursor={true}
  cursorCharacter="|"
  />
  </button>
    <Outlet></Outlet>
    
    </>
  )

  }

export default App
