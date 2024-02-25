$(document).ready(function () {
    let table = $('#staffDetailstable').DataTable({
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
            {"data":"password"},
            {"data":"roadnm"},
            {
                "data":"role",
                "searchable":false,
                "orderable":false,
            }
        ],
        columnDefs: [
            { targets: '_all', className: 'columns' }
        ],
    });

    const addModal = new bootstrap.Modal('#addModal', {
        keyboard: false,
        backdrop:'static',
      })

    $('#saveRowBtn').on('click', function() {
        addModal.hide()
        var rowData = {
            srno: table.rows().count() + 1,
            name: $('#name').val(),
            email: $('#email').val(),
            password: $('#password').val(),
            roadnm: $('#road').val(),
            role: $('#role').val()
        };
        console.table(rowdata);//perform dbms here 
        table.row.add(rowData).draw(false);
        $('#addForm')[0].reset();
    });
});