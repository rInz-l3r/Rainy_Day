<template>
    <div>
        <div class="block">
            <div class="panel">
                <UserInput/>
            </div>
            <div class="panel">
                <Users/>
            </div>
            <div class="panel">
                <Services/>
            </div>
        </div>
    </div>
    
    <!-- <div>
        <div class="container">
        <div class="leftPane">
            <UserInput/>
        </div>
        <div class="centerPane">
            <Users/>
        </div>
        <div class="rightPane">
             <Services/>
        </div>
    </div>
        <div class="container">
        <div class="leftPane">
        </div>
        <div class="centerPane">
        </div>
        <div class="rightPane">
        </div>
        </div>
    </div> -->
</template>

<script>
    import Users from '../components/Users.vue'
    import UserInput from '../components/UserInput.vue'
    import Services from '../components/Services.vue'

    export default {
        components: {
            Users,
            UserInput,
            Services
        }
    }
</script>

<style scoped>

    .block {
        display: flex;
        justify-content: center;
    }

    .panel {
        padding: 10px;
        flex-basis: 25%;
        text-align: center;
    }
   
</style>