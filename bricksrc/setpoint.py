from .namespaces import TAG, BRICK, RDFS, OWL
from rdflib import Literal

setpoint_definitions = {
    "Setpoint": {
        RDFS.seeAlso: Literal(
            "https://xp20.ashrae.org/terminology/index.php?term=setpoint"
        ),
        "tags": [TAG.Point, TAG.Setpoint],
        "subclasses": {
            "Enthalpy_Setpoint": {"tags": [TAG.Point, TAG.Setpoint, TAG.Enthalpy]},
            "Dewpoint_Setpoint": {"tags": [TAG.Point, TAG.Dewpoint, TAG.Setpoint]},
            "Demand_Setpoint": {
                "tags": [TAG.Point, TAG.Demand, TAG.Setpoint],
                "subclasses": {
                    "Cooling_Demand_Setpoint": {
                        "tags": [TAG.Point, TAG.Cool, TAG.Demand, TAG.Setpoint],
                    },
                    "Heating_Demand_Setpoint": {
                        "tags": [TAG.Point, TAG.Heat, TAG.Demand, TAG.Setpoint],
                    },
                    "Preheat_Demand_Setpoint": {
                        "tags": [TAG.Point, TAG.Preheat, TAG.Demand, TAG.Setpoint],
                    },
                    "Air_Flow_Demand_Setpoint": {
                        "tags": [
                            TAG.Point,
                            TAG.Air,
                            TAG.Flow,
                            TAG.Demand,
                            TAG.Setpoint,
                        ],
                        "subclasses": {
                            "Discharge_Air_Flow_Demand_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Discharge,
                                    TAG.Air,
                                    TAG.Flow,
                                    TAG.Demand,
                                    TAG.Setpoint,
                                ],
                            },
                            "Supply_Air_Flow_Demand_Setpoint": {
                                OWL.equivalentClass: BRICK[
                                    "Discharge_Air_Flow_Demand_Setpoint"
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Air,
                                    TAG.Flow,
                                    TAG.Demand,
                                    TAG.Setpoint,
                                ],
                            },
                        },
                    },
                },
            },
            "Damper_Position_Setpoint": {
                "tags": [TAG.Point, TAG.Damper, TAG.Position, TAG.Setpoint],
            },
            "Deadband_Setpoint": {
                "tags": [TAG.Point, TAG.Deadband, TAG.Setpoint],
                "subclasses": {
                    "Differential_Pressure_Deadband_Setpoint": {
                        "tags": [
                            TAG.Point,
                            TAG.Differential,
                            TAG.Pressure,
                            TAG.Deadband,
                            TAG.Setpoint,
                        ],
                        "parents": [BRICK.Differential_Pressure_Setpoint],
                        "subclasses": {
                            "Hot_Water_Differential_Pressure_Deadband_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Differential,
                                    TAG.Pressure,
                                    TAG.Deadband,
                                    TAG.Setpoint,
                                ],
                                "parents": [
                                    BRICK.Hot_Water_Differential_Pressure_Setpoint
                                ],
                            },
                            "Chilled_Water_Differential_Pressure_Deadband_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Chilled,
                                    TAG.Water,
                                    TAG.Differential,
                                    TAG.Pressure,
                                    TAG.Deadband,
                                    TAG.Setpoint,
                                ],
                                "parents": [
                                    BRICK.Chilled_Water_Differential_Pressure_Setpoint
                                ],
                                "subclasses": {
                                    "Chilled_Water_Pump_Differential_Pressure_Deadband_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Chilled,
                                            TAG.Water,
                                            TAG.Pump,
                                            TAG.Differential,
                                            TAG.Pressure,
                                            TAG.Deadband,
                                            TAG.Setpoint,
                                        ],
                                    },
                                },
                            },
                            "Discharge_Water_Differential_Pressure_Deadband_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Discharge,
                                    TAG.Water,
                                    TAG.Differential,
                                    TAG.Pressure,
                                    TAG.Deadband,
                                    TAG.Setpoint,
                                ],
                            },
                            "Supply_Water_Differential_Pressure_Deadband_Setpoint": {
                                OWL.equivalentClass: BRICK[
                                    "Discharge_Water_Differential_Pressure_Deadband_Setpoint"
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Water,
                                    TAG.Differential,
                                    TAG.Pressure,
                                    TAG.Deadband,
                                    TAG.Setpoint,
                                ],
                            },
                        },
                    },
                    "Temperature_Deadband_Setpoint": {
                        "subclasses": {
                            "Occupied_Cooling_Temperature_Deadband_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Occupied,
                                    TAG.Cool,
                                    TAG.Temperature,
                                    TAG.Deadband,
                                    TAG.Setpoint,
                                ],
                                "parents": [BRICK.Cooling_Temperature_Setpoint],
                            },
                            "Occupied_Heating_Temperature_Deadband_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Occupied,
                                    TAG.Heat,
                                    TAG.Temperature,
                                    TAG.Deadband,
                                    TAG.Setpoint,
                                ],
                                "parents": [BRICK.Heating_Temperature_Setpoint],
                            },
                            "Unoccupied_Cooling_Temperature_Deadband_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Unoccupied,
                                    TAG.Cool,
                                    TAG.Temperature,
                                    TAG.Deadband,
                                    TAG.Setpoint,
                                ],
                                "parents": [BRICK.Cooling_Temperature_Setpoint],
                            },
                            "Unoccupied_Heating_Temperature_Deadband_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Unoccupied,
                                    TAG.Heat,
                                    TAG.Temperature,
                                    TAG.Deadband,
                                    TAG.Setpoint,
                                ],
                                "parents": [BRICK.Heating_Temperature_Setpoint],
                            },
                            "Discharge_Air_Temperature_Deadband_Setpoint": {
                                "subclasses": {
                                    "Heating_Discharge_Air_Temperature_Deadband_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Heat,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Deadband,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [
                                            BRICK.Discharge_Air_Temperature_Heating_Setpoint
                                        ],
                                    },
                                    "Cooling_Discharge_Air_Temperature_Deadband_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Cool,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Deadband,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [
                                            BRICK.Discharge_Air_Temperature_Cooling_Setpoint
                                        ],
                                    },
                                },
                                "tags": [
                                    TAG.Point,
                                    TAG.Discharge,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Deadband,
                                    TAG.Setpoint,
                                ],
                                "parents": [BRICK.Discharge_Air_Temperature_Setpoint],
                            },
                            "Supply_Air_Temperature_Deadband_Setpoint": {
                                OWL.equivalentClass: BRICK[
                                    "Discharge_Air_Temperature_Deadband_Setpoint"
                                ],
                                "subclasses": {
                                    "Heating_Supply_Air_Temperature_Deadband_Setpoint": {
                                        OWL.equivalentClass: BRICK[
                                            "Heating_Discharge_Air_Temperature_Deadband_Setpoint"
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Heat,
                                            TAG.Supply,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Deadband,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [BRICK.Heating_Temperature_Setpoint],
                                    },
                                    "Cooling_Supply_Air_Temperature_Deadband_Setpoint": {
                                        OWL.equivalentClass: BRICK[
                                            "Cooling_Discharge_Air_Temperature_Deadband_Setpoint"
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Cool,
                                            TAG.Supply,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Deadband,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [BRICK.Cooling_Temperature_Setpoint],
                                    },
                                },
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Deadband,
                                    TAG.Setpoint,
                                ],
                                "parents": [BRICK.Air_Temperature_Setpoint],
                            },
                            "Supply_Water_Temperature_Deadband_Setpoint": {
                                OWL.equivalentClass: BRICK[
                                    "Discharge_Water_Temperature_Deadband_Setpoint"
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Deadband,
                                    TAG.Setpoint,
                                ],
                                "parents": [BRICK.Supply_Water_Temperature_Setpoint],
                            },
                            "Discharge_Water_Temperature_Deadband_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Discharge,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Deadband,
                                    TAG.Setpoint,
                                ],
                                "parents": [BRICK.Supply_Water_Temperature_Setpoint],
                            },
                        },
                        "tags": [
                            TAG.Point,
                            TAG.Temperature,
                            TAG.Deadband,
                            TAG.Setpoint,
                        ],
                        "parents": [BRICK.Temperature_Setpoint],
                    },
                    "Air_Flow_Deadband_Setpoint": {
                        "subclasses": {
                            "Exhaust_Air_Stack_Flow_Deadband_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Exhaust,
                                    TAG.Air,
                                    TAG.Stack,
                                    TAG.Flow,
                                    TAG.Deadband,
                                    TAG.Setpoint,
                                ],
                                "parents": [BRICK.Exhaust_Air_Stack_Flow_Setpoint],
                            }
                        },
                        "tags": [
                            TAG.Point,
                            TAG.Air,
                            TAG.Flow,
                            TAG.Deadband,
                            TAG.Setpoint,
                        ],
                        "parents": [BRICK.Air_Flow_Setpoint],
                    },
                    "Static_Pressure_Deadband_Setpoint": {
                        "tags": [
                            TAG.Point,
                            TAG.Static,
                            TAG.Pressure,
                            TAG.Deadband,
                            TAG.Setpoint,
                        ],
                        "parents": [BRICK.Static_Pressure_Setpoint],
                        "subclasses": {
                            "Discharge_Air_Static_Pressure_Deadband_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Discharge,
                                    TAG.Air,
                                    TAG.Static,
                                    TAG.Pressure,
                                    TAG.Deadband,
                                    TAG.Setpoint,
                                ],
                                "parents": [
                                    BRICK.Discharge_Air_Static_Pressure_Setpoint
                                ],
                            },
                            "Supply_Air_Static_Pressure_Deadband_Setpoint": {
                                OWL.equivalentClass: BRICK[
                                    "Discharge_Air_Static_Pressure_Deadband_Setpoint"
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Air,
                                    TAG.Static,
                                    TAG.Pressure,
                                    TAG.Deadband,
                                    TAG.Setpoint,
                                ],
                                "parents": [BRICK.Supply_Air_Static_Pressure_Setpoint],
                            },
                        },
                    },
                },
            },
            "Flow_Setpoint": {
                "tags": [TAG.Point, TAG.Flow, TAG.Setpoint],
                "subclasses": {
                    "Air_Flow_Setpoint": {
                        "tags": [TAG.Point, TAG.Air, TAG.Flow, TAG.Setpoint],
                        "subclasses": {
                            "Air_Flow_Demand_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Air,
                                    TAG.Flow,
                                    TAG.Demand,
                                    TAG.Setpoint,
                                ],
                            },
                            "Discharge_Air_Flow_Setpoint": {
                                "subclasses": {
                                    "Discharge_Air_Flow_Demand_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Flow,
                                            TAG.Demand,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Occupied_Discharge_Air_Flow_Setpoint": {
                                        "subclasses": {
                                            "Occupied_Cooling_Discharge_Air_Flow_Setpoint": {
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Occupied,
                                                    TAG.Cool,
                                                    TAG.Discharge,
                                                    TAG.Air,
                                                    TAG.Flow,
                                                    TAG.Setpoint,
                                                ],
                                                "parents": [
                                                    BRICK.Cooling_Discharge_Air_Flow_Setpoint
                                                ],
                                            },
                                            "Occupied_Heating_Discharge_Air_Flow_Setpoint": {
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Occupied,
                                                    TAG.Heat,
                                                    TAG.Discharge,
                                                    TAG.Air,
                                                    TAG.Flow,
                                                    TAG.Setpoint,
                                                ],
                                                "parents": [
                                                    BRICK.Heating_Discharge_Air_Flow_Setpoint
                                                ],
                                            },
                                        },
                                        "tags": [
                                            TAG.Point,
                                            TAG.Occupied,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Flow,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Unoccupied_Discharge_Air_Flow_Setpoint": {
                                        "subclasses": {
                                            "Unoccupied_Cooling_Discharge_Air_Flow_Setpoint": {
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Unoccupied,
                                                    TAG.Cool,
                                                    TAG.Discharge,
                                                    TAG.Air,
                                                    TAG.Flow,
                                                    TAG.Setpoint,
                                                ],
                                                "parents": [
                                                    BRICK.Cooling_Discharge_Air_Flow_Setpoint
                                                ],
                                            },
                                            "Unoccupied_Heating_Discharge_Air_Flow_Setpoint": {
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Unoccupied,
                                                    TAG.Heat,
                                                    TAG.Discharge,
                                                    TAG.Air,
                                                    TAG.Flow,
                                                    TAG.Setpoint,
                                                ],
                                                "parents": [
                                                    BRICK.Heating_Discharge_Air_Flow_Setpoint
                                                ],
                                            },
                                        },
                                        "tags": [
                                            TAG.Point,
                                            TAG.Unoccupied,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Flow,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Cooling_Discharge_Air_Flow_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Cool,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Flow,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Heating_Discharge_Air_Flow_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Heat,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Flow,
                                            TAG.Setpoint,
                                        ],
                                    },
                                },
                                "tags": [
                                    TAG.Point,
                                    TAG.Discharge,
                                    TAG.Air,
                                    TAG.Flow,
                                    TAG.Setpoint,
                                ],
                            },
                            "Exhaust_Air_Flow_Setpoint": {
                                "subclasses": {
                                    "Exhaust_Air_Stack_Flow_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Exhaust,
                                            TAG.Air,
                                            TAG.Stack,
                                            TAG.Flow,
                                            TAG.Setpoint,
                                        ],
                                    }
                                },
                                "tags": [
                                    TAG.Point,
                                    TAG.Exhaust,
                                    TAG.Air,
                                    TAG.Flow,
                                    TAG.Setpoint,
                                ],
                            },
                            "Outside_Air_Flow_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Outside,
                                    TAG.Air,
                                    TAG.Flow,
                                    TAG.Setpoint,
                                ],
                            },
                            "Supply_Air_Flow_Setpoint": {
                                OWL.equivalentClass: BRICK[
                                    "Discharge_Air_Flow_Setpoint"
                                ],
                                "subclasses": {
                                    "Supply_Air_Flow_Demand_Setpoint": {
                                        OWL.equivalentClass: BRICK[
                                            "Discharge_Air_Flow_Demand_Setpoint"
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Supply,
                                            TAG.Air,
                                            TAG.Flow,
                                            TAG.Demand,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Occupied_Supply_Air_Flow_Setpoint": {
                                        OWL.equivalentClass: BRICK[
                                            "Occupied_Discharge_Air_Flow_Setpoint"
                                        ],
                                        "subclasses": {
                                            "Occupied_Cooling_Supply_Air_Flow_Setpoint": {
                                                OWL.equivalentClass: BRICK[
                                                    "Occupied_Cooling_Discharge_Air_Flow_Setpoint"
                                                ],
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Occupied,
                                                    TAG.Cool,
                                                    TAG.Supply,
                                                    TAG.Air,
                                                    TAG.Flow,
                                                    TAG.Setpoint,
                                                ],
                                                "parents": [
                                                    BRICK.Cooling_Supply_Air_Flow_Setpoint
                                                ],
                                            },
                                            "Occupied_Heating_Supply_Air_Flow_Setpoint": {
                                                OWL.equivalentClass: BRICK[
                                                    "Occupied_Heating_Discharge_Air_Flow_Setpoint"
                                                ],
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Occupied,
                                                    TAG.Heat,
                                                    TAG.Supply,
                                                    TAG.Air,
                                                    TAG.Flow,
                                                    TAG.Setpoint,
                                                ],
                                                "parents": [
                                                    BRICK.Heating_Supply_Air_Flow_Setpoint
                                                ],
                                            },
                                        },
                                        "tags": [
                                            TAG.Point,
                                            TAG.Occupied,
                                            TAG.Supply,
                                            TAG.Air,
                                            TAG.Flow,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Unoccupied_Supply_Air_Flow_Setpoint": {
                                        OWL.equivalentClass: BRICK[
                                            "Unoccupied_Discharge_Air_Flow_Setpoint"
                                        ],
                                        "subclasses": {
                                            "Unoccupied_Cooling_Supply_Air_Flow_Setpoint": {
                                                OWL.equivalentClass: BRICK[
                                                    "Unoccupied_Cooling_Discharge_Air_Flow_Setpoint"
                                                ],
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Unoccupied,
                                                    TAG.Cool,
                                                    TAG.Supply,
                                                    TAG.Air,
                                                    TAG.Flow,
                                                    TAG.Setpoint,
                                                ],
                                                "parents": [
                                                    BRICK.Cooling_Supply_Air_Flow_Setpoint
                                                ],
                                            },
                                            "Unoccupied_Heating_Supply_Air_Flow_Setpoint": {
                                                OWL.equivalentClass: BRICK[
                                                    "Unoccupied_Heating_Discharge_Air_Flow_Setpoint"
                                                ],
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Unoccupied,
                                                    TAG.Heat,
                                                    TAG.Supply,
                                                    TAG.Air,
                                                    TAG.Flow,
                                                    TAG.Setpoint,
                                                ],
                                                "parents": [
                                                    BRICK.Heating_Supply_Air_Flow_Setpoint
                                                ],
                                            },
                                        },
                                        "tags": [
                                            TAG.Point,
                                            TAG.Unoccupied,
                                            TAG.Supply,
                                            TAG.Air,
                                            TAG.Flow,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Cooling_Supply_Air_Flow_Setpoint": {
                                        OWL.equivalentClass: BRICK[
                                            "Cooling_Discharge_Air_Flow_Setpoint"
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Cool,
                                            TAG.Supply,
                                            TAG.Air,
                                            TAG.Flow,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Heating_Supply_Air_Flow_Setpoint": {
                                        OWL.equivalentClass: BRICK[
                                            "Heating_Discharge_Air_Flow_Setpoint"
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Heat,
                                            TAG.Supply,
                                            TAG.Air,
                                            TAG.Flow,
                                            TAG.Setpoint,
                                        ],
                                    },
                                },
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Air,
                                    TAG.Flow,
                                    TAG.Setpoint,
                                ],
                            },
                        },
                    },
                    "Water_Flow_Setpoint": {
                        "tags": [
                            TAG.Point,
                            TAG.Water,
                            TAG.Flow,
                            TAG.Setpoint,
                        ],
                        "subclasses": {
                            "Supply_Water_Flow_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Water,
                                    TAG.Flow,
                                    TAG.Setpoint,
                                ],
                                OWL.equivalentClass: BRICK[
                                    "Discharge_Water_Flow_Setpoint"
                                ],
                                "subclasses": {
                                    "Chilled_Water_Supply_Flow_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Chilled,
                                            TAG.Water,
                                            TAG.Supply,
                                            TAG.Flow,
                                            TAG.Setpoint,
                                        ],
                                        OWL.equivalentClass: BRICK[
                                            "Chilled_Water_Discharge_Flow_Setpoint"
                                        ],
                                        "parents": [BRICK.Chilled_Water_Flow_Setpoint],
                                    },
                                    "Hot_Water_Supply_Flow_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Supply,
                                            TAG.Flow,
                                            TAG.Setpoint,
                                        ],
                                        OWL.equivalentClass: BRICK[
                                            "Hot_Water_Discharge_Flow_Setpoint"
                                        ],
                                        "parents": [BRICK.Hot_Water_Flow_Setpoint],
                                    },
                                },
                            },
                            "Discharge_Water_Flow_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Discharge,
                                    TAG.Water,
                                    TAG.Flow,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Chilled_Water_Discharge_Flow_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Chilled,
                                            TAG.Water,
                                            TAG.Discharge,
                                            TAG.Flow,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [BRICK.Chilled_Water_Flow_Setpoint],
                                    },
                                    "Hot_Water_Discharge_Flow_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Discharge,
                                            TAG.Flow,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [BRICK.Hot_Water_Flow_Setpoint],
                                    },
                                },
                            },
                            "Entering_Water_Flow_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Entering,
                                    TAG.Water,
                                    TAG.Flow,
                                    TAG.Setpoint,
                                ],
                            },
                            "Leaving_Water_Flow_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Leaving,
                                    TAG.Water,
                                    TAG.Flow,
                                    TAG.Setpoint,
                                ],
                            },
                            "Hot_Water_Flow_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Flow,
                                    TAG.Setpoint,
                                ],
                            },
                            "Chilled_Water_Flow_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Chilled,
                                    TAG.Water,
                                    TAG.Flow,
                                    TAG.Setpoint,
                                ],
                            },
                            "Bypass_Water_Flow_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Bypass,
                                    TAG.Water,
                                    TAG.Flow,
                                    TAG.Setpoint,
                                ],
                            },
                        },
                    },
                },
            },
            "Humidity_Setpoint": {
                "tags": [TAG.Point, TAG.Humidity, TAG.Setpoint],
                "subclasses": {
                    "Unoccupied_Humidity_Setpoint": {
                        "tags": [TAG.Point, TAG.Humidity, TAG.Setpoint, TAG.Unoccupied],
                    },
                    "Occupied_Humidity_Setpoint": {
                        "tags": [TAG.Point, TAG.Humidity, TAG.Setpoint, TAG.Occupied],
                    },
                    "Bypass_Air_Humidity_Setpoint": {
                        "tags": [
                            TAG.Point,
                            TAG.Humidity,
                            TAG.Setpoint,
                            TAG.Air,
                            TAG.Bypass,
                        ],
                    },
                    "Outside_Air_Humidity_Setpoint": {
                        "tags": [
                            TAG.Point,
                            TAG.Humidity,
                            TAG.Setpoint,
                            TAG.Air,
                            TAG.Outside,
                        ],
                    },
                    "Zone_Air_Humidity_Setpoint": {
                        "tags": [
                            TAG.Point,
                            TAG.Humidity,
                            TAG.Setpoint,
                            TAG.Air,
                            TAG.Zone,
                        ],
                    },
                    "Building_Air_Humidity_Setpoint": {
                        "tags": [
                            TAG.Point,
                            TAG.Humidity,
                            TAG.Setpoint,
                            TAG.Air,
                            TAG.Building,
                        ],
                    },
                    "Discharge_Air_Humidity_Setpoint": {
                        "tags": [
                            TAG.Point,
                            TAG.Humidity,
                            TAG.Setpoint,
                            TAG.Air,
                            TAG.Discharge,
                        ],
                    },
                    "Mixed_Air_Humidity_Setpoint": {
                        "tags": [
                            TAG.Point,
                            TAG.Humidity,
                            TAG.Setpoint,
                            TAG.Air,
                            TAG.Mixed,
                        ],
                    },
                    "Return_Air_Humidity_Setpoint": {
                        "tags": [
                            TAG.Point,
                            TAG.Humidity,
                            TAG.Setpoint,
                            TAG.Air,
                            TAG.Return,
                        ],
                    },
                    "Exhaust_Air_Humidity_Setpoint": {
                        "tags": [
                            TAG.Point,
                            TAG.Humidity,
                            TAG.Setpoint,
                            TAG.Air,
                            TAG.Exhaust,
                        ],
                    },
                    "Supply_Air_Humidity_Setpoint": {
                        OWL.equivalentClass: BRICK["Discharge_Air_Humidity_Setpoint"],
                        "tags": [
                            TAG.Point,
                            TAG.Humidity,
                            TAG.Setpoint,
                            TAG.Air,
                            TAG.Supply,
                        ],
                    },
                },
            },
            "Load_Setpoint": {
                "subclasses": {
                    "Load_Shed_Setpoint": {
                        "tags": [TAG.Point, TAG.Shed, TAG.Load, TAG.Setpoint],
                        "subclasses": {
                            "Medium_Temperature_Hot_Water_Differential_Pressure_Load_Shed_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Medium,
                                    TAG.Temperature,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Differential,
                                    TAG.Pressure,
                                    TAG.Shed,
                                    TAG.Load,
                                    TAG.Setpoint,
                                ],
                            },
                            "Medium_Temperature_Hot_Water_Supply_Temperature_Load_Shed_Setpoint": {
                                OWL.equivalentClass: BRICK[
                                    "Medium_Temperature_Hot_Water_Discharge_Temperature_Load_Shed_Setpoint"
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Medium,
                                    TAG.Temperature,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Supply,
                                    TAG.Pressure,
                                    TAG.Shed,
                                    TAG.Load,
                                    TAG.Setpoint,
                                ],
                            },
                            "Medium_Temperature_Hot_Water_Discharge_Temperature_Load_Shed_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Medium,
                                    TAG.Temperature,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Supply,
                                    TAG.Pressure,
                                    TAG.Shed,
                                    TAG.Load,
                                    TAG.Setpoint,
                                ],
                            },
                        },
                    },
                },
                "tags": [TAG.Point, TAG.Load, TAG.Setpoint],
            },
            "Luminance_Setpoint": {"tags": [TAG.Point, TAG.Luminance, TAG.Setpoint]},
            "Pressure_Setpoint": {
                "subclasses": {
                    "Differential_Pressure_Setpoint": {
                        "subclasses": {
                            "Air_Differential_Pressure_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Air,
                                    TAG.Differential,
                                    TAG.Pressure,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Exhaust_Air_Differential_Pressure_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Exhaust,
                                            TAG.Air,
                                            TAG.Setpoint,
                                            TAG.Pressure,
                                            TAG.Differential,
                                        ],
                                    },
                                    "Return_Air_Differential_Pressure_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Return,
                                            TAG.Air,
                                            TAG.Setpoint,
                                            TAG.Pressure,
                                            TAG.Differential,
                                        ],
                                    },
                                    "Supply_Air_Differential_Pressure_Setpoint": {
                                        OWL.equivalentClass: BRICK[
                                            "Discharge_Air_Differential_Pressure_Setpoint"
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Supply,
                                            TAG.Air,
                                            TAG.Setpoint,
                                            TAG.Pressure,
                                            TAG.Differential,
                                        ],
                                    },
                                    "Discharge_Air_Differential_Pressure_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Setpoint,
                                            TAG.Pressure,
                                            TAG.Differential,
                                        ],
                                    },
                                },
                            },
                            "Water_Differential_Pressure_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Water,
                                    TAG.Differential,
                                    TAG.Pressure,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Chilled_Water_Differential_Pressure_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Chilled,
                                            TAG.Water,
                                            TAG.Differential,
                                            TAG.Pressure,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Hot_Water_Differential_Pressure_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Differential,
                                            TAG.Pressure,
                                            TAG.Setpoint,
                                        ],
                                        "subclasses": {
                                            "Medium_Temperature_Hot_Water_Differential_Pressure_Setpoint": {
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Medium,
                                                    TAG.Temperature,
                                                    TAG.Hot,
                                                    TAG.Water,
                                                    TAG.Differential,
                                                    TAG.Pressure,
                                                    TAG.Setpoint,
                                                ],
                                            },
                                        },
                                    },
                                },
                            },
                            "Load_Shed_Differential_Pressure_Setpoint": {
                                "parents": [BRICK.Load_Shed_Setpoint],
                                "subclasses": {
                                    "Chilled_Water_Differential_Pressure_Load_Shed_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Chilled,
                                            TAG.Water,
                                            TAG.Differential,
                                            TAG.Pressure,
                                            TAG.Load,
                                            TAG.Shed,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [
                                            BRICK.Chilled_Water_Differential_Pressure_Setpoint
                                        ],
                                    },
                                },
                                "tags": [
                                    TAG.Point,
                                    TAG.Load,
                                    TAG.Shed,
                                    TAG.Differential,
                                    TAG.Pressure,
                                    TAG.Setpoint,
                                ],
                            },
                        },
                        "tags": [
                            TAG.Point,
                            TAG.Differential,
                            TAG.Pressure,
                            TAG.Setpoint,
                        ],
                    },
                    "Static_Pressure_Setpoint": {
                        "subclasses": {
                            "Building_Air_Static_Pressure_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Building,
                                    TAG.Air,
                                    TAG.Static,
                                    TAG.Pressure,
                                    TAG.Setpoint,
                                ],
                            },
                            "Chilled_Water_Static_Pressure_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Chilled,
                                    TAG.Water,
                                    TAG.Static,
                                    TAG.Pressure,
                                    TAG.Setpoint,
                                ],
                            },
                            "Discharge_Air_Static_Pressure_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Discharge,
                                    TAG.Air,
                                    TAG.Static,
                                    TAG.Pressure,
                                    TAG.Setpoint,
                                ],
                            },
                            "Exhaust_Air_Static_Pressure_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Exhaust,
                                    TAG.Air,
                                    TAG.Static,
                                    TAG.Pressure,
                                    TAG.Setpoint,
                                ],
                            },
                            "Hot_Water_Static_Pressure_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Static,
                                    TAG.Pressure,
                                    TAG.Setpoint,
                                ],
                            },
                            "Supply_Air_Static_Pressure_Setpoint": {
                                OWL.equivalentClass: BRICK[
                                    "Discharge_Air_Static_Pressure_Setpoint"
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Air,
                                    TAG.Static,
                                    TAG.Pressure,
                                    TAG.Setpoint,
                                ],
                            },
                            "Underfloor_Air_Plenum_Static_Pressure_Setpoint": {
                                "tags": [
                                    TAG.Underfloor,
                                    TAG.Air,
                                    TAG.Plenum,
                                    TAG.Static,
                                    TAG.Pressure,
                                    TAG.Setpoint,
                                ]
                            },
                        },
                        "tags": [TAG.Point, TAG.Static, TAG.Pressure, TAG.Setpoint],
                    },
                    "Velocity_Pressure_Setpoint": {
                        "tags": [TAG.Point, TAG.Velocity, TAG.Pressure, TAG.Setpoint],
                    },
                },
                "tags": [TAG.Point, TAG.Pressure, TAG.Setpoint],
            },
            "Reset_Setpoint": {
                "tags": [TAG.Point, TAG.Reset, TAG.Setpoint],
                "subclasses": {
                    "Supply_Air_Flow_Reset_Setpoint": {
                        OWL.equivalentClass: BRICK["Discharge_Air_Flow_Reset_Setpoint"],
                        "tags": [
                            TAG.Point,
                            TAG.Supply,
                            TAG.Air,
                            TAG.Flow,
                            TAG.Reset,
                            TAG.Setpoint,
                        ],
                        "subclasses": {
                            "Supply_Air_Flow_High_Reset_Setpoint": {
                                OWL.equivalentClass: BRICK[
                                    "Discharge_Air_Flow_High_Reset_Setpoint"
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Air,
                                    TAG.Flow,
                                    TAG.Reset,
                                    TAG.Setpoint,
                                    TAG.High,
                                ],
                            },
                            "Supply_Air_Flow_Low_Reset_Setpoint": {
                                OWL.equivalentClass: BRICK[
                                    "Discharge_Air_Flow_Low_Reset_Setpoint"
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Air,
                                    TAG.Flow,
                                    TAG.Reset,
                                    TAG.Setpoint,
                                    TAG.Low,
                                ],
                            },
                        },
                    },
                    "Discharge_Air_Flow_Reset_Setpoint": {
                        "tags": [
                            TAG.Point,
                            TAG.Discharge,
                            TAG.Air,
                            TAG.Flow,
                            TAG.Reset,
                            TAG.Setpoint,
                        ],
                        "subclasses": {
                            "Discharge_Air_Flow_High_Reset_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Discharge,
                                    TAG.Air,
                                    TAG.Flow,
                                    TAG.Reset,
                                    TAG.Setpoint,
                                    TAG.High,
                                ],
                            },
                            "Discharge_Air_Flow_Low_Reset_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Discharge,
                                    TAG.Air,
                                    TAG.Flow,
                                    TAG.Reset,
                                    TAG.Setpoint,
                                    TAG.Low,
                                ],
                            },
                        },
                    },
                    "Temperature_Differential_Reset_Setpoint": {
                        "tags": [
                            TAG.Point,
                            TAG.Temperature,
                            TAG.Differential,
                            TAG.Reset,
                            TAG.Setpoint,
                        ],
                        "subclasses": {
                            "Discharge_Air_Temperature_Reset_Differential_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Discharge,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Differential,
                                    TAG.Reset,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Discharge_Air_Temperature_High_Reset_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Differential,
                                            TAG.Reset,
                                            TAG.Setpoint,
                                            TAG.High,
                                        ],
                                    },
                                    "Discharge_Air_Temperature_Low_Reset_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Differential,
                                            TAG.Reset,
                                            TAG.Setpoint,
                                            TAG.Low,
                                        ],
                                    },
                                },
                            },
                            "Supply_Air_Temperature_Reset_Differential_Setpoint": {
                                OWL.equivalentClass: BRICK[
                                    "Discharge_Air_Temperature_Reset_Differential_Setpoint"
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Differential,
                                    TAG.Reset,
                                    TAG.Setpoint,
                                ],
                            },
                        },
                    },
                    "Temperature_High_Reset_Setpoint": {
                        "tags": [
                            TAG.Point,
                            TAG.Temperature,
                            TAG.High,
                            TAG.Reset,
                            TAG.Setpoint,
                        ],
                        "subclasses": {
                            "Hot_Water_Supply_Temperature_High_Reset_Setpoint": {
                                OWL.equivalentClass: BRICK[
                                    "Hot_Water_Discharge_Temperature_High_Reset_Setpoint"
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Supply,
                                    TAG.Temperature,
                                    TAG.High,
                                    TAG.Reset,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Medium_Temperature_Hot_Water_Supply_Temperature_High_Reset_Setpoint": {
                                        OWL.equivalentClass: BRICK[
                                            "Medium_Temperature_Hot_Water_Discharge_Temperature_High_Reset_Setpoint"
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Medium,
                                            TAG.Temperature,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Supply,
                                            TAG.Temperature,
                                            TAG.High,
                                            TAG.Reset,
                                            TAG.Setpoint,
                                        ],
                                    },
                                },
                            },
                            "Hot_Water_Discharge_Temperature_High_Reset_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Supply,
                                    TAG.Temperature,
                                    TAG.High,
                                    TAG.Reset,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Medium_Temperature_Hot_Water_Discharge_Temperature_High_Reset_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Medium,
                                            TAG.Temperature,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Discharge,
                                            TAG.Temperature,
                                            TAG.High,
                                            TAG.Reset,
                                            TAG.Setpoint,
                                        ],
                                    },
                                },
                            },
                            "Supply_Air_Temperature_High_Reset_Setpoint": {
                                OWL.equivalentClass: BRICK[
                                    "Discharge_Air_Temperature_High_Reset_Setpoint"
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.High,
                                    TAG.Reset,
                                    TAG.Setpoint,
                                ],
                            },
                            "Outside_Air_Temperature_High_Reset_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Outside,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.High,
                                    TAG.Reset,
                                    TAG.Setpoint,
                                ],
                            },
                            "Return_Air_Temperature_High_Reset_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Return,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.High,
                                    TAG.Reset,
                                    TAG.Setpoint,
                                ],
                            },
                        },
                    },
                    "Temperature_Low_Reset_Setpoint": {
                        "tags": [
                            TAG.Point,
                            TAG.Temperature,
                            TAG.Low,
                            TAG.Reset,
                            TAG.Setpoint,
                        ],
                        "subclasses": {
                            "Supply_Air_Temperature_Low_Reset_Setpoint": {
                                OWL.equivalentClass: BRICK[
                                    "Discharge_Air_Temperature_Low_Reset_Setpoint"
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Low,
                                    TAG.Reset,
                                    TAG.Setpoint,
                                ],
                            },
                            "Hot_Water_Supply_Temperature_Low_Reset_Setpoint": {
                                OWL.equivalentClass: BRICK[
                                    "Hot_Water_Discharge_Temperature_Low_Reset_Setpoint"
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Supply,
                                    TAG.Temperature,
                                    TAG.Low,
                                    TAG.Reset,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Medium_Temperature_Hot_Water_Supply_Temperature_Low_Reset_Setpoint": {
                                        OWL.equivalentClass: BRICK[
                                            "Medium_Temperature_Hot_Water_Discharge_Temperature_Low_Reset_Setpoint"
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Medium,
                                            TAG.Temperature,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Supply,
                                            TAG.Temperature,
                                            TAG.Low,
                                            TAG.Reset,
                                            TAG.Setpoint,
                                        ],
                                    },
                                },
                            },
                            "Hot_Water_Discharge_Temperature_Low_Reset_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Discharge,
                                    TAG.Temperature,
                                    TAG.Low,
                                    TAG.Reset,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Medium_Temperature_Hot_Water_Discharge_Temperature_Low_Reset_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Medium,
                                            TAG.Temperature,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Discharge,
                                            TAG.Temperature,
                                            TAG.Low,
                                            TAG.Reset,
                                            TAG.Setpoint,
                                        ],
                                    },
                                },
                            },
                            "Outside_Air_Temperature_Low_Reset_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Outside,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Low,
                                    TAG.Reset,
                                    TAG.Setpoint,
                                ],
                            },
                            "Return_Air_Temperature_Low_Reset_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Return,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Low,
                                    TAG.Reset,
                                    TAG.Setpoint,
                                ],
                            },
                        },
                    },
                },
            },
            "Speed_Setpoint": {
                "tags": [TAG.Point, TAG.Speed, TAG.Setpoint],
                "subclasses": {
                    "Rated_Speed_Setpoint": {
                        "tags": [TAG.Point, TAG.Rated, TAG.Speed, TAG.Setpoint],
                    },
                    "Differential_Speed_Setpoint": {
                        "tags": [TAG.Point, TAG.Differential, TAG.Speed, TAG.Setpoint],
                    },
                },
            },
            "Temperature_Setpoint": {
                "tags": [TAG.Point, TAG.Temperature, TAG.Setpoint],
                "subclasses": {
                    "Air_Temperature_Setpoint": {
                        "tags": [TAG.Point, TAG.Air, TAG.Temperature, TAG.Setpoint],
                        "subclasses": {
                            "Differential_Air_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Differential,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                            },
                            "Discharge_Air_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Discharge,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Effective_Discharge_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                            TAG.Effective,
                                        ],
                                        "parents": [
                                            BRICK.Effective_Air_Temperature_Setpoint
                                        ],
                                    },
                                    "Occupied_Discharge_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                            TAG.Occupied,
                                        ],
                                        "parents": [
                                            BRICK.Occupied_Air_Temperature_Setpoint
                                        ],
                                    },
                                    "Unoccupied_Discharge_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                            TAG.Unoccupied,
                                        ],
                                        "parents": [
                                            BRICK.Unoccupied_Air_Temperature_Setpoint
                                        ],
                                    },
                                    "Discharge_Air_Temperature_Heating_Setpoint": {
                                        "parents": [BRICK.Heating_Temperature_Setpoint],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Heat,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Discharge_Air_Temperature_Cooling_Setpoint": {
                                        "parents": [BRICK.Cooling_Temperature_Setpoint],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Cool,
                                            TAG.Setpoint,
                                        ],
                                    },
                                },
                            },
                            "Effective_Air_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Effective,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Effective_Air_Temperature_Cooling_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Effective,
                                            TAG.Air,
                                            TAG.Cool,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [BRICK.Cooling_Temperature_Setpoint],
                                    },
                                    "Effective_Air_Temperature_Heating_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Effective,
                                            TAG.Air,
                                            TAG.Heat,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [BRICK.Heating_Temperature_Setpoint],
                                    },
                                },
                            },
                            "Mixed_Air_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Mixed,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                            },
                            "Occupied_Air_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Occupied,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Occupied_Air_Temperature_Cooling_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Occupied,
                                            TAG.Cool,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [BRICK.Cooling_Temperature_Setpoint],
                                    },
                                    "Occupied_Air_Temperature_Heating_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Occupied,
                                            TAG.Heat,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [BRICK.Heating_Temperature_Setpoint],
                                    },
                                },
                            },
                            "Return_Air_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Return,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Effective_Return_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Return,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Heat,
                                            TAG.Setpoint,
                                            TAG.Effective,
                                        ],
                                        "parents": [
                                            BRICK.Effective_Air_Temperature_Setpoint
                                        ],
                                    },
                                    "Occupied_Return_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Return,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Heat,
                                            TAG.Setpoint,
                                            TAG.Occupied,
                                        ],
                                        "parents": [
                                            BRICK.Occupied_Air_Temperature_Setpoint
                                        ],
                                    },
                                    "Unoccupied_Return_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Return,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Heat,
                                            TAG.Setpoint,
                                            TAG.Unoccupied,
                                        ],
                                        "parents": [
                                            BRICK.Unoccupied_Air_Temperature_Setpoint
                                        ],
                                    },
                                },
                            },
                            "Room_Air_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Room,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Effective_Room_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Room,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Heat,
                                            TAG.Setpoint,
                                            TAG.Effective,
                                        ],
                                        "parents": [
                                            BRICK.Effective_Air_Temperature_Setpoint
                                        ],
                                    },
                                    "Occupied_Room_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Room,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Heat,
                                            TAG.Setpoint,
                                            TAG.Occupied,
                                        ],
                                        "parents": [
                                            BRICK.Occupied_Air_Temperature_Setpoint
                                        ],
                                    },
                                    "Unoccupied_Room_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Room,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Heat,
                                            TAG.Setpoint,
                                            TAG.Unoccupied,
                                        ],
                                        "parents": [
                                            BRICK.Unoccupied_Air_Temperature_Setpoint
                                        ],
                                    },
                                },
                            },
                            "Zone_Air_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Zone,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Effective_Zone_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Zone,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Heat,
                                            TAG.Setpoint,
                                            TAG.Effective,
                                        ],
                                        "parents": [
                                            BRICK.Effective_Air_Temperature_Setpoint
                                        ],
                                    },
                                    "Occupied_Zone_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Zone,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Heat,
                                            TAG.Setpoint,
                                            TAG.Occupied,
                                        ],
                                        "parents": [
                                            BRICK.Occupied_Air_Temperature_Setpoint
                                        ],
                                    },
                                    "Unoccupied_Zone_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Zone,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Heat,
                                            TAG.Setpoint,
                                            TAG.Unoccupied,
                                        ],
                                        "parents": [
                                            BRICK.Unoccupied_Air_Temperature_Setpoint
                                        ],
                                    },
                                    "Zone_Air_Cooling_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Zone,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                            TAG.Cool,
                                        ],
                                        "parents": [BRICK.Cooling_Temperature_Setpoint],
                                    },
                                    "Zone_Air_Heating_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Zone,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                            TAG.Heating,
                                        ],
                                        "parents": [BRICK.Heating_Temperature_Setpoint],
                                    },
                                },
                            },
                            "Outside_Air_Temperature_Setpoint": {
                                "subclasses": {
                                    "Low_Outside_Air_Temperature_Enable_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Low,
                                            TAG.Outside,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Enable,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Disable_Hot_Water_System_Outside_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Disable,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.System,
                                            TAG.Outside,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Enable_Hot_Water_System_Outside_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Enable,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.System,
                                            TAG.Outside,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Open_Heating_Valve_Outside_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Open,
                                            TAG.Heat,
                                            TAG.Valve,
                                            TAG.Outside,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [BRICK.Heating_Temperature_Setpoint],
                                    },
                                    "Outside_Air_Lockout_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Outside,
                                            TAG.Air,
                                            TAG.Lockout,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                    },
                                },
                                "tags": [
                                    TAG.Point,
                                    TAG.Outside,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                            },
                            "Unoccupied_Air_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Unoccupied,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Unoccupied_Air_Temperature_Cooling_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Unoccupied,
                                            TAG.Cool,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [BRICK.Cooling_Temperature_Setpoint],
                                    },
                                    "Unoccupied_Air_Temperature_Heating_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Unoccupied,
                                            TAG.Heat,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [BRICK.Heating_Temperature_Setpoint],
                                    },
                                },
                            },
                            "Supply_Air_Temperature_Setpoint": {
                                OWL.equivalentClass: BRICK[
                                    "Discharge_Air_Temperature_Setpoint"
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Effective_Supply_Air_Temperature_Setpoint": {
                                        OWL.equivalentClass: BRICK[
                                            "Effective_Discharge_Air_Temperature_Setpoint"
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Supply,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Heat,
                                            TAG.Setpoint,
                                            TAG.Effective,
                                        ],
                                        "parents": [
                                            BRICK.Effective_Air_Temperature_Setpoint
                                        ],
                                    },
                                    "Occupied_Supply_Air_Temperature_Setpoint": {
                                        OWL.equivalentClass: BRICK[
                                            "Occupied_Discharge_Air_Temperature_Setpoint"
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Supply,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Heat,
                                            TAG.Setpoint,
                                            TAG.Occupied,
                                        ],
                                        "parents": [
                                            BRICK.Occupied_Air_Temperature_Setpoint
                                        ],
                                    },
                                    "Unoccupied_Supply_Air_Temperature_Setpoint": {
                                        OWL.equivalentClass: BRICK[
                                            "Unoccupied_Discharge_Air_Temperature_Setpoint"
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Supply,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Heat,
                                            TAG.Setpoint,
                                            TAG.Unoccupied,
                                        ],
                                        "parents": [
                                            BRICK.Unoccupied_Air_Temperature_Setpoint
                                        ],
                                    },
                                    "Supply_Air_Temperature_Heating_Setpoint": {
                                        OWL.equivalentClass: BRICK[
                                            "Discharge_Air_Temperature_Heating_Setpoint"
                                        ],
                                        "parents": [BRICK.Heating_Temperature_Setpoint],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Supply,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Heat,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Supply_Air_Temperature_Cooling_Setpoint": {
                                        OWL.equivalentClass: BRICK[
                                            "Discharge_Air_Temperature_Cooling_Setpoint"
                                        ],
                                        "parents": [BRICK.Cooling_Temperature_Setpoint],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Supply,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Cool,
                                            TAG.Setpoint,
                                        ],
                                    },
                                },
                            },
                            "Min_Air_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Min,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ]
                            },
                            "Max_Air_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Max,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ]
                            },
                        },
                    },
                    "Cooling_Temperature_Setpoint": {
                        "tags": [TAG.Point, TAG.Temperature, TAG.Setpoint, TAG.Cool],
                        "subclasses": {
                            "Occupied_Cooling_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                    TAG.Cool,
                                    TAG.Occupied,
                                ],
                            },
                            "Unoccupied_Cooling_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                    TAG.Cool,
                                    TAG.Unoccupied,
                                ],
                            },
                        },
                    },
                    "Heating_Temperature_Setpoint": {
                        "tags": [TAG.Point, TAG.Temperature, TAG.Setpoint, TAG.Heat],
                        "subclasses": {
                            "Occupied_Heating_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                    TAG.Heat,
                                    TAG.Occupied,
                                ],
                            },
                            "Unoccupied_Heating_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                    TAG.Heat,
                                    TAG.Unoccupied,
                                ],
                            },
                        },
                    },
                    "Schedule_Temperature_Setpoint": {
                        "tags": [
                            TAG.Point,
                            TAG.Temperature,
                            TAG.Setpoint,
                            TAG.Schedule,
                        ],
                    },
                    "Radiant_Panel_Temperature_Setpoint": {
                        "tags": [
                            TAG.Point,
                            TAG.Radiant,
                            TAG.Panel,
                            TAG.Temperature,
                            TAG.Setpoint,
                        ],
                        "subclasses": {
                            "Inside_Face_Surface_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Inside,
                                    TAG.Face,
                                    TAG.Surface,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                            },
                            "Outside_Face_Surface_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Outside,
                                    TAG.Face,
                                    TAG.Surface,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                            },
                            "Embedded_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Embedded,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Core_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Core,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                    },
                                },
                            },
                        },
                    },
                    "Water_Temperature_Setpoint": {
                        "subclasses": {
                            "Domestic_Hot_Water_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Domestic,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                                "parents": [BRICK.Hot_Water_Temperature_Setpoint],
                                "subclasses": {
                                    "Domestic_Hot_Water_Supply_Temperature_Setpoint": {
                                        OWL.equivalentClass: BRICK[
                                            "Domestic_Hot_Water_Discharge_Temperature_Setpoint"
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Domestic,
                                            TAG.Hot,
                                            TAG.Supply,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [
                                            BRICK.Supply_Water_Temperature_Setpoint
                                        ],
                                    },
                                    "Domestic_Hot_Water_Discharge_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Domestic,
                                            TAG.Hot,
                                            TAG.Discharge,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [
                                            BRICK.Discharge_Water_Temperature_Setpoint
                                        ],
                                    },
                                },
                            },
                            "Water_Differential_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Water,
                                    TAG.Differential,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                            },
                            "Chilled_Water_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Chilled,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                            },
                            "Hot_Water_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                            },
                            "Return_Water_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Return,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Return_Hot_Water_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                            TAG.Return,
                                        ],
                                        "parents": [
                                            BRICK.Hot_Water_Temperature_Setpoint
                                        ],
                                    },
                                    "Return_Chilled_Water_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Return,
                                            TAG.Chilled,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [
                                            BRICK.Chilled_Water_Temperature_Setpoint
                                        ],
                                    },
                                },
                            },
                            "Discharge_Water_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Discharge,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Discharge_Hot_Water_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Discharge,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                            TAG.Hot,
                                        ],
                                        "parents": [
                                            BRICK.Hot_Water_Temperature_Setpoint
                                        ],
                                    },
                                    "Discharge_Chilled_Water_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Discharge,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                            TAG.Chilled,
                                        ],
                                        "parents": [
                                            BRICK.Chilled_Water_Temperature_Setpoint
                                        ],
                                    },
                                    "Discharge_Condenser_Water_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Discharge,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                            TAG.Condenser,
                                        ],
                                    },
                                },
                            },
                            "Supply_Water_Temperature_Setpoint": {
                                OWL.equivalentClass: BRICK[
                                    "Discharge_Water_Temperature_Setpoint"
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Supply_Hot_Water_Temperature_Setpoint": {
                                        OWL.equivalentClass: BRICK[
                                            "Discharge_Hot_Water_Temperature_Setpoint"
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Supply,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                            TAG.Hot,
                                        ],
                                        "parents": [
                                            BRICK.Hot_Water_Temperature_Setpoint
                                        ],
                                    },
                                    "Supply_Chilled_Water_Temperature_Setpoint": {
                                        OWL.equivalentClass: BRICK[
                                            "Discharge_Chilled_Water_Temperature_Setpoint"
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Supply,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                            TAG.Chilled,
                                        ],
                                        "parents": [
                                            BRICK.Chilled_Water_Temperature_Setpoint
                                        ],
                                    },
                                    "Supply_Condenser_Water_Temperature_Setpoint": {
                                        OWL.equivalentClass: BRICK[
                                            "Discharge_Condenser_Water_Temperature_Setpoint"
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Supply,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                            TAG.Condenser,
                                        ],
                                    },
                                    "Return_Condenser_Water_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Return,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                            TAG.Condenser,
                                        ],
                                        "parents": [
                                            BRICK.Discharge_Water_Temperature_Setpoint
                                        ],
                                    },
                                },
                            },
                            "Entering_Water_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Entering,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                            },
                            "Leaving_Water_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Leaving,
                                    TAG.Setpoint,
                                    TAG.Temperature,
                                    TAG.Water,
                                ],
                            },
                            "Min_Water_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Min,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ]
                            },
                            "Max_Water_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Max,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ]
                            },
                        },
                        "tags": [TAG.Point, TAG.Water, TAG.Temperature, TAG.Setpoint],
                    },
                },
            },
            "CO2_Setpoint": {
                "subclasses": {
                    "Return_Air_CO2_Setpoint": {
                        "tags": [TAG.Point, TAG.Return, TAG.Air, TAG.CO2, TAG.Setpoint],
                    }
                },
                "tags": [TAG.Point, TAG.CO2, TAG.Setpoint],
            },
            "Time_Setpoint": {
                "tags": [TAG.Point, TAG.Time, TAG.Setpoint],
                "subclasses": {
                    "Deceleration_Time_Setpoint": {
                        "tags": [TAG.Point, TAG.Time, TAG.Setpoint, TAG.Deceleration],
                    },
                    "Acceleration_Time_Setpoint": {
                        "tags": [TAG.Point, TAG.Time, TAG.Setpoint, TAG.Acceleration],
                    },
                },
            },
        },
    }
}
