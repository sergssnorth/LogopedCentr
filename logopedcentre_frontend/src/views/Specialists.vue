<template>
    <div class="home">
    
      <div class="columns is-multiline">
        <div class="column is-12">
          <h2 class="is-size-3 has-text-centered">Наши специалисты:</h2>
        </div>
        
        <SpecialistBox
          v-for="specialist in latestSpecialists"
          v-bind:key = "specialist.id"
          v-bind:specialist = "specialist" />

      </div>
    </div>
  </template>
  
  <script>
  import moment from 'moment'
  import axios from 'axios'
  import SpecialistBox from '@/components/SpecialistBox.vue'

  export default {
    name: 'Specialist',
    data() {
      return {
        latestSpecialists: []
      }
    },
    components: {
        SpecialistBox
    },
    async mounted() {
      await this.getLatestSpecialist()
      await this.correctingTime()
      document.title = 'Специалисты | Logoped'
    },
    methods: {
      async getLatestSpecialist() {
        this.$store.commit('setIsLoading', true)

        await axios.
          get('/api/v1/latest-specialists/')
          .then(response => {
            this.latestSpecialists = response.data
            console.log
          })
          .catch(error => {
            console.log(error)
          })
  
        this.$store.commit('setIsLoading', false)
      },
      async correctingTime() {   
        this.latestSpecialists.forEach((item, index, array) => {
                item.date_added = moment(item.date_added).utc().format('YYYY-MM-DD')
            });
      }
    }
  }
  </script>