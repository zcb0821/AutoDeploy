import Vue from 'vue'
import ClusterManage from './cluster-manage.vue'
import Dropdown from './basic/dropdown.vue'


Vue.filter('array', {
    // model -> view
    // 在更新 `<input>` 元素之前格式化值
    read: function (val) {
        return val.join(',')
    },
    // view -> model
    // 在写回数据之前格式化值
    write: function (val, oldVal) {
        return val.split(',')
    }
})

Vue.filter('integer', {
    // model -> view
    // 在更新 `<input>` 元素之前格式化值
    read: function (val) {
        return val != null ? val.toString() : '请输入整数'
    },
    // view -> model
    // 在写回数据之前格式化值
    write: function (val, oldVal) {
        var val = parseInt(val)
        return isNaN(val) ? null : val
    }
})

new Vue({
    el: 'body',
    components: {ClusterManage, Dropdown},
    data: {
        options: [1, 2, 3],
        value: 1
    },
    watch: {
        value: function() {
            console.log(this.value)
        }
    }
})
