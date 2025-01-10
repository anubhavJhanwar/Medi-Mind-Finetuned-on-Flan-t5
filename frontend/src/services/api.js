import axios from 'axios'

const client = axios.create({
  baseURL: 'http://localhost:8001',
  timeout: 600000,
})

export async function askQuestion(question) {
  const { data } = await client.post('/ask', { question })
  return data
}

export async function checkHealth() {
  const { data } = await client.get('/health')
  return data
}
