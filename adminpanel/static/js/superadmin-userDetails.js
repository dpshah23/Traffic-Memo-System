$(document).ready(function () {
    let table = $('#userDetailstable').DataTable({
        lengthMenu: [10, 30, 50],
        paging:false,
        info:false,
        columns: [
            {
                "data":"srno",
                "searchable":false,
            },
            {"data":"name"},
            {"data":"email"},
            {"data":"mobile"},
            {"data":"plateno"},
        ],
        columnDefs: [
            { targets: '_all', className: 'columns' }
        ],
    });
});