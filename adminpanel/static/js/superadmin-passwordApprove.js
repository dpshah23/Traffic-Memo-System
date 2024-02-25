$(document).ready(function () {
    let table = $('#passwordApproveTable').DataTable({
        lengthMenu: [10, 30, 50],
        // searching:"false",
        searching:false,
        paging:false,
        info:false,
        columns: [
            {
                "data":"srno",
                "orderable": false,
            },
            {"data":"username"},
            {
                "data":"oldPassword",
                "orderable": false,
            },
            {
                "data":"newPassword",
                "orderable": false,
            },
            {"data":"requestedOn"},
            {
                "data":"action",
                "orderable": false,
            },
        ],
        columnDefs: [
            { targets: '_all', className: 'columns' }
        ],
        order: [[1, 'asc']]
    });

    const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
    const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))

    $('#passwordApproveTable').on('dblclick', '.fa-check', function () {
        let rowData = table.row($(this).closest('tr')).data();
        let message = {
            "approved":true,
            "row":rowData
        }
        console.log(message);
        //perform dbms here
        table.row($(this).closest('tr')).remove().draw(false);
    });

    $('#passwordApproveTable').on('dblclick', '.fa-xmark', function () {
        let rowData = table.row($(this).closest('tr')).data();
        let message = {
            "approved":false,
            "row":rowData
        }
        console.log(message);
        //perform dbms here
        table.row($(this).closest('tr')).remove().draw(false);
    });
});