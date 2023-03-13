import {createStore} from 'vuex'

export default createStore({

    state: {
        token: '',
        isAuthenticated: false,
        username : ''
    },
    mutations: {
        initializedStore(state){
            if(localStorage.getItem('token'))
            {
                state.token = localStorage.getItem('token')
                state.username = localStorage.getItem('username')
                state.isAuthenticated = true;
            }
            else{
                state.token = ''
                state.username = ''
                state.isAuthenticated = false;
            }
        },
        setToken(state, token, username)
        {
            state.token = token
            state.username = username
            state.isAuthenticated = true
        },
        removeToken(state)
        {
            state.token =''
            state.username =''
            state.isAuthenticated = false
        }
    },
    actions: {

    },
    modules: {

    }


})