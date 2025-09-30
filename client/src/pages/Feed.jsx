import React, { useEffect, useState } from "react";
import { fetchPosts, createPost, addComment, updatePost, deletePost } from "../utils/Api";
import PostList from "../components/PostList";
import PostForm from "../components/PostForm";

function Feed() {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);

  // Load posts on mount
  useEffect(() => {
    loadPosts();
  }, []);

  const loadPosts = async () => {
    try {
      setLoading(true);
      const data = await fetchPosts();
      setPosts(data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  // Add a new post
  const handleAddPost = async (postData) => {
    try {
      const newPost = await createPost(postData);
      setPosts([newPost, ...posts]); 
    } catch (err) {
      console.error("Error creating post:", err);
    }
  };

  // Add a new comment
  const handleAddComment = async (postId, commentData) => {
    try {
      const newComment = await addComment(
        postId,
        commentData.user_id,
        commentData.content
      );

      setPosts((prevPosts) =>
        prevPosts.map((post) =>
          post.id === postId
            ? { ...post, comments: [...(post.comments || []), newComment] }
            : post
        )
      );
    } catch (err) {
      console.error("Error adding comment:", err);
    }
  };

  // Update a post
  const handleUpdatePost = async (postId, updatedData) => {
    try {
      const updatedPost = await updatePost(postId, updatedData);
      setPosts((prevPosts) =>
        prevPosts.map((post) => (post.id === postId ? updatedPost : post))
      );
    } catch (err) {
      console.error("Error updating post:", err);
    }
  };

  // Delete a post
  const handleDeletePost = async (postId) => {
    try {
      await deletePost(postId);
      setPosts((prevPosts) => prevPosts.filter((post) => post.id !== postId));
    } catch (err) {
      console.error("Error deleting post:", err);
    }
  };

  if (loading) return <p>Loading posts...</p>;

  return (
    <div className="feed">
      <h2>Feed</h2>
      <PostForm onAddPost={handleAddPost} />
      <PostList
        posts={posts}
        onAddComment={handleAddComment}
        onUpdatePost={handleUpdatePost}
        onDeletePost={handleDeletePost}
      />
    </div>
  );
}

export default Feed;
