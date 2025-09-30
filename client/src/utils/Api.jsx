// Use environment variable
const BASE_URL = import.meta.env.VITE_API_URL;

// Helper to get JWT token from localStorage
function getToken() {
  return localStorage.getItem("token"); // token saved after login
}

// Helper to set headers with Authorization
function authHeaders() {
  const token = getToken();
  return {
    "Content-Type": "application/json",
    ...(token ? { Authorization: `Bearer ${token}` } : {}),
  };
}

// ------------------ Posts ------------------
export async function fetchPosts() {
  const res = await fetch(`${BASE_URL}/posts`, { headers: authHeaders() });
  if (!res.ok) throw new Error("Failed to fetch posts");
  return res.json();
}

export async function fetchPostById(id) {
  const res = await fetch(`${BASE_URL}/posts/${id}`, { headers: authHeaders() });
  if (!res.ok) throw new Error("Failed to fetch post");
  return res.json();
}

export async function createPost(data) {
  const res = await fetch(`${BASE_URL}/posts`, {
    method: "POST",
    headers: authHeaders(),
    body: JSON.stringify(data),
  });
  if (!res.ok) throw new Error("Failed to create post");
  return res.json();
}

export async function updatePost(id, data) {
  const res = await fetch(`${BASE_URL}/posts/${id}`, {
    method: "PATCH",
    headers: authHeaders(),
    body: JSON.stringify(data),
  });
  if (!res.ok) throw new Error("Failed to update post");
  return res.json();
}

export async function deletePost(id) {
  const res = await fetch(`${BASE_URL}/posts/${id}`, {
    method: "DELETE",
    headers: authHeaders(),
  });
  if (!res.ok) throw new Error("Failed to delete post");
  return true;
}

// ------------------ Likes ------------------
export async function addLike(postId, userId) {
  const res = await fetch(`${BASE_URL}/likes`, {
    method: "POST",
    headers: authHeaders(),
    body: JSON.stringify({ post_id: postId, user_id: userId }),
  });
  if (!res.ok) throw new Error("Failed to add like");
  return res.json();
}

// ------------------ Comments ------------------
export async function addComment(postId, userId, content) {
  const res = await fetch(`${BASE_URL}/comments`, {
    method: "POST",
    headers: authHeaders(),
    body: JSON.stringify({ post_id: postId, user_id: userId, content }),
  });
  if (!res.ok) throw new Error("Failed to add comment");
  return res.json();
}

// ------------------ Groups ------------------
export async function fetchGroups() {
  const res = await fetch(`${BASE_URL}/groups`, { headers: authHeaders() });
  if (!res.ok) throw new Error("Failed to fetch groups");
  return res.json();
}

export async function fetchGroupById(id) {
  const res = await fetch(`${BASE_URL}/groups/${id}`, { headers: authHeaders() });
  if (!res.ok) throw new Error("Failed to fetch group");
  return res.json();
}

// ------------------ Users ------------------
export async function fetchUserById(id) {
  const res = await fetch(`${BASE_URL}/users/${id}`, { headers: authHeaders() });
  if (!res.ok) throw new Error("Failed to fetch user");
  return res.json();
}
