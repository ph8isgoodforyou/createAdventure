<template>
<div>
    <Header />
    <RegisterComp />
    <Footer />
</div>
</template>

<script>
import Header from '../components/Header'
import Footer from '../components/Footer'
import RegisterComp from '../components/RegisterComp'

export default {
    name: 'Register',
    components: {
        Header,
        Footer,
        RegisterComp
    }
}
</script>

<style>

</style>
