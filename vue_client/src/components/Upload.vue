<template>
  <v-container class="text-center">
    <v-row>
      <v-col>
        <v-file-input
        color="black"
        truncate-length="15"
        prepend-icon="mdi-camera"
        label="Please upload a file for processing."
        outlined
        dense
        ></v-file-input>
        <p class="font-weight-light Heading 6"></p>
      </v-col>
        
        
    </v-row>
  </v-container>
</template>

<script>
  export default {
    name: 'upload',

    data: () => ({
    
    })  
  }
</script>
