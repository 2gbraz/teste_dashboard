'use client'

import { useState } from 'react'
import { RefreshCw, CheckCircle2, AlertCircle, XCircle } from 'lucide-react'
import { User, UpdateResults } from '@/types'
import { updateUsers } from '@/lib/api'

interface ActionButtonsProps {
  users: User[]
  onUsersUpdated: () => void
  onClearData: () => void
}

export default function ActionButtons({
  users,
  onUsersUpdated,
  onClearData,
}: ActionButtonsProps) {
  const [isUpdating, setIsUpdating] = useState(false)
  const [results, setResults] = useState<UpdateResults | null>(null)
  const [showDetails, setShowDetails] = useState(false)

  const handleUpdateUsers = async () => {
    setIsUpdating(true)
    setResults(null)

    try {
      const updateResults = await updateUsers(users)
      setResults(updateResults)
      if (!updateResults.error) {
        onUsersUpdated()
      }
    } catch (error: any) {
      setResults({
        total: users.length,
        successful: 0,
        failed: users.length,
        results: {},
        error: error.message || 'Failed to update users',
      })
    } finally {
      setIsUpdating(false)
    }
  }

  return (
    <div className="space-y-4">
      {/* Action Buttons - Green Horizontal Layout */}
      <div className="flex flex-wrap gap-3">
        <button
          onClick={handleUpdateUsers}
          disabled={isUpdating}
          className="px-4 py-2 bg-intapp-green text-white rounded hover:bg-intapp-green-hover disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2 transition-colors font-medium text-sm"
        >
          {isUpdating ? (
            <>
              <RefreshCw className="w-4 h-4 animate-spin" />
              Updating...
            </>
          ) : (
            'Update Users in Service'
          )}
        </button>
        <button
          onClick={onClearData}
          className="px-4 py-2 bg-intapp-green text-white rounded hover:bg-intapp-green-hover flex items-center gap-2 transition-colors font-medium text-sm"
        >
          Clear Processed Data
        </button>
      </div>

      {/* Results Display */}
      {results && (
        <div className="mt-4 space-y-3">
          {results.error ? (
            <div className="p-3 bg-red-50 border border-red-200 rounded-lg flex items-center gap-2">
              <XCircle className="w-5 h-5 text-red-600" />
              <span className="text-sm text-red-800">{results.error}</span>
            </div>
          ) : (
            <>
              <div className="p-3 bg-green-50 border border-green-200 rounded-lg">
                <div className="flex items-center gap-2 mb-2">
                  <CheckCircle2 className="w-5 h-5 text-green-600" />
                  <span className="text-sm font-medium text-green-800">
                    Updated {results.successful}/{results.total} users successfully
                  </span>
                </div>
                {results.failed > 0 && (
                  <div className="flex items-center gap-2 mt-2">
                    <AlertCircle className="w-4 h-4 text-yellow-600" />
                    <span className="text-xs text-yellow-800">
                      {results.failed} users failed to update
                    </span>
                  </div>
                )}
              </div>

              <button
                onClick={() => setShowDetails(!showDetails)}
                className="text-sm text-blue-600 hover:text-blue-800 py-2"
              >
                {showDetails ? 'Hide' : 'Show'} Detailed Results
              </button>

              {showDetails && (
                <div className="p-3 bg-gray-50 rounded-lg border border-gray-200 max-h-60 overflow-y-auto">
                  <pre className="text-xs text-gray-700">
                    {JSON.stringify(results.results, null, 2)}
                  </pre>
                </div>
              )}
            </>
          )}
        </div>
      )}
    </div>
  )
}

