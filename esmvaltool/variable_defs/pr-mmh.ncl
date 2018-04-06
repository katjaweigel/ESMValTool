;
; Requires: pr:T2*s
;
load "interface_scripts/data_handling.ncl"
load "./interface_scripts/logging.ncl"

variable_info = True
variable_info@derived = True
variable_info@long_name = "Precipitation Rate"
variable_info@units = "mm/hour"

;ymin,ymax info for DiurnalCycle_box.ncl diag_script
variable_info@minmax = (/0,1.6/)

undef("calculate")
function calculate(index [1] : integer,
                   variable [1] : string,
                   field_type [1] : string)
;;                 return_val [1] : logical
;; Arguments:
;;    index    - index to current infile defined in the 'interface_data/ncl.interface'-file
;;    variable - string with current variable
;;    field_type  - string with field type classification
;; Return value:
;;    data_new - logical
;; Description:
;;    Converts precipitation rate from units "kg m-2 s-1" to "mm h-1"
local result, T, verbosity
begin
    verbosity = config_user_info@verbosity
    info_output("<<<<<<<< Entering calculate (pr-mmh)", verbosity, 4)
    result = read_data(index, "pr", "T2*s")
    T = extract_data(index, result, -1, 0, 0)
    T=T*3600
    T@units = variable_info@units

    data_new = True
    add_data_var(index, data_new, T, variable)
    info_output(">>>>>>>> Leaving calculate (pr-mmh)", verbosity, 4)
    return(data_new)
end
