<template>
    <div class="column is-3">
        <div class="box">
            <h3 class="is-size-4 title mb-3">{{ direction.name }}</h3>
            <li v-for="direction_point in direction.directionpoints">
                {{ direction_point.description }}
            </li>
            <router-link  v-bind:to="direction.get_absolute_url" class="button is-info is-outlined">Посмотреть специалистов</router-link>
        </div>
    </div>
</template>

<script>
export default {
    name: 'DirectionBox',
    props: {
        direction: Object
    }
}
</script>

<style scoped>

.button.is-info.is-outlined{
    margin-top: 30px; 
}
.box {
    height: 100%;
    display: flex;
    justify-content: space-between;
    flex-direction: column;
}
  .image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
</style>