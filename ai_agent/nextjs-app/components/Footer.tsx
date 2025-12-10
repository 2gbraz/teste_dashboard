'use client'

export default function Footer() {
  return (
    <footer className="mt-auto py-4 px-4 text-right text-sm text-gray-600">
      <div className="container mx-auto">
        <div>© 2025 Intapp, Inc.</div>
        <div className="mt-1">
          Region: US, Tenant alias: intappazuretestus, Tenant ID:{' '}
          <a href="#" className="text-blue-600 hover:underline">
            e94f02c92
          </a>
        </div>
      </div>
    </footer>
  )
}

