<template>
  <v-app>
  <!-- <v-navigation-drawer app> -->
    <!-- -->
  <!-- </v-navigation-drawer> -->
  <v-app-bar app> 
    <h2 class="font-weight-light">Rainy Day</h2>
  </v-app-bar>
  <!-- Sizes your content based upon application components -->
  <v-main>
    <!-- Provides the application the proper gutter -->
    <v-container fluid>
        <home/>
    </v-container>
  </v-main>

  <v-footer app>
    <!-- -->
  </v-footer>

  
</v-app>
</template>

<script>
import Home from './views/Home.vue';

  export default {
    

    name: 'App',

    data: () => ({
      //
    }),

    components :{
        Home
    }
  };
</script>

<style>

  .img {
    background-blend-mode: darken;
    background-position: center;
    background-size: cover;
  }


</style>
