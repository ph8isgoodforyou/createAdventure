<template>
<div>
    <Header />
    <CreateCityComp />
    <Footer />
</div>
</template>

<script>
import Header from '../components/Header'
import Footer from '../components/Footer'
import CreateCityComp from '../components/CreateCityComp'
export default {
    name: 'CreateCity',
    components: {
        Header,
        Footer,
        CreateCityComp
    }
}
</script>

<style>

</style>
