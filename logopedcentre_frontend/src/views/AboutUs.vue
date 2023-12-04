<template>
    <div class="columns is-multiline">
        <div class="column is-12">
          <h2 class="is-size-3 has-text-centered">О нас:</h2>
        </div>
    </div>
    <div class="box">
        <div class="content is-normal">
            <h1>Логопедический центр "Logoped"</h1>
            <p>Комплексная психолого-педагогическая работа логопедов, дефектологов, психологов, педагогов, нейропсихологов.</p>
            <h2>О нас</h2>
            <ul>
                <li>Логопедический центр «Речевик» функционирует с 2012 года.</li>
                <li>На сегодняшний день в центре представлена комплексная психолого-педагогическая работа специалистов: логопедов, дефектологов, психологов, педагогов, нейропсихологов.</li>
                <li>В Центре «Речевик» ежемесячно обучаются больше 150 детей, регулярно на психолого-педагогическую реабилитацию приезжают иногородние семьи.</li>
                <li>Среди воспитанников центра 50% нормотипичные дети с речевыми нарушениями, а также 50% дети с ОВЗ</li>
            </ul>
        </div>
    </div>
    <div class="columns is-multiline">
        <div class="column is-6">
            <form class="box">
                <div class="content is-normal">
                    <h3>Запись на консультацию</h3>
                </div>    
                <div class="field">
                    <label class="label">Телефон</label>
                    <div class="control">
                        <input class="input" type="" placeholder="89115926942">
                    </div>
                </div>

                <div class="field">
                    <label class="label">Пароль</label>
                    <div class="control">
                    <input class="input" type="password" placeholder="Сергей">
                    </div>
                </div>

                <button class="button is-primary">Отправить заявку</button>
            </form>
        </div>
    </div>
</template>

<script>

export default {
  name: 'AboutUs',
  data() {
    return {
        
    }
  },
  mounted() {
    document.title = 'О нас | Logoped'
  },
}
</script>

<style lang="scss">
@import '../../node_modules/bulma';

.box {
    border-radius: 15px;
}

.button {
    border-radius: 10px;
}
</style>