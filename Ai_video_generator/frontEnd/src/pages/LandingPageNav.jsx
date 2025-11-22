import React from 'react'
import { Link } from 'react-router'
import { useNavigate } from 'react-router'
//@import "tailwindcss"

function LandingPageNav() {

    const navigate = useNavigate();

 return (
    <header className="sticky top-0 z-40 border-b border-slate-200/70 bg-white/80 backdrop-blur">
      <nav className="mx-auto flex h-16 max-w-6xl items-center justify-between px-4 sm:px-6 lg:px-8">
        
        <div className="flex items-center gap-2">
          <div className="flex h-8 w-8 items-center justify-center rounded-full bg-gradient-to-tr from-indigo-500 to-sky-500 text-sm font-semibold text-white">
            M
          </div>
          <span className="text-lg font-semibold tracking-tight text-slate-900">
            MotionLanding
          </span>
        </div>

        
        <div className="flex items-center gap-3">
          <button 
          onClick = {() => navigate("/main")}
          className="rounded-full border border-slate-300 px-4 py-1.5 text-sm font-medium text-slate-700 hover:border-slate-400 hover:bg-slate-50">
            Log in
          </button>
          <button 
          onClick = {() => navigate("/main")}
          className="rounded-full bg-slate-900 px-4 py-1.5 text-sm font-medium text-white shadow-sm hover:bg-slate-800">
            Sign up
          </button>
        </div>
      </nav>
    </header>
  )
}

export default LandingPageNav

//Old navbar
/**
 return (
    <header className="sticky top-0 z-40 border-b border-slate-200/70 bg-white/80 backdrop-blur">
      <nav className="mx-auto flex h-16 max-w-6xl items-center justify-between px-4 sm:px-6 lg:px-8">
        
        <div className="flex items-center gap-2">
          <div className="flex h-8 w-8 items-center justify-center rounded-full bg-gradient-to-tr from-indigo-500 to-sky-500 text-sm font-semibold text-white">
            M
          </div>
          <span className="text-lg font-semibold tracking-tight text-slate-900">
            MotionLanding
          </span>
        </div>

        
        <div className="flex items-center gap-3">
          <button className="rounded-full border border-slate-300 px-4 py-1.5 text-sm font-medium text-slate-700 hover:border-slate-400 hover:bg-slate-50">
            Log in
          </button>
          <button className="rounded-full bg-slate-900 px-4 py-1.5 text-sm font-medium text-white shadow-sm hover:bg-slate-800">
            Sign up
          </button>
        </div>
      </nav>
    </header>
  )
  
 */