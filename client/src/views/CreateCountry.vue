<template>
<div>
    <Header />
    <CreateCountryComp />
    <Footer />
</div>
</template>

<script>
import Header from '../components/Header'
import Footer from '../components/Footer'
import CreateCountryComp from '../components/CreateCountryComp'
export default {
    name: 'CreateCountry',
    components: {
        Header,
        Footer,
        CreateCountryComp
    }
}
</script>

<style>

</style>
