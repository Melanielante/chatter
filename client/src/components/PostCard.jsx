import React, { useState } from "react";
import CommentForm from "./CommentForm";
import CommentList from "./CommentList";

function PostCard({ post, onAddComment, onUpdatePost, onDeletePost }) {
  const [showComments, setShowComments] = useState(false);
  const [editing, setEditing] = useState(false);
  const [content, setContent] = useState(post.content);

  const handleSave = () => {
    onUpdatePost(post.id, { content });
    setEditing(false);
  };

  return (
    <div className="post-card">
      <h3 className="post-user">{post.user?.username}</h3>

      {editing ? (
        <textarea
          value={content}
          onChange={(e) => setContent(e.target.value)}
          rows="3"
          className="post-edit-textarea"
        />
      ) : (
        <p className="post-content">{post.content}</p>
      )}

      {post.group && <small className="post-group">Group: {post.group.name}</small>}

      {/* Likes */}
      <div className="post-likes">
        <strong>{post.likes?.length || 0} Likes</strong>
      </div>

      {/* Edit/Delete */}
      <div className="post-actions">
        {editing ? (
          <button className="btn btn-save" onClick={handleSave}>
            Save
          </button>
        ) : (
          <button className="btn btn-edit" onClick={() => setEditing(true)}>
            Edit
          </button>
        )}
        <button className="btn btn-delete" onClick={() => onDeletePost(post.id)}>
          Delete
        </button>
      </div>

      {/* Toggle comments */}
      <button
        className="btn btn-toggle"
        onClick={() => setShowComments(!showComments)}
      >
        {showComments ? "Hide" : "Show"} Comments
      </button>

      {/* Comments */}
      {showComments && (
        <div className="post-comments">
          <CommentList comments={post.comments || []} />
          <CommentForm
            postId={post.id}
            onAddComment={(commentData) => onAddComment(post.id, commentData)}
          />
        </div>
      )}
    </div>
  );
}

export default PostCard;
