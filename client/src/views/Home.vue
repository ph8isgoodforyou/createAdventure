<template>
<div>
    <Header />
    <Intro v-if="accessToken==null"/>
    <GreetingUser v-if="accessToken!=null"/>
    <AboutSection v-if="accessToken==null"/>
    <ContactSection v-if="accessToken==null"/>
    <Footer />
</div>
</template>

<script>
// @ is an alias to /src
import Header from '../components/Header'
import Intro from '../components/Intro'
import AboutSection from '../components/AboutSection'
import ContactSection from '../components/ContactSection'
import Footer from '../components/Footer'
import GreetingUser from "@/components/GreetingUser"
import {
    mapState
} from 'vuex'
export default {
    name: 'Home',
    computed: mapState(['accessToken']),
    components: {
        GreetingUser,
        ContactSection,
        AboutSection,
        Intro,
        Footer,
        Header,
    }
}
</script>
