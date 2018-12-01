var vueApp = new Vue({
    el = "#vue_app",
    data: {
        connpassApi:null
    },
    mounted: function() {
        axios.get('https://connpass.com/api/v1/event/?keyword=%E8%8B%B1%E8%AA%9E')
    })
    }
})