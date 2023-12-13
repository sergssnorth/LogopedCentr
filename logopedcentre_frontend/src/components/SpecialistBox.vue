<template>
    <div class="column is-3">
        <div class="box">
            <figure class="image mb-6">
                <img v-bind:src="specialist.get_image">
            </figure>
            <h3 class="is-size-4 title mb-2">{{ specialist.sname }} {{ specialist.name }} {{ specialist.tname }}</h3>
            <h2 class="is-size-5  mb-2">{{ specialist.phone }}</h2>
            <p>Работает в нашей компании с {{ specialist.date_added }}</p>
        </div>
    </div>
</template>

<script>

export default {
    name: 'SpecialistBox',
    props: {
        specialist: Object
    }

}
</script>

<style scoped>

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