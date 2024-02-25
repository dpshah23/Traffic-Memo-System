$(document).ready(function () {
    let table = $('#memoTable').DataTable({
        lengthMenu: [10, 30, 50],
        columns: [
            {
                "data": "srno",
                "searchable": false,
                "orderable": false,
            },
            { "data": "memos" },
            {
                "data": "imageLink",
                "searchable": false,
                "orderable": false,
            },
            {
                "data": "pdfLink",
                "searchable": false,
                "orderable": false,
            },
            { "data": "roadName" },
            { "data": "fine" },
            { "data": "name" },
            { "data": "plateNo" },
            { "data": "dateAndTime" },
        ],
        columnDefs: [
            {
                targets: '_all',
                className: 'columns'
            }
        ],
        order: [[1, 'asc']]
    });

    async function load () {  

        var urlParams = new URLSearchParams(window.location.search);
        await $('#roadwayFilter').val(urlParams.get('roadwayFilter'));
        await $('#vehicleTypeFilter').val(urlParams.get('vehicleTypeFilter'));
        await $('#namePlateFilter').val(urlParams.get('namePlateFilter'));
        await $('#roadwayFilter').click();
    }
    load()

    $('#roadwayFilter, #vehicleTypeFilter, #namePlateFilter').on('click change input', function () {
        console.log("erer");
        var roadwayFilterValue = $('#roadwayFilter').val();
        var vehicleTypeFilterValue = $('#vehicleTypeFilter').val();
        var namePlateFilterValue = $('#namePlateFilter').val().toLowerCase();

        table.columns(4).search(roadwayFilterValue);
        table.columns(1).search(vehicleTypeFilterValue);
        table.columns(7).search(namePlateFilterValue, true, false).draw();

        // Update URL with new filter values
        var params = {
            roadwayFilter: roadwayFilterValue,
            vehicleTypeFilter: vehicleTypeFilterValue,
            namePlateFilter: namePlateFilterValue
        };
        var newUrl = window.location.pathname + '?' + $.param(params);
        window.history.replaceState({}, '', newUrl);
    });

/*
    fetch('MOCK_DATA.json')
            .then(response => response.json())
            .then(data => {
                const tableBody = document.getElementById('tableBody');
                data.forEach(item => {
                    const row = document.createElement('tr');
                    row.innerHTML = `
                        <td>${item.dateandtime}</td>
                        <td>${item.email}</td>
                        <td>${item.fine}</td>
                        <td><a href=${item.imageurl} >${truncateString(item.imageurl, 10)}</a></td>
                        <td>${item.name}</td>
                        <td><a href=${item.pdfurl} >${truncateString(item.imageurl, 10)}</a></td>
                        <td>${item.plateno}</td>
                        <td>${item.roadnm}</td>
                    `;
                    tableBody.appendChild(row);
                });
            });*/
});
/* 
Memos
    Image link
    Pdf link
    Road name
    Fine.
    Name
    Plate no
    Date and time
*/