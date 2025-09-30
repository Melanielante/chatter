import React, { useEffect, useState } from "react";
import { fetchPosts, createPost } from "../utils/Api";
import PostForm from "../components/PostForm";
import PostList from "../components/PostList";

function Feed({ user }) {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);

  // fetch posts when component loads
  useEffect(() => {
    fetchPosts()
      .then((data) => {
        setPosts(data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching posts:", error);
        setLoading(false);
      });
  }, []);

  const handleAddPost = async (content) => {
    try {
      const newPost = await createPost({ content, user_id: user.id });
      setPosts([newPost, ...posts]); // add new post at top
    } catch (err) {
      console.error("Error creating post:", err);
    }
  };

  if (loading) return <p>Loading feed...</p>;

  return (
    <div>
      <h2>Chatter Feed</h2>

      {user && <PostForm onSubmit={handleAddPost} />}

      {posts.length === 0 ? (
        <p>No posts yet. Be the first to share something!</p>
      ) : (
        <PostList posts={posts} />
      )}
    </div>
  );
}

export default Feed;
