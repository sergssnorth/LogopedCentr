<template>
    <div class="page-my-account">
        <div class="columns is-multiline is-centered">
            <div class="column is-6">
                <template v-if="accountInformationFilled">
                    <form @change="formEditUpdated" @submit.prevent="submitForm" class="box">
                        <h1 class="is-size-3 has-text-centered mb-3">Профиль:</h1>

                        <div class="field">
                            <label class="label">Фамилия</label>
                            <div class="control">
                                <input class="input" type="text" v-model="accountInformation.sname">
                            </div>
                        </div>

                        <div class="field">
                            <label class="label">Имя</label>
                            <div class="control">
                            <input class="input" type="text" v-model="accountInformation.name">
                            </div>
                        </div>

                        <div class="field">
                            <label class="label">Отчество</label>
                            <div class="control">
                            <input class="input" type="text" v-model="accountInformation.tname">
                            </div>
                        </div>

                        <div class="field">
                            <label class="label">Телефон</label>
                            <div class="control">
                            <input class="input" type="text" v-model="accountInformation.phone">
                            </div>
                        </div>

                        <div class="field">
                            <label class="label">Паспорт</label>
                            <div class="control">
                            <input class="input" type="text" v-model="accountInformation.passport">
                            </div>
                        </div>
                        
                        
                        <button class="button is-info mt-3" @click="editFormAccountInfo" :disabled ='isEditUpdatedDisabled'>Изменить</button>

                        <div class="notification is-danger" v-if="errors.length">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>

                    </form>
                </template>
                <template v-else>
                    <form @change="formAddUpdated" @submit.prevent="submitForm" class="box">
                        <h1 class="is-size-3 has-text-centered mb-3">Профиль:</h1>

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
                            <label class="label">Паспорт</label>
                            <div class="control">
                            <input class="input" type="text" placeholder="4225231221324221" v-model="accountInformation.passport">
                            </div>
                        </div>

                        <div class="field is-grouped">
                            <div class="control">
                                <button class="button is-success mt-3" @click="saveFormAccountInfo" :disabled ='isAddUpdatedDisabled'>Добавить информацию</button>
                            </div>
                        </div>

                        <div class="notification is-danger" v-if="errors.length">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>

                    </form>
                </template>
            </div>
            

            <div class="column is-6">
                <template v-if="showFieldAddChildren">
                    <div class="box">
                        <h1 class="is-size-3 has-text-centered mb-3">Мои дети:</h1>
                        <form @change="formCreateChildrenUpdated" @submit.prevent="submitForm" class="box">
                            <div class="field">
                                <label class="label">Фамилия</label>
                                <div class="control">
                                    <input class="input" type="text" v-model="childrenInformation.sname">
                                </div>
                            </div>

                            <div class="field">
                                <label class="label">Имя</label>
                                <div class="control">
                                <input class="input" type="text" v-model="childrenInformation.name">
                                </div>
                            </div>

                            <div class="field">
                                <label class="label">Отчество</label>
                                <div class="control">
                                <input class="input" type="text" v-model="childrenInformation.tname">
                                </div>
                            </div>

                            <div class="field">
                                <label class="label">№ полиса ОМС</label>
                                <div class="control">
                                <input class="input" type="text" v-model="childrenInformation.oms">
                                </div>
                            </div>

                            <div class="field">
                                <label class="label">№ СНИЛС</label>
                                <div class="control">
                                <input class="input" type="text" v-model="childrenInformation.snils">
                                </div>
                            </div>

                            <div class="field">
                                <label class="label">№ Свидетельства о рождении</label>
                                <div class="control">
                                <input class="input" type="text" v-model="childrenInformation.svidetelstvo">
                                </div>
                            </div>
                            
                            <button class="button is-success mt-3" @click="saveFormCreateChildrenInfo" :disabled ='isCreateChildrenUpdatedDisabled'>Сохранить</button>
                            <button class="button is-normal is-danger is-light ml-3 mt-3" @click="closeFormChildren">
                                    <font-awesome-icon icon="fa-solid fa-minus" />
                            </button>
                            <div class="notification is-danger" v-if="errors.length">
                                <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                            </div>
                        </form>
                    </div>
                </template>
                <template v-else>
                    <div class="box">
                        <form @submit.prevent="submitForm">
                            <h1 class="is-size-3 has-text-centered mb-3">Мои дети:</h1>
                            <div class="box" v-for="children in all_childrens" :key="children.id">
                                <div class="columns">

                                        <div class="column is-11">
                                            <p><strong>ФИО:</strong> {{ children.name }} {{ children.sname }} {{ children.tname }}</p>
                                            <p><strong>№ полиса ОМС:</strong> {{ children.oms }}</p>
                                            <p><strong>№ СНИЛС:</strong> {{ children.snils }}</p>
                                            <p><strong>№ Свидетельства о рождении:</strong> {{ children.svidetelstvo }}</p>
                                        </div>
                                        <div class="column is-1">
                                            <button class="button is-normal is-danger is-light" @click="deleteChildren(children.id)">
                                                <font-awesome-icon icon="fa-solid fa-trash" />
                                            </button>
                                        </div>
                                
                                </div>
                            </div>
    

                        
                            <button class="button is-normal is-success" @click="addFormChildren">
                                    <font-awesome-icon icon="fa-solid fa-plus" />
                            </button>
                        </form>
                    </div>
                </template>
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
import DirectionBox from '@/components/DirectionBox.vue'



