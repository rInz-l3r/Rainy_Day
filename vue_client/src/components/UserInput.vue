<template>
    <div>
        <h3 class="font-weight-light">User Input</h3>
        <div class="Input">
            <v-text-field label="First Name" underlined dense color=#00BCD4></v-text-field>
            <v-text-field label="Last Name" underlined dense color=#00BCD4></v-text-field>
        </div>
        <div class="Button">
            <v-btn text> Submit </v-btn>
        </div>
    </div>
</template>

<script>
    export default {
        
    }
</script>

<style>

    .Input{
        margin-top: 5px;
    }

    .Button {
        text-align: right;
        margin: -10px;
    }

</style>