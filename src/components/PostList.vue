<template>
  <div>
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light shadow-sm">
      <div class="container">
        <!-- Logo and Brand -->
        <a class="navbar-brand" href="#">
          <img src="../assets/blog.png" alt="Logo" height="50" class="d-inline-block align-top">
        </a>
        <!-- Toggler/collapsible Button -->
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <!-- Navbar Links -->
        <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link" href="#">Home</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Contact</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <!-- Main Content -->
    <div class="container mt-5">
      <div class="row">
        <!-- Blog Posts -->
        <div class="col-md-8">
          <div class="card mb-4">
            <div class="card-body">
              <!-- Blog post content -->
              <template v-for="(post, index) in paginatedPosts" :key="index">
                <h3>
                  <router-link :to="{ name: 'PostDetail', params: { year: post.year, month: post.month, day: post.day, slug: post.slug }}" class="text-decoration-none">
                    {{ post.title }}
                  </router-link>
                </h3>
                <p class="text-muted">Published {{ post.publish }} by {{ post.author }}</p>
                <p>{{ getFirstParagraph(post.body) }}...</p>
                <!-- Separator line if needed between posts -->
                <hr v-if="index !== paginatedPosts.length - 1">
              </template>
            </div>
          </div>

          <!-- Pagination -->
          <nav aria-label="Page navigation example">
            <ul class="pagination justify-content-center">
              <li class="page-item" :class="{ disabled: currentPage === 1 }">
                <a class="page-link" href="#" @click.prevent="previousPage">Previous</a>
              </li>
              <li class="page-item" v-for="page in totalPages" :key="page" :class="{ active: page === currentPage }">
                <a class="page-link" href="#" @click.prevent="setCurrentPage(page)">{{ page }}</a>
              </li>
              <li class="page-item" :class="{ disabled: currentPage === totalPages }">
                <a class="page-link" href="#" @click.prevent="nextPage">Next</a>
              </li>
            </ul>
          </nav>
        </div>

        <!-- Sidebar -->
        <div class="col-md-4">
          <div class="card mb-4">
            <div class="card-body">
              <h3 class="card-title">About This Blog</h3>
              <p class="card-text">Welcome to my blog! Here you can find various posts on different topics. Feel free to browse and enjoy the content.</p>
            </div>
            <div class="card-body">
              <h4 class="card-title">Other Blogs</h4>
              <ul class="list-unstyled">
                <!-- Render other blogs dynamically -->
                <li v-for="(post, index) in processed_posts" :key="index">
                  <router-link :to="{ name: 'PostDetail', params: { year: post.year, month: post.month, day: post.day, slug: post.slug }}" class="text-decoration-none">
                    {{ post.title }}
                  </router-link>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Footer -->
    <footer class="bg-dark text-white mt-5 p-4 text-center">
      <div class="container">
        <p class="mb-0">© 2024 Agri-pulse. All rights reserved.</p>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';
import moment from 'moment';

// Data
const posts = ref([]);

// Pagination variables
const currentPage = ref(1);
const postsPerPage = 5; // Number of posts per page

// Computed property to process posts
const processed_posts = computed(() => {
  return posts.value.map(post => ({
    ...post,
    year: moment(post.publish).format('Y'),
    month: moment(post.publish).format('M'),
    day: moment(post.publish).format('D')
  }));
});

// Computed property for paginated posts
const paginatedPosts = computed(() => {
  const startIndex = (currentPage.value - 1) * postsPerPage;
  return processed_posts.value.slice(startIndex, startIndex + postsPerPage);
});

// Computed property for total pages
const totalPages = computed(() => {
  return Math.ceil(processed_posts.value.length / postsPerPage);
});

// Methods
const setCurrentPage = (page) => {
  currentPage.value = page;
};

const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++;
  }
};

const previousPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--;
  }
};

// Method to get the first paragraph
const getFirstParagraph = (body) => {
  const paragraphs = body.split('\n');
  return paragraphs.length > 0 ? paragraphs[0] : body;
};

// Fetch posts on mounted
onMounted(() => {
  axios.get('http://localhost:8000/blog/post/')
    .then(response => {
      posts.value = response.data;
    })
    .catch(error => {
      console.error('Error fetching posts:', error);
    });
});
</script>
