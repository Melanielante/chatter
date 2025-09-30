import { useEffect, useState } from "react";
import { useParams } from "react-router";
import { fetchPostById, addComment, addLike } from "../utils/Api";
import CommentList from "../components/CommentList";
import CommentForm from "../components/CommentForm";

function PostDetail() {
  const { id } = useParams();
  const [post, setPost] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchPostById(id)
      .then((data) => {
        setPost(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Error fetching post:", err);
        setLoading(false);
      });
  }, [id]);

  const handleAddComment = async (commentData) => {
    try {
      const newComment = await addComment(
        commentData.post_id,
        commentData.user_id,
        commentData.content
      );
      setPost({
        ...post,
        comments: [...(post.comments || []), newComment],
      });
    } catch (err) {
      console.error("Error adding comment:", err);
    }
  };

  const handleLike = async () => {
    try {
      // placeholder user until auth
      const userId = 1;
      const newLike = await addLike(post.id, userId);

      setPost({
        ...post,
        likes: [...(post.likes || []), newLike],
      });
    } catch (err) {
      console.error("Error liking post:", err);
    }
  };

  if (loading) return <p>Loading post...</p>;
  if (!post) return <p>Post not found.</p>;

  return (
    <div className="post-detail">
      <h2>Post Details</h2>

      <div className="post-card">
        <p>{post.content}</p>
        <small>
          Posted by {post.user?.username}
          {post.group ? ` in ${post.group.name}` : ""}
        </small>
      </div>

      <div className="likes">
        <p>Likes: {post.likes?.length || 0}</p>
        <button onClick={handleLike}>👍 Like</button>
        <ul>
          {post.likes?.map((likeUser) => (
            <li key={likeUser.id}>{likeUser.username}</li>
          ))}
        </ul>
      </div>

      <div className="comments">
        <h3>Comments</h3>
        <CommentList comments={post.comments || []} />
        <CommentForm postId={post.id} onAddComment={handleAddComment} />
      </div>
    </div>
  );
}

export default PostDetail;
