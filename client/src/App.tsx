import React, { useState, useCallback } from 'react'
import axios from 'axios'

export default function App() {
  const [files, setFiles] = useState<File[]>([])
  const [results, setResults] = useState<{ fileName: string; transcript: string; analysis: string }[]>([])
  const [isProcessing, setIsProcessing] = useState(false)
  const [dragActive, setDragActive] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const handleFileChange = useCallback((event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files) {
      setFiles(Array.from(event.target.files))
    }
  }, [])

  const handleDrag = useCallback((e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault()
    e.stopPropagation()
    if (e.type === "dragenter" || e.type === "dragover") {
      setDragActive(true)
    } else if (e.type === "dragleave") {
      setDragActive(false)
    }
  }, [])

  const handleDrop = useCallback((e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault()
    e.stopPropagation()
    setDragActive(false)
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      setFiles(Array.from(e.dataTransfer.files))
    }
  }, [])

  const handleUpload = async () => {
    setIsProcessing(true)
    setError(null)
    const formData = new FormData()
    files.forEach((file) => formData.append('files', file))

    try {
      const response = await axios.post('http://127.0.0.1:8000/upload', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      })
      setResults(response.data)
    } catch (error) {
      console.error('Error uploading files:', error)
      setError('Failed to upload files. Please try again.')
    } finally {
      setIsProcessing(false)
    }
  }

  return (
    <div className="min-h-screen bg-gray-100 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-4xl mx-auto bg-white rounded-lg shadow-md overflow-hidden">
        <div className="px-4 py-5 sm:px-6">
          <h1 className="text-2xl font-bold text-gray-900 text-center">Multi-File Upload and Processing App</h1>
          <p className="mt-1 text-sm text-gray-600 text-center">Upload audio files for transcription and analysis</p>
        </div>
        <div className="px-4 py-5 sm:p-6">
          <div 
            className={`flex flex-col items-center justify-center w-full h-64 border-2 border-dashed rounded-lg cursor-pointer transition-colors ${
              dragActive ? 'border-blue-400 bg-blue-50' : 'border-gray-300 hover:bg-gray-50'
            }`}
            onDragEnter={handleDrag}
            onDragLeave={handleDrag}
            onDragOver={handleDrag}
            onDrop={handleDrop}
          >
            <label htmlFor="file-upload" className="flex flex-col items-center justify-center w-full h-full">
              <svg className="w-10 h-10 mb-3 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"></path>
              </svg>
              <p className="mb-2 text-sm text-gray-500">
                <span className="font-semibold">Click to upload</span> or drag and drop
              </p>
              <p className="text-xs text-gray-500">WAV, MP3, or OGG (MAX. 10 files)</p>
            </label>
            <input
              id="file-upload"
              type="file"
              className="hidden"
              onChange={handleFileChange}
              multiple
              accept=".wav,.mp3,.ogg"
            />
          </div>
          {files.length > 0 && (
            <div className="mt-4">
              <h3 className="text-lg font-semibold mb-2 text-gray-700">Selected Files:</h3>
              <ul className="list-disc pl-5">
                {files.map((file, index) => (
                  <li key={index} className="text-sm text-gray-600">
                    {file.name}
                  </li>
                ))}
              </ul>
            </div>
          )}
          {error && (
            <div className="mt-4 p-2 bg-red-100 border border-red-400 text-red-700 rounded">
              {error}
            </div>
          )}
          <button
            onClick={handleUpload}
            disabled={files.length === 0 || isProcessing}
            className={`mt-4 w-full py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white ${
              files.length === 0 || isProcessing
                ? 'bg-gray-300 cursor-not-allowed'
                : 'bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500'
            }`}
          >
            {isProcessing ? 'Processing...' : 'Upload and Process Files'}
          </button>
        </div>
        {results.length > 0 && (
          <div className="px-4 py-5 sm:p-6 border-t border-gray-200">
            <h3 className="text-xl font-semibold mb-4 text-gray-900">Results:</h3>
            {results.map((result, index) => (
              <div key={index} className="mb-4 bg-gray-50 rounded-lg p-4">
                <h4 className="text-lg font-medium text-gray-900 flex items-center">
                  <svg className="w-5 h-5 mr-2 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 19V6l12-3v13M9 19c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zm12-3c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zM9 10l12-3"></path>
                  </svg>
                  {result.fileName}
                </h4>
                <div className="mt-2 space-y-2">
                  <p><strong className="text-gray-700">Transcript:</strong> <span className="text-gray-600">{result.transcript}</span></p>
                  <p><strong className="text-gray-700">Analysis:</strong> <span className="text-gray-600">{result.analysis}</span></p>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  )
}