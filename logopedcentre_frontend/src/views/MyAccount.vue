<template>
    <div class="page-my-account">
        <div class="columns is-multiline is-centered">
            <div class="column is-6">
                <h1 class="is-size-3 has-text-centered">Профиль:</h1>

                <form @submit.prevent="submitForm">
                <div class="field">
                    <label class="label">Фамилия</label>
                    <div class="control">
                        <input class="input" type="text" placeholder="Тюрин" v-model="sname">
                    </div>
                </div>
                
                <div class="field">
                    <label class="label">Имя</label>
                    <div class="control">
                        <input class="input" type="text" placeholder="Сергей" v-model="name">
                    </div>
                </div>

                <div class="field">
                    <label class="label">Отчество</label>
                    <div class="control">
                        <input class="input" type="text" placeholder="Сергеевич" v-model="tname">
                    </div>
                </div>  
                    
                <div class="field">
                    <label class="label">Телефон</label>
                    <div class="control">
                        <input class="input" type="text" placeholder="89115926942" v-model="phone">
                    </div>
                </div>

                <div class="field">
                    <div class="control">
                        <label class="checkbox">
                        <input type="checkbox">
                        I agree to the <a href="#">terms and conditions</a>
                        </label>
                    </div>
                </div>

                <div class="field is-grouped">
                    <div class="control">
                        <button class="button is-link">Submit</button>
                    </div>
                    <div class="control">
                        <button class="button is-link is-light">Cancel</button>
                    </div>
                </div>
            </form>
            </div>





            <div class="column is-6">
                <h1 class="is-size-3 has-text-centered">Мои дети:</h1>
            </div>

            <div class="column is-12">
                <button @click="logout()" class="button is-danger">Выйти</button>
            </div>

            <hr>

            <div class="column is-12">
                <h2 class="subtitle">Мои записи</h2>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'



export default {
    name: 'MyAccount',
    components: {
        
    },
    data() {
        return {
            orders: []
        }
    },
    mounted() {
        document.title = 'Мой аккаунт | Logoped'
        this.getMyOrders()
    },
    methods: {
        logout() {
            axios.defaults.headers.common["Authorization"] = ""
            localStorage.removeItem("token")
            localStorage.removeItem("username")
            localStorage.removeItem("userid")
            this.$store.commit('removeToken') 
            this.$router.push('/')
        },
        
        async getMyOrders() {
            this.$store.commit('setIsLoading', true)

            await axios
                .get('/api/v1/orders/')
                .then(response => {
                    this.orders = response.data
                })
                .catch(error => {
                    console.log(error)
                })
            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>