<template>
    <div class="home">
    
      <div class="columns is-multiline">
        <div class="column is-12">
          <h2 class="is-size-3 has-text-centered">Направления работы:</h2>
        </div>
        
        <DirectionBox
          v-for="direction in latestDirections"
          v-bind:key = "direction.id"
          v-bind:direction = "direction" />
  
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  import DirectionBox from '@/components/DirectionBox.vue'
  
  export default {
    name: 'Direction',
    data() {
      return {
        latestDirections: []
      }
    },
    components: {
        DirectionBox
    },
    mounted() {
      this.getLatestDirections()
      document.title = 'Направления работы | Logoped'
    },
    methods: {
      async getLatestDirections() {
        this.$store.commit('setIsLoading', true)
        await axios.
          get('/api/v1/latest-directions/')
          .then(response => {
            this.latestDirections = response.data
            console.log
          })
          .catch(error => {
            console.log(error)
          })
  
        this.$store.commit('setIsLoading', false)
      }
    } 
  }
  </script>