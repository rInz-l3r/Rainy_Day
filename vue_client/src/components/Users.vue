<template>
    <div class="Background">
        <h3 class="font-weight-light">Users</h3>
        <div class='table'>
        <v-list class='names' color=rgba(0,0,0,0) dense>
            <v-list-item class="table" v-for="item in this.entries" v-bind:key="item">
                {{item}}
            </v-list-item>
        </v-list>
        </div>
    </div>
    
</template>

<script>
   
    export default {
        data: () => {
            return {
                entries : [],
                bios : [],
            }
        },

        async mounted() {
            await this.getUsers();

        },

        methods: {
            async getUsers() {
                let resp = await fetch('/users');
                let respJson = await resp.json();
                respJson.forEach(element => {
                    this.entries.push(element.name)
                });
            }
        }
}

</script>

<style scoped>

    .table {
        display: flex;
        justify-content: center;
    }
    
    .img{
        flex-basis: 50%;    
    }

    .names {
        flex-basis: 50%;
    }
</style>