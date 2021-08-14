<template>
  <v-card>
    <v-toolbar
    src = "../assets/title.jpg">
        <v-toolbar-title class="font-weight-light">Rainy Day</v-toolbar-title>
    </v-toolbar>
    <v-file-input
    accept="image/*"
    label="File input"
    ></v-file-input>
  </v-card>
</template>

<script>
  // import upload from '../components/Upload.vue'

  export default {
    name: 'Home',

    components: {
        // upload,
    },
  }
</script>
