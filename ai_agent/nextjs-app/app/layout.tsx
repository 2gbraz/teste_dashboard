import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'User Data AI Agent',
  description: 'AI-powered agent for uploading and processing user data from Excel files',
  icons: {
    icon: '🤖',
  },
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className="antialiased">{children}</body>
    </html>
  )
}

