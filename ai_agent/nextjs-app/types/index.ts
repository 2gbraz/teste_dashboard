export interface User {
  id: string
  data: Record<string, any>
}

export interface Message {
  role: 'user' | 'assistant'
  content: string
}

export interface UpdateResults {
  total: number
  successful: number
  failed: number
  results: Record<string, boolean>
  error?: string
}

export interface ChatResponse {
  message: string
}

