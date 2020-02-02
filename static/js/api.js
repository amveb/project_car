new Vue({
        el: '#services_order',
        data: {
            message: 'Привет, Vue!!!!!',
            services: []
        },
        created: function () {
            const vm = this;
            axios.get('http://127.0.0.1:8000/api/services/?format=json')
                .then(function (response) {
                    vm.services = response.data
                    console.log(response.data)
                    console.log('Успешноооооо')

                })
        }
    }
)