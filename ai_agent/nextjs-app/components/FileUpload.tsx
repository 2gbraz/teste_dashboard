'use client'

import { useState, useRef } from 'react'
import { Upload, AlertCircle, CheckCircle2 } from 'lucide-react'
import { User } from '@/types'
import { processExcelFile } from '@/lib/api'

interface FileUploadProps {
  onFileProcessed: (users: User[]) => void
}

export default function FileUpload({ onFileProcessed }: FileUploadProps) {
  const [isUploading, setIsUploading] = useState(false)
  const [uploadStatus, setUploadStatus] = useState<{
    type: 'success' | 'error' | null
    message: string
  }>({ type: null, message: '' })
  const fileInputRef = useRef<HTMLInputElement>(null)

  const processFile = async (file: File) => {
    // Validate file type
    if (!file.name.match(/\.(xlsx|xls)$/i)) {
      setUploadStatus({
        type: 'error',
        message: 'Please upload a valid Excel file (.xlsx or .xls)',
      })
      return
    }

    setIsUploading(true)
    setUploadStatus({ type: null, message: '' })

    try {
      const formData = new FormData()
      formData.append('file', file)

      const users = await processExcelFile(formData)
      onFileProcessed(users)
      setUploadStatus({
        type: 'success',
        message: `Successfully processed ${users.length} users`,
      })
    } catch (error: any) {
      setUploadStatus({
        type: 'error',
        message: error.message || 'Error processing file. Please try again.',
      })
    } finally {
      setIsUploading(false)
      if (fileInputRef.current) {
        fileInputRef.current.value = ''
      }
    }
  }

  const handleFileChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (!file) return
    await processFile(file)
  }

  const handleDrop = async (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault()
    const file = e.dataTransfer.files[0]
    if (!file) return
    await processFile(file)
  }

  const handleDragOver = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault()
  }

  return (
    <div className="relative">
      <label
        className="px-4 py-2 bg-intapp-green text-white rounded hover:bg-intapp-green-hover cursor-pointer inline-flex items-center gap-2 transition-colors font-medium text-sm"
        onDrop={handleDrop}
        onDragOver={handleDragOver}
        onClick={(e) => {
          e.preventDefault()
          fileInputRef.current?.click()
        }}
      >
        <Upload className="w-4 h-4" />
        {isUploading ? 'Processing...' : 'Upload Excel File'}
      </label>
      <input
        ref={fileInputRef}
        type="file"
        accept=".xlsx,.xls"
        onChange={handleFileChange}
        className="hidden"
      />

      {uploadStatus.type && (
        <div
          className={`absolute top-full left-0 mt-2 p-3 rounded-lg flex items-center gap-2 z-10 shadow-lg ${
            uploadStatus.type === 'success'
              ? 'bg-green-50 text-green-800 border border-green-200'
              : 'bg-red-50 text-red-800 border border-red-200'
          }`}
        >
          {uploadStatus.type === 'success' ? (
            <CheckCircle2 className="w-5 h-5" />
          ) : (
            <AlertCircle className="w-5 h-5" />
          )}
          <span className="text-sm whitespace-nowrap">{uploadStatus.message}</span>
        </div>
      )}
    </div>
  )
}

