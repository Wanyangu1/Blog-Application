<template>
    <div>
      <nav class="navbar navbar-expand-lg navbar-light bg-light shadow-sm">
        <div class="container">
          <a class="navbar-brand" href="/dashboard">
            <img src="../assets/blog.png" alt="Logo" height="50" class="d-inline-block align-top">
          </a>
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
            <ul class="navbar-nav">
              <li class="nav-item">
                <a class="nav-link" href="/dashboard">Home</a>
              </li>
              <li class="nav-item">
                <router-link :to="{ name: 'CreatePost' }" class="nav-link">Create Post</router-link>
              </li>
            </ul>
          </div>
        </div>
      </nav>
  
      <div class="container mt-5">
        <div class="row">
          <div class="col-md-8 offset-md-2">
            <h2>Create a New Post</h2>
            <form @submit.prevent="submitPost">
              <div class="form-group">
                <label for="title">Title</label>
                <input type="text" class="form-control" id="title" v-model="post.title" required>
              </div>
              <div class="form-group">
                <label for="slug">Slug</label>
                <input type="text" class="form-control" id="slug" v-model="post.slug" required>
              </div>
              <div class="form-group">
                <label for="author">Author</label>
                <input type="text" class="form-control" id="author" v-model="post.author" required>
              </div>
              <div class="form-group">
                <label for="body">Body</label>
                <textarea class="form-control" id="body" rows="5" v-model="post.body" required></textarea>
              </div>
              <div class="form-group">
                <label for="status">Status</label>
                <select class="form-control" id="status" v-model="post.status" required>
                  <option value="draft">Draft</option>
                  <option value="published">Published</option>
                </select>
              </div>
              <button type="submit" class="btn btn-primary">Submit</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import axios from 'axios';
  import { useRouter } from 'vue-router';
  
  const router = useRouter();
  const post = ref({
    title: '',
    slug: '',
    author: '',
    body: '',
    status: 'draft'
  });
  
  const submitPost = async () => {
    try {
      const response = await axios.post('http://localhost:8000/blog/post/create/', post.value, {
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('token')}`
        }
      });
      if (response.status === 201) {
        router.push({ name: 'PostList' });
      }
    } catch (error) {
      console.error('Error creating post:', error);
    }
  };
  </script>
  