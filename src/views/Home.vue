<template>
    <v-container fluid>
      <v-row>
        <working/>
      </v-row>
      <v-row>
        <upload/>
      </v-row>
    </v-container>
</template>

<script>
  import working from '../components/Title.vue'
  import upload from '../components/Upload.vue'

  export default {
    name: 'Home',

    components: {
        working,
        upload,
    },
  }
</script>
