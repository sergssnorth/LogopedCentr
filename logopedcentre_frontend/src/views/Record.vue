<template>
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h2 class="is-size-3 has-text-centered mb-5">Запись на прием:</h2>
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label class="label">Фамилия</label>
                        <div class="control">
                            <input class="input" type="text" placeholder="Тюрин" v-model="accountInformation.sname">
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Имя</label>
                        <div class="control">
                            <input class="input" type="text" placeholder="Сергей" v-model="accountInformation.name">
                        </div>
                    </div>


                    <div class="field">
                        <label class="label">Отчество</label>
                        <div class="control">
                            <input class="input" type="text" placeholder="Сергеевич" v-model="accountInformation.tname">
                        </div>
                    </div>
                    
                    <div class="field">
                        <label class="label">Телефон</label>
                        <div class="control">
                            <input class="input" type="text" placeholder="89115926942" v-model="accountInformation.phone">
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Ребенок</label>
                        <div class="control">
                            <div class="select">
                                <select @change="changeDirection" v-model="selectedChildren">
                                    <option v-for="option in latestChildren" :value="option.id">
                                    {{ option.sname }} {{ option.name }} {{ option.tname }}
                                    </option>
                                </select>
                            </div>
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Направление работы</label>
                        <div class="control">
                            <div class="select">
                                <select @change="changeDirection" v-model="selectedDirections">
                                    <option v-for="option in latestDirections" :value="option.slug">
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
                                <select @change="changeSpecialist" v-model="selectedSpecialist">
                                    <option v-for="option in latestSpecialists" :value="option.id">
                                    {{option.name}} {{option.sname}} {{option.tname}}
                                    </option>
                                </select>
                            </div>
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Дата и время</label>
                            <div class="control">
                                    <div class="select">
                                        <select v-model="selectedSpecialistSheduleDate">
                                            <option v-for="option in latestSpecialistShedule" :value="option.id">
                                            {{option.date}} {{option.time}}
                                            </option>
                                        </select>
                                    </div>
                            </div>
                    </div>
                    

                    <div class="field">
                    <label class="label">Комментарий:</label>
                    <div class="control">
                        <textarea class="textarea" placeholder="" v-model="comment"></textarea>
                    </div>
                    </div>

                    <div class="field is-grouped">
                    <div class="control">
                        <button class="button is-link">Записаться</button>
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
            user_id: 0,
            accountInformation: {
                name: '',
                sname: '',
                tname: '',
                phone: '',
            },

            all_childrens: [],

            isActiveFirstField: false,
            isActiveSecondField: false,

            selectedDirections: ref('1'),
            latestDirections: ref([]),

            selectedChildren: ref('1'),
            latestChildren: ref([]),

            selectedSpecialistSheduleDate: ref('1'),
            latestSpecialistShedule: ref([]),

            specialistDate: [],
            
            selectedSpecialist: '',
            latestSpecialists: ref([]),

            comment: '',
            errors: []
        }
    },
    async mounted() {
        document.title = 'Logoped'
        await this.getLatestDirections()
        await this.getSpecialists()
        console.log()
        await this.getUserId()
        await this.getMyInformation()
        await this.getMyChildren()

        
    },
    methods: {
        async getUserId() {
            this.$store.commit('setIsLoading', true)
            const token = this.$store.state.token
            await axios
                .get(`/api/v1/get_user_id/${token}/`)
                .then(response => {
                    this.user_id = response.data[0].user_id
                })
                .catch(error => {
                    console.log(error)
                })
            this.$store.commit('setIsLoading', false)
        },

        async getSpecialists() {
            const direction_slug = 'logoped'
            this.$store.commit('setIsLoading', true)
            await axios.
                get(`/api/v1/direction-specialists/${direction_slug}/`)
                .then(response => {
                    this.latestSpecialists = response.data
                    console.log(`getSpecialists ${this.latestSpecialists}`)
                })
                .catch(error => {
                    console.log(error)
                })
        
                this.$store.commit('setIsLoading', false)

        },

        async getSpecialistsSheduleDate() {
            const specialist_id = '1'
            this.$store.commit('setIsLoading', true)
            await axios.
                get(`/api/v1/direction-specialists/${specialist_id}/`)
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
            const direction_slug = event.target.value
            this.$store.commit('setIsLoading', true)
            await axios.
                get(`/api/v1/direction-specialists/${direction_slug}/`)
                .then(response => {
                    this.latestSpecialists = response.data
                    console.log(this.latestSpecialists)
                })
                .catch(error => {
                    console.log(error)
                })
        
                this.$store.commit('setIsLoading', false)

        },

        async changeSpecialist(event) {
            const specialist_id = event.target.value
            this.$store.commit('setIsLoading', true)
            await axios.
                get(`/api/v1/specialist/get_shedule/${specialist_id}/`)
                .then(response => {
                    this.latestSpecialistShedule = response.data
                    console.log(this.latestSpecialistShedule)
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
        async getMyInformation() {
            this.$store.commit('setIsLoading', true)
            await axios
                .get(`/api/v1/account/${this.user_id}/info/`)
                .then(response => {
                    if (response.data.length == 0) {
                        this.accountInformationFilled = false
                    }
                    else {
                        this.accountInformationFilled = true
                        this.accountInformation = response.data[0]
                    }
                    
                })
                .catch(error => {
                    console.log(error)
                })
            this.$store.commit('setIsLoading', false)
        },

        async getMyChildren() {
            this.$store.commit('setIsLoading', true)
            await axios
                .get(`/api/v1/account/${this.user_id}/children_info/`)
                .then(response => {
                    if (response.data.length == 0) {
                        this.latestChildren = []
                    }
                    else {
                        this.latestChildren = response.data
                    }
                    
                })
                .catch(error => {
                    console.log(error)
                })
            this.$store.commit('setIsLoading', false)
        },

        async submitForm() {
            console.log(this.selectedSpecialistSheduleDate)
            console.log(this.selectedDirections)
            const formData = {
                user_id: this.user_id, 
                // sname: this.accountInformation.sname,
                // name: this.accountInformation.name,
                // tname: this.accountInformation.tname,
                children_id: Number(this.selectedChildren),
                direction_slug: this.selectedDirections,
                specialist_id: Number(this.selectedSpecialist),
                datetime: this.selectedSpecialistSheduleDate,
                comment: this.comment,
                record_slug: 'in-processing'
            }

            console.log(formData)
            
            await axios
                .post("/api/v1/record/add_record_children/", {'query' : formData})
                .then(response => {
                    console.log(response)
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