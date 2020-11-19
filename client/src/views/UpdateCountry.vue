<template>
<div>
    <Header />
    <UpdateCountryComp />
    <Footer />
</div>
</template>

<script>
import Header from '../components/Header'
import Footer from '../components/Footer'
import UpdateCountryComp from '../components/UpdateCountryComp'
export default {
    name: 'UpdateCountry',
    components: {
        Header,
        Footer,
        UpdateCountryComp
    }
}
</script>

<style>

</style>
