<template>
    <div>
        <v-list>
           <v-list-item v-for="item in this.entries" v-bind:key="item">
               {{item}}
           </v-list-item>

        </v-list>
    </div>
</template>

<script>
    let entries = ['Jacob','Something About Me','Something About Me','Something About Me']

    export default {
        data: () => {
            return {
                entries
            }
        }
    }
    
</script>

<style scoped>

</style>