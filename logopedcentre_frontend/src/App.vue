<template>
  <div id="wrapper">
    <nav class="navbar is-spaced is-size-5">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item">
          <img src="@/assets/logoped12.jpg" width="112" height="">
        </router-link>
        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-targer="navbar-menu" @click="showMobileMenu =!showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">
        <div class="navbar-start">
          <div class="navbar-item">
            <form method="get" action="/search">
              <div class="field has-addons">
                <div class="control">
                  <input type="text" class="input" placeholder="Фамилия Имя Отчество" name="query">
                </div>

                <div class="control">
                  <button class="button is-info">
                      <span class="icon">
                        <font-awesome-icon icon="fa-solid fa-magnifying-glass" />
                      </span>
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>
        <div class="navbar-end">
          <router-link to="/records" class="navbar-item">Запись</router-link>
          <router-link to="/directions" class="navbar-item">Направления работы</router-link>
          <router-link to="/specialists" class="navbar-item">Специалисты</router-link>
          <router-link to="/about-us" class="navbar-item">О нас</router-link>

          <div class="navbar-item">
            <div class="buttons">
              
              <template v-if="$store.state.isAuthenticated">
                <router-link to="/my-account" class="button is-light">Мой аккаунт</router-link>
                <router-link to="/my-records" class="button is-info">
                  <span>Мои записи</span>
                </router-link>
              </template>

              <template v-else>
                <router-link to="/log-in" class="button is-outlined is-info"><span>Вход</span></router-link>
                <router-link to="/sign-up" class="button is-outlined is-success"><span>Регистрация</span></router-link>
              </template>
            </div>
          </div>
        </div>
      </div>
    </nav>
    
    <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading': $store.state.isLoading}">
      <div class="lds-dual-ring"></div>
    </div>

    <section class="section is-spaced">
      <router-view/>
    </section>
    
  </div>
</template>


<script>
import axios from 'axios'


export default{
  data() {
    return {
      showMobileMenu: false,
      cart: {
        items: []
      }
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')
    
    const token = this.$store.state.token

    if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
        axios.defaults.headers.common['Authorization'] = ""
    }
  },
  mounted() {
    this.cart = this.$store.state.cart
  },
  computed: {
    cartTotalLength() {
      let totalLength = 0

      for (let i = 0; i < this.cart.items.length; i++) {
        totalLength += this.cart.items[i].quantity
      }

      return totalLength
      
    }
  }
}
</script>
<style lang="scss">
@import '../node_modules/bulma';
.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.is-loading-bar {
  height: 0;
  overflow: hidden;

  -webkit-transition: all 0.3s;
  transition: all 0.3s;

  &.is-loading {
    height: 80px;
  }
}
* {
  margin: 0;
  padding: 0;
}

</style>