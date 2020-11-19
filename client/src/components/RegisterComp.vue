<template>
<div class="register-container">
    <div class="inner-register-container">
        <div class="register-box">
            <form @submit.prevent="registerUser" method="post">
                <h2>Sign In</h2>
                <input v-model="user.username" id="username" type="text" placeholder="Username" onfocus="placeholder=''" onblur="placeholder='Username'">
                <input v-model="user.email" id="email" type="email" placeholder="Email" onfocus="placeholder=''" onblur="placeholder='Email'">
                <input v-model="user.password" id="password" type="password" placeholder="Password" onfocus="placeholder=''" onblur="placeholder='Password'">
                <input v-model="user.password2" id="password2" type="password" placeholder="Repeat Password" onfocus="placeholder=''" onblur="placeholder='Repeat Password'">
                <input class="register-btn" type="submit" value="Sign In">
                <p>Already a <span>member</span> yet?</p>
                <a v-on:click="$router.push({ path: `/login/` } )">Log In</a>
            </form>
        </div>
    </div>
</div>
</template>

<script>
import {
    getAPI
} from '../axios-api'

export default {
    name: 'RegisterComp',
    data() {
        return {
            user: {
                username: '',
                email: '',
                password: '',
                password2: ''
            }
        };
    },
    methods: {
        registerUser() {
            getAPI.post('/register/',
                    this.user
                )
                .then(
                    this.$router.push({
                        path: `/login/`
                    })
                )
                .catch((err) => {
                    console.log(err);
                })

        },
    }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Lato:wght@300;400&family=Poppins:wght@200;400&display=swap');

/*
        font-family: 'Lato', sans-serif;
        font-family: 'Poppins', sans-serif;
        */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

.register-container {
    font-family: 'Poppins', sans-serif;
    background: url('../assets/img/login-img.jpg') no-repeat center;
    background-size: cover;
    color: white;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

.inner-register-container {
    /*max-width: 80%;
        max-height: 80%;
        margin: 50px;*/
}

.register-box {
    background-color: rgba(0, 0, 0, 0.8);
    /*box-shadow: 0 0 15px 6px rgb(16, 102, 48);*/
    /*opacity: 0.8;*/
    width: 45vh;
    height: auto;
    width: auto;
    border-radius: 50px;
}

form {
    display: grid;
    flex-direction: column;
    align-items: center;
    padding: 30px;
}

form h2 {
    font-size: 30px;
    font-weight: 100;
    margin-bottom: 10px;
    letter-spacing: 5px;
}

form input {
    width: 250px;
    height: 30px;
    border: none;
    margin: 20px;
    padding: 20px;
    border-radius: 12px;
}

form input:focus {
    background-color: rgb(16, 102, 48);
    color: white;
}

::placeholder {
    font-size: 15px;
    font-weight: 100;
}

form .register-btn {
    padding: 0;
    background-color: rgb(144, 255, 183);
    font-size: 18px;
}

form .register-btn:hover {
    background-color: rgb(16, 102, 48);
    color: white;
}

form p {
    font-size: 15px;
    font-weight: 150;
    margin-top: 10px;
    margin-bottom: 10px;
    letter-spacing: 2px;
}

form p span {
    color: rgb(144, 255, 183);
}

form a {
    background-color: rgb(16, 102, 48);
    color: black;
    text-decoration: none;
    cursor: pointer;
    border: 1px solid;
    border-radius: 12px;
    width: 250px;
    height: 30px;
    text-align: center;
    padding-top: 3px;
}

form a:hover {
    background-color: rgb(218, 175, 110);
    color: black;
}

@media (max-width: 380px) {
    .register-box {
        width: 40vh;
    }

    form input {
        width: 200px;
        height: 30px;
        margin: 10px;
        padding: 10px;
    }

    form a {
        width: 200px;
        height: 30px;
        margin: 10px;
        padding: 5px;
    }
}
</style>
