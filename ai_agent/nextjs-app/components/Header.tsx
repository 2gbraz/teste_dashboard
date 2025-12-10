'use client'

import { Settings, RefreshCw, Wrench, Undo2, User, Bell, HelpCircle } from 'lucide-react'

export default function Header() {
  return (
    <>
      {/* Main Header - Dark Blue */}
      <header className="bg-intapp-dark text-white">
        <div className="container mx-auto px-4">
          <div className="flex items-center justify-between h-14">
            {/* Left: Logo and Admin Portal */}
            <div className="flex items-center gap-4">
              <div className="text-xl font-bold">INTAPP</div>
              <div className="text-intapp-light font-medium">Admin Portal</div>
            </div>

            {/* Center: Navigation Tabs */}
            <nav className="flex items-center gap-1">
              <a href="#" className="px-4 py-2 bg-intapp-light rounded-t text-white font-medium">
                Tool
              </a>
              <a href="#" className="px-4 py-2 hover:bg-intapp-light/20 rounded-t transition-colors">
                Persons
              </a>
              <a href="#" className="px-4 py-2 hover:bg-intapp-light/20 rounded-t transition-colors">
                Roles
              </a>
              <a href="#" className="px-4 py-2 hover:bg-intapp-light/20 rounded-t transition-colors">
                Groups
              </a>
              <a href="#" className="px-4 py-2 hover:bg-intapp-light/20 rounded-t transition-colors">
                Clients
              </a>
              <a href="#" className="px-4 py-2 hover:bg-intapp-light/20 rounded-t transition-colors">
                Matters
              </a>
              <a href="#" className="px-4 py-2 hover:bg-intapp-light/20 rounded-t transition-colors">
                RefData
              </a>
            </nav>

            {/* Right: Icons */}
            <div className="flex items-center gap-3">
              <button className="hover:bg-white/10 p-2 rounded transition-colors">
                <Settings className="w-5 h-5" />
              </button>
              <button className="hover:bg-white/10 p-2 rounded transition-colors">
                <RefreshCw className="w-5 h-5" />
              </button>
              <button className="hover:bg-white/10 p-2 rounded transition-colors">
                <Wrench className="w-5 h-5" />
              </button>
              <button className="hover:bg-white/10 p-2 rounded transition-colors">
                <Undo2 className="w-5 h-5" />
              </button>
              <button className="hover:bg-white/10 p-2 rounded transition-colors">
                <User className="w-5 h-5" />
              </button>
              <button className="hover:bg-white/10 p-2 rounded transition-colors">
                <Bell className="w-5 h-5" />
              </button>
              <div className="w-px h-6 bg-white/30"></div>
              <button className="hover:bg-white/10 p-2 rounded transition-colors">
                <HelpCircle className="w-5 h-5" />
              </button>
              <div className="w-8 h-8 rounded-full bg-white/20 flex items-center justify-center text-sm font-medium">
                GB
              </div>
            </div>
          </div>
        </div>
      </header>

      {/* Sub-header - Light Blue */}
      <div className="bg-intapp-light text-white">
        <div className="container mx-auto px-4 py-2">
          <h1 className="text-lg font-medium">Admin Portal</h1>
        </div>
      </div>
    </>
  )
}

