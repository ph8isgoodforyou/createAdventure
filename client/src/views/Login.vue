<template>
<div>
    <Header />
    <LoginComp />
    <Footer />
</div>
</template>

<script>
import Header from '../components/Header'
import Footer from '../components/Footer'
import LoginComp from '../components/LoginComp'
export default {
    name: 'Login',
    components: {
        Header,
        Footer,
        LoginComp
    }
}
</script>

<style>

</style>
