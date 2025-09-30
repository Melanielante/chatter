import { useEffect, useState } from "react";
import { fetchPosts } from "../utils/Api";
import PostList from "../components/PostList";

function Explore() {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchPosts()
      .then((data) => {
        setPosts(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Error fetching posts:", err);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading explore...</p>;

  return (
    <div className="explore">
      <h2>Explore</h2>
      {posts.length === 0 ? (
        <p>No posts yet.</p>
      ) : (
        <PostList posts={posts} />
      )}
    </div>
  );
}

export default Explore;
