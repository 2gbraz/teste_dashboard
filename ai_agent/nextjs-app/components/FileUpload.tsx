'use client'

import { useState, useRef } from 'react'
import { Upload, FileSpreadsheet, AlertCircle, CheckCircle2 } from 'lucide-react'
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

  const handleFileChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (!file) return

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

  const handleDrop = async (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault()
    const file = e.dataTransfer.files[0]
    if (!file) return

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
    }
  }

  const handleDragOver = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault()
  }

  return (
    <div className="bg-white rounded-lg shadow-md p-6">
      <h2 className="text-xl font-semibold text-gray-900 mb-4 flex items-center gap-2">
        <FileSpreadsheet className="w-5 h-5 text-primary-600" />
        Upload Excel File
      </h2>

      <div
        className="border-2 border-dashed border-gray-300 rounded-lg p-8 text-center hover:border-primary-400 transition-colors cursor-pointer"
        onDrop={handleDrop}
        onDragOver={handleDragOver}
        onClick={() => fileInputRef.current?.click()}
      >
        <input
          ref={fileInputRef}
          type="file"
          accept=".xlsx,.xls"
          onChange={handleFileChange}
          className="hidden"
        />

        {isUploading ? (
          <div className="flex flex-col items-center">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600 mb-4"></div>
            <p className="text-gray-600">Processing file...</p>
          </div>
        ) : (
          <>
            <Upload className="w-12 h-12 text-gray-400 mx-auto mb-4" />
            <p className="text-gray-600 mb-2">
              Click to upload or drag and drop
            </p>
            <p className="text-sm text-gray-500">
              Excel files only (.xlsx, .xls)
            </p>
            <p className="text-xs text-gray-400 mt-2">
              Must include an 'id' column
            </p>
          </>
        )}
      </div>

      {uploadStatus.type && (
        <div
          className={`mt-4 p-3 rounded-lg flex items-center gap-2 ${
            uploadStatus.type === 'success'
              ? 'bg-green-50 text-green-800'
              : 'bg-red-50 text-red-800'
          }`}
        >
          {uploadStatus.type === 'success' ? (
            <CheckCircle2 className="w-5 h-5" />
          ) : (
            <AlertCircle className="w-5 h-5" />
          )}
          <span className="text-sm">{uploadStatus.message}</span>
        </div>
      )}
    </div>
  )
}

