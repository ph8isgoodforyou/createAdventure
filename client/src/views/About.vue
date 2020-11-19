<template>
<div>
    <Header />
    <AboutSection />
    <Footer />
</div>
</template>

<script>
import Header from '../components/Header'
import Footer from '../components/Footer'
import AboutSection from '../components/AboutSection'

export default {
    name: 'About',
    components: {
        AboutSection,
        Footer,
        Header,
    }
}
</script>

<style>

</style>
