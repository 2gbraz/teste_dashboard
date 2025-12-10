'use client'

import { useState, useEffect } from 'react'
import FileUpload from '@/components/FileUpload'
import ChatInterface from '@/components/ChatInterface'
import UsersTable from '@/components/UsersTable'
import ActionButtons from '@/components/ActionButtons'
import Header from '@/components/Header'
import Footer from '@/components/Footer'
import { User, Message } from '@/types'

export default function Home() {
  const [processedUsers, setProcessedUsers] = useState<User[] | null>(null)
  const [messages, setMessages] = useState<Message[]>([])
  const [isLoading, setIsLoading] = useState(false)
  const [showChat, setShowChat] = useState(false)

  useEffect(() => {
    // Initialize with welcome message
    if (messages.length === 0) {
      const welcomeMessage: Message = {
        role: 'assistant',
        content: "Hello! I'm ready to help you upload and process user data from Excel files. Please upload an Excel file to get started.",
      }
      setMessages([welcomeMessage])
    }
  }, [])

  const handleFileProcessed = (users: User[]) => {
    setProcessedUsers(users)
  }

  const handleUsersUpdated = () => {
    // Optionally clear processed users after update
    // setProcessedUsers(null)
  }

  const handleClearData = () => {
    setProcessedUsers(null)
  }

  return (
    <div className="min-h-screen flex flex-col bg-gray-50">
      <Header />
      
      <main className="flex-1 container mx-auto px-4 py-6">
        {/* Action Buttons and File Upload Section */}
        <div className="mb-6 flex flex-wrap items-center justify-between gap-4">
          <div className="flex flex-wrap gap-3">
            <ActionButtons
              users={processedUsers || []}
              onUsersUpdated={handleUsersUpdated}
              onClearData={handleClearData}
            />
          </div>
          <div className="flex items-center gap-4">
            <FileUpload onFileProcessed={handleFileProcessed} />
            <button
              onClick={() => setShowChat(!showChat)}
              className="px-4 py-2 bg-intapp-light text-white rounded hover:bg-intapp-light/90 transition-colors font-medium text-sm"
            >
              {showChat ? 'Hide Chat' : 'Show Chat'}
            </button>
          </div>
        </div>

        {/* Users Table */}
        {processedUsers && processedUsers.length > 0 ? (
          <UsersTable users={processedUsers} />
        ) : (
          <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-12 text-center">
            <p className="text-gray-500 text-lg">
              No users loaded. Please upload an Excel file to get started.
            </p>
          </div>
        )}

        {/* Chat Interface Modal/Overlay */}
        {showChat && (
          <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
            <div className="bg-white rounded-lg shadow-xl w-full max-w-4xl h-[80vh] flex flex-col">
              <div className="flex items-center justify-between p-4 border-b">
                <h2 className="text-xl font-semibold">AI Chat Assistant</h2>
                <button
                  onClick={() => setShowChat(false)}
                  className="text-gray-500 hover:text-gray-700 text-2xl"
                >
                  ×
                </button>
              </div>
              <div className="flex-1 overflow-hidden">
                <ChatInterface
                  messages={messages}
                  setMessages={setMessages}
                  processedUsers={processedUsers}
                  isLoading={isLoading}
                  setIsLoading={setIsLoading}
                />
              </div>
            </div>
          </div>
        )}
      </main>

      <Footer />
    </div>
  )
}

