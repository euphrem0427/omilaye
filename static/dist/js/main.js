$(function() {
    "use strict";
    /** disable input until checkbox not checked */
    $('#checkSolaire').change(function () {
        $('#solaire').prop("disabled", !this.checked);
    }).change()

    $('#checkGroupe').change(function () {
        $('#groupe').prop("disabled", !this.checked);
    }).change()

    $('#checknouveau').change(function () {
        $('#nouveau').prop("disabled", !this.checked);
    }).change()

    $('#checkproduction').change(function () {
        $('#Production').prop("disabled", !this.checked);
    }).change()

    $('#checksbee').change(function () {
        $('#Sbee').prop("disabled", !this.checked);
    }).change()

    $('#checkwaterwQT').change(function () {
        $('#water').prop("disabled", !this.checked);
    }).change()

    $('#checkobservation').change(function () {
        $('#Observation').prop("disabled", !this.checked);
    }).change()

    $('#checknbrpanne').change(function () {
        $('#nbrepanne').prop("disabled", !this.checked);
    }).change()

    $('#checknbrpanne').change(function () {
        $('#pannedesc').prop("disabled", !this.checked);
    }).change()
    
    $('#checkprod').change(function () {
        $('#prod').prop("disabled", !this.checked);
    }).change()

    $('#checkautre').change(function () {
        $('#autre').prop("disabled", !this.checked);
    }).change()

    //script to calculate production
    $(document).ready(function() {
        //this calculates values automatically 
        Subtract();
        $("#ancien, #nouveau").on("keydown keyup", function() {
            Subtract();
        });
    });
    // Lorsque l'état de la case à cocher change
    $('#checkProdCalc').change(function() {
        // Si la case à cocher est désactivée
        if (!$(this).is(':checked')) {
            // Vider le champ input
            $('#NouveaIndex').val('');
        }
    });
    $(document).ready(function() {
    // Lorsque l'état de la case à cocher change
    $('#checkProdCalc').change(function() {
        // Si la case à cocher est désactivée
        if (!$(this).is(':checked')) {
            // Vider le champ input
            $('#NouveaIndex').val('');
        }
    });
});
    function Subtract() {
                var ancien = document.getElementById('ancien').value;
                var nouveau = document.getElementById('nouveau').value;
                var result = parseInt(nouveau) - parseInt(ancien);
                if (!isNaN(result)) {
                    document.getElementById('subt').value = result;
                }
            }
});
