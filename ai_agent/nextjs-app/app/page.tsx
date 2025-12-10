'use client'

import { useState, useEffect } from 'react'
import FileUpload from '@/components/FileUpload'
import ChatInterface from '@/components/ChatInterface'
import UserPreview from '@/components/UserPreview'
import ActionButtons from '@/components/ActionButtons'
import { User, Message } from '@/types'

export default function Home() {
  const [processedUsers, setProcessedUsers] = useState<User[] | null>(null)
  const [messages, setMessages] = useState<Message[]>([])
  const [isLoading, setIsLoading] = useState(false)

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
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100">
      <div className="container mx-auto px-4 py-8 max-w-7xl">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-2">
            🤖 User Data AI Agent
          </h1>
          <p className="text-gray-600">
            Upload Excel files with user data and update the user service with AI assistance.
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Sidebar */}
          <div className="lg:col-span-1 space-y-6">
            <FileUpload onFileProcessed={handleFileProcessed} />
            
            {processedUsers && (
              <>
                <UserPreview users={processedUsers} />
                <ActionButtons
                  users={processedUsers}
                  onUsersUpdated={handleUsersUpdated}
                  onClearData={handleClearData}
                />
              </>
            )}
          </div>

          {/* Main Chat Area */}
          <div className="lg:col-span-2">
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
    </div>
  )
}

