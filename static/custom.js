$(document).ready(function() { $('.datatable').dataTable({
  autoFill: true
}); });

$.datetimepicker.setDateFormatter({
        parseDate: function (date, format) {
            var d = moment(date, format);
            return d.isValid() ? d.toDate() : false;
        },
        formatDate: function (date, format) {
            return moment(date).format(format);
        },
    });

    $('.datetime').datetimepicker({
        format:'DD-MM-YYYY HH:mm',
        formatTime:'HH:mm',
        formatDate:'DD-MM-YYYY',
        useCurrent: true,
    });


const pusher = new Pusher('1a2e5fd5d91f28433d49', {
        cluster: 'ap2',
        encrypted: true
    });
var channel = pusher.subscribe('table');

channel.bind('new-record', (data) => {
        const time_in = moment(`${data.data.time_in}`, 'DD/MM/YYYY hh:mm a').format('YYYY-MM-DD hh:mm:ss a')

       $('#datatable').append(`
            <tr id="${data.data.id} ">
                <th scope="row"> ${data.data.customer} </th>
                <td> ${data.data.ride} </td>
                <td> ${time_in} </td>
            </tr>
       `)
    });

channel.bind('update-record', (data) => {
        const time_in = moment(`${data.data.time_in}`, 'DD/MM/YYYY hh:mm a').format('YYYY-MM-DD hh:mm:ss a')

        $(`#${data.data.id}`).empty()

        $(`#${data.data.id}`).html(`
          <th scope="row"> ${data.data.customer} </th>
          <td> ${data.data.ride} </td>
          <td> ${time_in} </td>
        `)
     });
