import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'Intapp Admin Portal - Users',
  description: 'Admin Portal for managing users and user data',
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

