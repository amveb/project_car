new Vue({
        el: '#vueOrder',
        data: {
            services: [],
            selectedOrder: []
        },
    computed: {
              itog() {
                let result = 0;
                for (
                  var i = 0, _len = this.selectedOrder.length;
                  i < _len;
                  i++
                ) {
                  result += this.selectedOrder[i].price;
                }
                return result;
              }
            },
            methods: {
              changeOrder(service) {
                const findService = this.selectedOrder.find(
                  x => x.name === service.name
                );
                if (findService) {
                  this.selectedOrder.splice(
                    this.selectedOrder.indexOf(findService),
                    1
                  );
                } else {
                  this.selectedOrder.push(service);
                }
                console.log(this.selectedOrder);
              }
            },
        created: function () {
            const vm = this;
            axios.get('http://127.0.0.1:8000/api/services/?format=json')
                .then(function (response) {
                    vm.services = response.data
                    console.log(response.data)
                    console.log('Успешно')

                })
        }
    }
)

