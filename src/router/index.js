// src/router/index.js or wherever your router configuration is located

import { createRouter, createWebHistory } from 'vue-router';
import PostListComponent from '../components/PostList.vue'; 
import PostDetailComponent from '../components/PostDetail.vue'; 
import CreatePost from '../components/CreatePost.vue';

const routes = [
  {
    path: '/',
    name: 'PostList',
    component: PostListComponent,
  },
  { 
    path: '/create-post', 
    name: 'CreatePost', 
    component: CreatePost 
  },
  {
    path: '/blog/post',
    name: 'PostList',
    component: PostListComponent,
  },
  {
    path: '/blog/post/:year/:month/:day/:slug',
    name: 'PostDetail',
    component: PostDetailComponent,
    props: true,
  },
  // other routes
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
