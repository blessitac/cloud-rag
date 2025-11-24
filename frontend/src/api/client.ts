const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export async function apiGet(path: string) {
  const res = await fetch(`${API_BASE_URL}${path}`);
  return res.json();
}

export const api = { get: apiGet };