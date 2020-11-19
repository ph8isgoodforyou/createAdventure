<template>
<div class="create-container">
    <div class="inner-create-container">
        <div class="create-box">
            <form @submit.prevent="updatePoint" method="post">
                <h2>Update Point Of Interest</h2>
                <div class="dash"></div>
                <input v-model="point.title" value="" id="title" type="text" placeholder="Title" onfocus="placeholder=''" onblur="placeholder='Title'" required>

                <input v-model="point.price" id="price" type="text" placeholder="Price" onfocus="placeholder=''" onblur="placeholder='Price'" required>

                <input v-model="point.work_hours" id="work_hours" type="text" placeholder="Working Hours" onfocus="placeholder=''" onblur="placeholder='Working Hours'" required>

                <div class="dash"></div>
                <input class="create-btn" type="submit" value="Add">
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
    name: 'UpdatePointOfInterestComp',
    data() {
        return {
            point: {
                title: '',
                price: '',
                work_hours: '',
            }
        };
    },
    mounted() {
        getAPI.get('/pointsOfInterest/' + this.$route.params.id, {
                headers: {
                    'Authorization': `Bearer ${this.$store.state.accessToken}`
                }
            })
            .then(response => {
                //console.log(response.data),
                this.point = response.data
            });
    },
    methods: {
        updatePoint() {
            getAPI.put(`/pointsOfInterest/${this.point.id}/`,
                    this.point, {
                        headers: {
                            'Authorization': `Bearer ${this.$store.state.accessToken}`
                        }
                    }
                )
                .then(
                    history.back(1)
                ).catch((err) => {
                    console.log(err);
                })
        }
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

.create-container {
    font-family: 'Poppins', sans-serif;
    background: url('../assets/img/pointOfInterest.jpg') no-repeat center;
    background-size: cover;
    color: white;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

.inner-create-container {
    width: auto;
    height: 100%;
    /*max-width: 80%;
            max-height: 80%;
            margin: 50px;*/
}

.create-box {
    background-color: rgba(0, 0, 0, 0.5);
    box-shadow: 0 0 15px 6px #34495e;
    /*opacity: 0.8;*/
    height: auto;
    width: auto;
    border-radius: 50px;
}

form {
    height: 100%;
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 30px;
}

form .dash {
    background-color: white;
    width: 100%;
    height: 5px;
    border: 2px solid rgb(98, 154, 206);
    border-radius: 12px;
    margin-top: 20px;
    margin-bottom: 20px;
}

form h2 {
    font-size: 25px;
    font-weight: 100;
    margin-bottom: 10px;
    padding: 20px;
    letter-spacing: 5px;
    text-align: center;
}

form input,
form select {
    width: 250px;
    height: 30px;
    border: none;
    margin: 20px;
    padding: 20px;
    border-radius: 12px;
}

form select {
    font-family: 'Poppins', sans-serif;
    color: black;
    padding: 0px;
    padding-left: 10px;
    height: 40px;
}

form select optgroup {
    font-family: 'Poppins', sans-serif;
}

form textarea {
    overflow: hidden;
    width: 540px;
    height: 90px;
    border: none;
    margin: 20px;
    padding: 20px;
    border-radius: 12px;
    line-height: 20px;
}

form input:focus,
form textarea:focus {
    background-color: rgb(24, 55, 85);
    color: white;
}

::placeholder {
    font-family: 'Poppins', sans-serif;
    font-size: 15px;
    font-weight: 100;
    color: black;
}

form .create-btn {
    background-color: rgb(98, 154, 206);
    color: white;
    margin: 0;
    padding: 0;
    float: right;
}

form .create-btn:hover {
    background-color: rgb(24, 55, 85);
    color: white;
}
</style>
