'use client'

import { useState } from 'react'
import { Users, ChevronDown, ChevronUp } from 'lucide-react'
import { User } from '@/types'

interface UserPreviewProps {
  users: User[]
}

export default function UserPreview({ users }: UserPreviewProps) {
  const [isExpanded, setIsExpanded] = useState(false)
  const previewCount = 5

  return (
    <div className="bg-white rounded-lg shadow-md p-6">
      <div className="flex items-center justify-between mb-4">
        <h2 className="text-xl font-semibold text-gray-900 flex items-center gap-2">
          <Users className="w-5 h-5 text-primary-600" />
          Processed Users
        </h2>
        <span className="text-sm text-gray-500 bg-gray-100 px-3 py-1 rounded-full">
          {users.length} total
        </span>
      </div>

      <div className="space-y-2">
        {(isExpanded ? users : users.slice(0, previewCount)).map((user, index) => (
          <div
            key={user.id}
            className="p-3 bg-gray-50 rounded-lg border border-gray-200"
          >
            <div className="flex items-center justify-between mb-1">
              <span className="font-medium text-gray-900">ID: {user.id}</span>
            </div>
            <div className="text-sm text-gray-600">
              {Object.keys(user.data).length > 0 ? (
                <div className="mt-1 space-y-1">
                  {Object.entries(user.data).slice(0, 3).map(([key, value]) => (
                    <div key={key} className="flex gap-2">
                      <span className="font-medium">{key}:</span>
                      <span>{String(value)}</span>
                    </div>
                  ))}
                  {Object.keys(user.data).length > 3 && (
                    <span className="text-gray-400 text-xs">
                      +{Object.keys(user.data).length - 3} more fields
                    </span>
                  )}
                </div>
              ) : (
                <span className="text-gray-400">No additional data</span>
              )}
            </div>
          </div>
        ))}
      </div>

      {users.length > previewCount && (
        <button
          onClick={() => setIsExpanded(!isExpanded)}
          className="mt-4 w-full py-2 text-sm text-primary-600 hover:text-primary-700 flex items-center justify-center gap-2 transition-colors"
        >
          {isExpanded ? (
            <>
              <ChevronUp className="w-4 h-4" />
              Show Less
            </>
          ) : (
            <>
              <ChevronDown className="w-4 h-4" />
              Show All ({users.length} users)
            </>
          )}
        </button>
      )}
    </div>
  )
}

