import axios from 'axios'
import { User, ChatResponse, UpdateResults } from '@/types'

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

const api = axios.create({
  baseURL: `${API_URL}/api`,
  headers: {
    'Content-Type': 'application/json',
  },
})

export async function processExcelFile(file: FormData): Promise<User[]> {
  const response = await api.post('/process-excel', file, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  })
  return response.data.users
}

export async function sendChatMessage(
  message: string,
  processedUsers: User[] | null
): Promise<ChatResponse> {
  const response = await api.post('/chat', {
    message,
    processed_users: processedUsers,
  })
  return response.data
}

export async function updateUsers(users: User[]): Promise<UpdateResults> {
  const response = await api.post('/update-users', { users })
  return response.data
}

