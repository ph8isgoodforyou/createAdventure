<template>
<div>
    <Header />
    <UpdateCityComp />
    <Footer />
</div>
</template>

<script>
import Header from '../components/Header'
import Footer from '../components/Footer'
import UpdateCityComp from '../components/UpdateCityComp'
export default {
    name: 'UpdateCity',
    components: {
        Header,
        Footer,
        UpdateCityComp
    }
}
</script>

<style>

</style>
