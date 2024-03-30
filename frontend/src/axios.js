import axios from 'axios'

export function sleep(ms = 400) {
  console.log('Kindly remember to remove `sleep`');
  return new Promise((resolve) => setTimeout(resolve, ms));
}

export const client = axios.create({
  withCredentials: true,
  baseURL: 'http://localhost:8013',
});