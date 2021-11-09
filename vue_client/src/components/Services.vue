<template>
    <div class="element">
        <h3 class="font-weight-light">Services</h3>
        <div class="margin">
            <b class="font-weight-light">User Service </b>
            <v-icon :color="user_service_status">mdi-database</v-icon>
        </div>
        <div class="margin">
            <b class="font-weight-light">Data Service </b>
            <v-icon :color="data_service_status">mdi-database</v-icon>
        </div>
        <div class="margin">
            <b class="font-weight-light">Auth Service </b>
            <v-icon :color="auth_service_status">mdi-database</v-icon>
        </div>
    </div>
</template>

<script>
    export default {
        data: () => {
            return {
                user_service_status : 'red',
                data_service_status : 'red',
                auth_service_status : 'red'
            }
        },

        async mounted() {
            await this.checkUserDB();
        },

        methods: {
            async checkUserDB() {
                let resp = await fetch('/users');
                if (resp.status == 200) {
                    this.user_service_status = 'green';
                }
            }
        }
    }
</script>

<style scoped>

    .margin {
        margin-top: 5px;
    }

    .status {
        color: red;
    }
</style>