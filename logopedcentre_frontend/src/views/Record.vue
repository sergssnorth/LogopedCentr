<template>
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h2 class="is-size-3 has-text-centered mb-5">Запись на прием:</h2>
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label class="label">ФИО</label>
                        <div class="control">
                            <input class="input" type="text" placeholder="Тюрин Сергей Сергеевич" v-model="username">
                        </div>
                    </div>
                    
                    <div class="field">
                        <label class="label">Телефон</label>
                        <div class="control">
                            <input class="input" type="text" placeholder="89115926942" v-model="phone">
                        </div>
                    </div>

        

                    <div class="field">
                        <label class="label">Направление работы</label>
                        <div class="control">
                            <div class="select">
                                <select @change="changeDirection" v-model="selectedDirections">
                                    <option v-for="option in latestDirections" :value="option.id">
                                    {{ option.name }}
                                    </option>
                                </select>
                            </div>
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Специалист</label>
                        <div class="control">
                            <div class="select">
                                <select v-model="selectedSpecialist">
                                    <option v-for="option in latestSpecialists" :value="option.id">
                                    {{option.name}} {{option.sname}} {{option.tname}}
                                    </option>
                                </select>
                            </div>
                        </div>
                    </div>


                    <div class="field">
                    <label class="label">Message</label>
                    <div class="control">
                        <textarea class="textarea" placeholder="Textarea"></textarea>
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

                    <div class="field">
                    <div class="control">
                        <label class="radio">
                        <input type="radio" name="question">
                        Yes
                        </label>
                        <label class="radio">
                        <input type="radio" name="question">
                        No
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
        </div>
</template>
  


<script>
import axios from 'axios'
import { ref } from 'vue'


export default {
    name: 'Record',
    data() {
        return {
            username: '',
            password: '',
            isActiveFirstField: false,
            isActiveSecondField: false,

            selectedDirections: ref('1'),
            latestDirections: ref([]),
            
            selectedSpecialist: ref('1'),
            latestSpecialists: ref([]),

            selected: ref('1'),
            options: ref([
            { text: 'One', value: 'A' },
            { text: 'Two', value: 'B' },
            { text: 'Three', value: 'C' }
            ]),
            errors: []
        }
    },
    mounted() {
        this.getLatestDirections()
        this.getSpecialists()
        document.title = 'Log In | Djackets'
    },
    methods: {

        async getSpecialists() {
            const directionID = 1
            this.$store.commit('setIsLoading', true)
            await axios.
                get(`/api/v1/direction-specialists/${directionID}/`)
                .then(response => {
                    this.latestSpecialists = response.data
                    console.log(this.latestSpecialists)
                })
                .catch(error => {
                    console.log(error)
                })
        
                this.$store.commit('setIsLoading', false)

        },

        async changeDirection(event) {
            const directionID = event.target.value
            this.$store.commit('setIsLoading', true)
            await axios.
                get(`/api/v1/direction-specialists/${directionID}/`)
                .then(response => {
                    this.latestSpecialists = response.data
                    console.log(this.latestSpecialists)
                })
                .catch(error => {
                    console.log(error)
                })
        
                this.$store.commit('setIsLoading', false)

        },

        async getLatestDirections() {
            this.$store.commit('setIsLoading', true)
            await axios.
            get('/api/v1/latest-directions/')
            .then(response => {
                this.latestDirections = response.data
                console.log(this.latestDirections)
            })
            .catch(error => {
                console.log(error)
            })
    
            this.$store.commit('setIsLoading', false)
        },
        async getLatestDirections() {
            this.$store.commit('setIsLoading', true)
            await axios.
            get('/api/v1/latest-directions/')
            .then(response => {
                this.latestDirections = response.data
                console.log(this.latestDirections)
            })
            .catch(error => {
                console.log(error)
            })
    
            this.$store.commit('setIsLoading', false)
        },
        async submitForm() {
            axios.defaults.headers.common["Authorization"] = ""

            localStorage.removeItem("token")

            const formData = {
                username: this.username,
                password: this.password,
                direction: this.direction
            }

            console.log(formData)
            
            await axios
                .post("/api/v1/token/login/", formData)
                .then(response => {
                    console.log(response)
                    const auth_token = response.data.auth_token

                    this.$store.commit('setToken', auth_token)
                    
                    axios.defaults.headers.common["Authorization"] = "Token " + auth_token

                    localStorage.setItem("token", auth_token)

                    const toPath = this.$route.query.to || '/'

                    this.$router.push(toPath)
                })
                .catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                    } else {
                        this.errors.push('Something went wrong. Please try again')
                        
                        console.log(JSON.stringify(error))
                    }
                })
        }
    }
}
</script>