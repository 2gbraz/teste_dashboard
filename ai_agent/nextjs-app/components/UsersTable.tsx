'use client'

import { useState } from 'react'
import { User } from '@/types'

interface UsersTableProps {
  users: User[]
  onUserClick?: (user: User) => void
}

export default function UsersTable({ users, onUserClick }: UsersTableProps) {
  const [currentPage, setCurrentPage] = useState(1)
  const [rowsPerPage, setRowsPerPage] = useState(10)
  const [searchTerm, setSearchTerm] = useState('')

  // Filter users based on search term
  const filteredUsers = users.filter(user => {
    const searchLower = searchTerm.toLowerCase()
    const userId = user.id.toLowerCase()
    const email = (user.data.email || '').toLowerCase()
    return userId.includes(searchLower) || email.includes(searchLower)
  })

  // Calculate pagination
  const totalPages = Math.ceil(filteredUsers.length / rowsPerPage)
  const startIndex = (currentPage - 1) * rowsPerPage
  const endIndex = startIndex + rowsPerPage
  const paginatedUsers = filteredUsers.slice(startIndex, endIndex)

  // Get status from user data or default to 'Active'
  const getStatus = (user: User): string => {
    return user.data.status || 'Active'
  }

  const handlePageChange = (page: number) => {
    if (page >= 1 && page <= totalPages) {
      setCurrentPage(page)
    }
  }

  const handleRowsPerPageChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const value = parseInt(e.target.value) || 10
    setRowsPerPage(value)
    setCurrentPage(1) // Reset to first page
  }

  return (
    <div className="bg-white rounded-lg shadow-sm border border-gray-200">
      {/* Search Bar */}
      <div className="p-4 border-b border-gray-200">
        <input
          type="text"
          placeholder="Search"
          value={searchTerm}
          onChange={(e) => {
            setSearchTerm(e.target.value)
            setCurrentPage(1) // Reset to first page on search
          }}
          className="px-4 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-intapp-light"
        />
      </div>

      {/* Table */}
      <div className="overflow-x-auto">
        <table className="w-full">
          <thead className="bg-gray-50 border-b border-gray-200">
            <tr>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider">
                User ID
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider">
                Email
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider">
                Status
              </th>
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {paginatedUsers.length === 0 ? (
              <tr>
                <td colSpan={3} className="px-6 py-8 text-center text-gray-500">
                  {searchTerm ? 'No users found matching your search.' : 'No users to display.'}
                </td>
              </tr>
            ) : (
              paginatedUsers.map((user) => (
                <tr
                  key={user.id}
                  className="hover:bg-gray-50 cursor-pointer transition-colors"
                  onClick={() => onUserClick?.(user)}
                >
                  <td className="px-6 py-4 whitespace-nowrap">
                    <a
                      href="#"
                      className="text-blue-600 hover:text-blue-800 hover:underline"
                      onClick={(e) => {
                        e.stopPropagation()
                        onUserClick?.(user)
                      }}
                    >
                      {user.id}
                    </a>
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap">
                    <a
                      href="#"
                      className="text-blue-600 hover:text-blue-800 hover:underline"
                      onClick={(e) => {
                        e.stopPropagation()
                        onUserClick?.(user)
                      }}
                    >
                      {user.data.email || 'N/A'}
                    </a>
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap">
                    <span
                      className={`px-2 py-1 text-xs font-medium rounded ${
                        getStatus(user) === 'Active'
                          ? 'bg-green-100 text-green-800'
                          : 'bg-gray-100 text-gray-800'
                      }`}
                    >
                      {getStatus(user)}
                    </span>
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>

      {/* Pagination */}
      <div className="px-6 py-4 border-t border-gray-200 flex items-center justify-between">
        <div className="flex items-center gap-2">
          <span className="text-sm text-gray-700">Show</span>
          <input
            type="number"
            min="1"
            value={rowsPerPage}
            onChange={handleRowsPerPageChange}
            className="w-16 px-2 py-1 border border-gray-300 rounded text-sm focus:outline-none focus:ring-2 focus:ring-intapp-light"
          />
          <span className="text-sm text-gray-700">rows</span>
        </div>

        <div className="flex items-center gap-2">
          <button
            onClick={() => handlePageChange(1)}
            disabled={currentPage === 1}
            className="px-3 py-1 text-sm border border-gray-300 rounded hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            First
          </button>
          <button
            onClick={() => handlePageChange(currentPage - 1)}
            disabled={currentPage === 1}
            className="px-3 py-1 text-sm border border-gray-300 rounded hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            ‹
          </button>
          {Array.from({ length: Math.min(5, totalPages) }, (_, i) => {
            let pageNum
            if (totalPages <= 5) {
              pageNum = i + 1
            } else if (currentPage <= 3) {
              pageNum = i + 1
            } else if (currentPage >= totalPages - 2) {
              pageNum = totalPages - 4 + i
            } else {
              pageNum = currentPage - 2 + i
            }
            return (
              <button
                key={pageNum}
                onClick={() => handlePageChange(pageNum)}
                className={`px-3 py-1 text-sm border rounded ${
                  currentPage === pageNum
                    ? 'bg-intapp-light text-white border-intapp-light'
                    : 'border-gray-300 hover:bg-gray-50'
                }`}
              >
                {pageNum}
              </button>
            )
          })}
          <button
            onClick={() => handlePageChange(currentPage + 1)}
            disabled={currentPage === totalPages}
            className="px-3 py-1 text-sm border border-gray-300 rounded hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            ›
          </button>
          <button
            onClick={() => handlePageChange(totalPages)}
            disabled={currentPage === totalPages}
            className="px-3 py-1 text-sm border border-gray-300 rounded hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            Last
          </button>
        </div>

        <div className="text-sm text-gray-700">
          Total rows: {filteredUsers.length}
        </div>
      </div>
    </div>
  )
}