export default {
    name: 'MyAccount',
    components: {
        DirectionBox
    },
    data() {
        return {
            user_id: 0,
            form_edit_updated: false,
            form_add_updated: false,

            errors: [],

            accountInformation: {
                name: '',
                sname: '',
                tname: '',
                phone: '',
                passport: '',
                
            },
            accountInformationFilled: false,

            ////////////////////////////////////
            showFieldAddChildren: false,
            childrenInformation: {
                name: '',
                sname: '',
                tname: '',
                oms: '',
                snils: '',
                svidetelstvo: '',
            },
            all_childrens: [],
            form_create_children_updated: false,

            childrenInformationFilled: false,
        }
    },
    async mounted() {
        document.title = 'Мой аккаунт | Logoped'
        await this.getUserId()
        await this.getMyInformation()
        await this.getMyChildren()
        //console.log(this.user_id)
        //console.log(this.accountInformation)
        //console.log(this.accountInformationFilled)
    },
    computed: {
        isEditUpdatedDisabled(){
    	    return !this.form_edit_updated;
        },
        isAddUpdatedDisabled(){
    	    return !this.form_add_updated;
        },
        isCreateChildrenUpdatedDisabled(){
    	    return !this.form_create_children_updated;
        },

    },
    methods: {
        errorCheckAddAccountInformation() {
            this.errors = []

            if (this.accountInformation.name === '') {
                this.errors.push('Поле "Имя" пустое!')
                this.form_add_updated = false
            }

            if (this.accountInformation.sname === '') {
                this.errors.push('Поле "Фамилия" пустое!')
                this.form_add_updated = false
            }

            if (this.accountInformation.tname === '') {
                this.errors.push('Поле "Отчество" пустое!')
                this.form_add_updated = false
            }

            if (this.accountInformation.phone === '') {
                this.errors.push('Поле "Телефон" пустое!')
                this.form_add_updated = false
            }

            if (this.accountInformation.passport === '') {
                this.errors.push('Поле "Паспорт" пустое!')
                this.form_add_updated = false
            }
        },

        errorCheckAddChildrenInformation() {
            this.errors = []

            if (this.childrenInformation.name === '') {
                this.errors.push('Поле "Имя" пустое!')
                this.form_create_children_updated = false
            }

            if (this.childrenInformation.sname === '') {
                this.errors.push('Поле "Фамилия" пустое!')
                this.form_create_children_updated = false
            }

            if (this.childrenInformation.tname === '') {
                this.errors.push('Поле "Отчество" пустое!')
                this.form_create_children_updated = false
            }

            if (this.childrenInformation.oms === '') {
                this.errors.push('Поле "Телефон" пустое!')
                this.form_create_children_updated = false
            }

            if (this.childrenInformation.snils === '') {
                this.errors.push('Поле "Паспорт" пустое!')
                this.form_create_children_updated = false
            }

            if (this.childrenInformation.svidetelstvo === '') {
                this.errors.push('Поле "Паспорт" пустое!')
                this.form_create_children_updated = false
            }
        },

        formEditUpdated () {
            this.form_edit_updated = true
            console.log(this.accountInformation)
        },
        formCreateChildrenUpdated () {
            this.form_create_children_updated = true
            console.log(this.childrenInformation)
        }, 
        formAddUpdated () {
            this.form_add_updated = true
            console.log(this.accountInformation)
            console.log(this.form_add_updated)
        },
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

        async editFormAccountInfo() {
            this.errorCheckAddAccountInformation()
            if (!this.errors.length) {
                this.$store.commit('setIsLoading', true)

                this.accountInformation.user_id = this.user_id
                await axios
                    .post('/api/v1/account/edit_info/', {'query' : this.accountInformation})
                    .then(response => {
                        this.form_edit_updated = false
                        console.log("Изменил")
                    })
                    .catch(error => {
                        console.log(error)
                    })

                this.$store.commit('setIsLoading', false)
            }
        },

        async saveFormAccountInfo() {   
            this.errorCheckAddAccountInformation()
            if (!this.errors.length) {
                this.$store.commit('setIsLoading', true)

                this.accountInformation.user_id = this.user_id
                await axios
                    .post('/api/v1/account/add_info/', {'query' : this.accountInformation})
                    .then(response => {
                        this.form_edit_updated = false
                    })
                    .catch(error => {
                        console.log(error)
                    })

                this.$store.commit('setIsLoading', false)
            }
        },

        async saveFormCreateChildrenInfo() {   
            this.errorCheckAddChildrenInformation()
            if (!this.errors.length) {
                this.$store.commit('setIsLoading', true)

                this.childrenInformation.user_id = this.user_id
                await axios
                    .post('/api/v1/account/add_children/', {'query' : this.childrenInformation})
                    .then(response => {
                        this.form_create_children_updated = false
                        this.showFieldAddChildren = false
                    })
                    .catch(error => {
                        console.log(error)
                    })
                
                await this.getMyChildren()
                this.$store.commit('setIsLoading', false)
                
            }
        },
        async deleteChildren(children_id) {   
           console.log(children_id)
           const deleteForm = {};
           deleteForm.user_id = this.user_id
           deleteForm.children_id = children_id

           this.$store.commit('setIsLoading', true)

            await axios
                .post('/api/v1/account/delete_children/', {'query' : deleteForm})
                .then(response => {
                    console.log('delete')
                    let index = this.all_childrens.indexOf('green');
                    
                })
                .catch(error => {
                    console.log(error)
                })
            
            await this.getMyChildren()

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
                        this.all_childrens = []
                    }
                    else {
                        this.all_childrens = response.data
                    }
                    
                })
                .catch(error => {
                    console.log(error)
                })
            this.$store.commit('setIsLoading', false)
        },

        async addFormChildren() {
            this.showFieldAddChildren = true
        },

        async closeFormChildren() {
            this.showFieldAddChildren = false
            console.log(this.showFieldAddChildren)
        },

        logout() {
            axios.defaults.headers.common["Authorization"] = ""
            localStorage.removeItem("token")
            localStorage.removeItem("username")
            localStorage.removeItem("userid")
            this.$store.commit('removeToken') 
            this.$router.push('/')
        },

    }
}
</script>