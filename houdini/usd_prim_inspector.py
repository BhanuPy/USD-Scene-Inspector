"""
USD Prim Inspector

Purpose:
Inspect USD prims from a Houdini Solaris stage.

Features:
- USD stage initialization
- Prim path and type inspection
- Child count inspection
- Attribute inspection
- Relationship inspection
- Prim metadata inspection
- Applied API schema inspection
- JSON report generation
- Invalid prim handling
"""
import hou
import json
from pxr import Usd, UsdGeom

# ----------------------------------
# 1. INITIALIZE USD STAGE
# ----------------------------------

lop_path = "/obj/usd_stage/YOUR_FINAL_NODE"

lop = hou.node(lop_path)

if lop is None:
    raise RuntimeError(f"LOP node not found: {lop_path}")

if lop.isBypassed():
    raise RuntimeError("The selected LOP node is bypassed.")

if lop.errors():
    raise RuntimeError(f"LOP errors: {lop.errors()}")

stage = lop.stage()

print("USD Stage initialized successfully.")


# ----------------------------------
# 2. PRIM INSPECTION FUNCTION
# ----------------------------------

def inspect_prim(stage, prim_path):

    prim = stage.GetPrimAtPath(prim_path)

    if not prim.IsValid():
        print(f"Prim not found: {prim_path}")
        return None

    attributes = []

    for attr in prim.GetAttributes():
        attributes.append({
            "name": attr.GetName(),
            "type": str(attr.GetTypeName()),
            "value": str(attr.Get())
        })

    relationships = []

    for relationship in prim.GetRelationships():
        relationships.append({
            "name": relationship.GetName(),
            "targets": [
                str(target)
                for target in relationship.GetTargets()
            ]
        })

    metadata = {
        "specifier": str(prim.GetSpecifier()),
        "type_name": prim.GetTypeName(),
        "is_active": prim.IsActive(),
        "is_defined": prim.IsDefined(),
        "is_instance": prim.IsInstance()
    }

    report = {
        "path": str(prim.GetPath()),
        "type": prim.GetTypeName(),
        "child_count": len(prim.GetChildren()),
        "metadata": metadata,
        "attributes": attributes,
        "relationships": relationships,
        "applied_schemas": prim.GetAppliedSchemas()
    }

    return report


# ----------------------------------
# 3. TEST INSPECTION
# ----------------------------------

test_paths = [
    "/World",
    "/World/Parent",
    "/World/Parent/Child",
    "/World/Parent/Child/Mesh"
]

for path in test_paths:

    print("\n" + "=" * 60)

    result = inspect_prim(stage, path)

    if result:
        print(json.dumps(result, indent=4))


# ----------------------------------
# 4. TEST INVALID PRIM
# ----------------------------------

print("\nINVALID PRIM TEST")

inspect_prim(stage, "/World/Car")


#OutputUSD Stage initialized successfully.

============================================================
# {
#     "path": "/World",
#     "type": "Xform",
#     "child_count": 1,
#     "metadata": {
#         "specifier": "Sdf.SpecifierDef",
#         "type_name": "Xform",
#         "is_active": true,
#         "is_defined": true,
#         "is_instance": false
#     },
#     "attributes": [
#         {
#             "name": "purpose",
#             "type": "token",
#             "value": "default"
#         },
#         {
#             "name": "visibility",
#             "type": "token",
#             "value": "inherited"
#         },
#         {
#             "name": "xformOpOrder",
#             "type": "token[]",
#             "value": "None"
#         }
#     ],
#     "relationships": [
#         {
#             "name": "proxyPrim",
#             "targets": []
#         }
#     ],
#     "applied_schemas": []
# }

# ============================================================
# {
#     "path": "/World/Parent",
#     "type": "Xform",
#     "child_count": 1,
#     "metadata": {
#         "specifier": "Sdf.SpecifierDef",
#         "type_name": "Xform",
#         "is_active": true,
#         "is_defined": true,
#         "is_instance": false
#     },
#     "attributes": [
#         {
#             "name": "purpose",
#             "type": "token",
#             "value": "default"
#         },
#         {
#             "name": "visibility",
#             "type": "token",
#             "value": "inherited"
#         },
#         {
#             "name": "xformOp:rotateXYZ",
#             "type": "float3",
#             "value": "(0, 0, 0)"
#         },
#         {
#             "name": "xformOp:scale",
#             "type": "float3",
#             "value": "(1, 1, 1)"
#         },
#         {
#             "name": "xformOp:translate",
#             "type": "double3",
#             "value": "(10, 0, 0)"
#         },
#         {
#             "name": "xformOp:translate:pivot",
#             "type": "float3",
#             "value": "(0, 0, 0)"
#         },
#         {
#             "name": "xformOpOrder",
#             "type": "token[]",
#             "value": "[xformOp:translate, xformOp:translate:pivot, xformOp:rotateXYZ, xformOp:scale, !invert!xformOp:translate:pivot]"
#         }
#     ],
#     "relationships": [
#         {
#             "name": "proxyPrim",
#             "targets": []
#         }
#     ],
#     "applied_schemas": []
# }

# ============================================================
# {
#     "path": "/World/Parent/Child",
#     "type": "Xform",
#     "child_count": 1,
#     "metadata": {
#         "specifier": "Sdf.SpecifierDef",
#         "type_name": "Xform",
#         "is_active": true,
#         "is_defined": true,
#         "is_instance": false
#     },
#     "attributes": [
#         {
#             "name": "purpose",
#             "type": "token",
#             "value": "default"
#         },
#         {
#             "name": "visibility",
#             "type": "token",
#             "value": "inherited"
#         },
#         {
#             "name": "xformOp:rotateXYZ",
#             "type": "float3",
#             "value": "(0, 0, 0)"
#         },
#         {
#             "name": "xformOp:scale",
#             "type": "float3",
#             "value": "(1, 1, 1)"
#         },
#         {
#             "name": "xformOp:translate",
#             "type": "double3",
#             "value": "(0, 5, 0)"
#         },
#         {
#             "name": "xformOp:translate:pivot",
#             "type": "float3",
#             "value": "(0, 0, 0)"
#         },
#         {
#             "name": "xformOpOrder",
#             "type": "token[]",
#             "value": "[xformOp:translate, xformOp:translate:pivot, xformOp:rotateXYZ, xformOp:scale, !invert!xformOp:translate:pivot]"
#         }
#     ],
#     "relationships": [
#         {
#             "name": "proxyPrim",
#             "targets": []
#         }
#     ],
#     "applied_schemas": []
# }

# ============================================================
# {
#     "path": "/World/Parent/Child/Mesh",
#     "type": "Cube",
#     "child_count": 0,
#     "metadata": {
#         "specifier": "Sdf.SpecifierDef",
#         "type_name": "Cube",
#         "is_active": true,
#         "is_defined": true,
#         "is_instance": false
#     },
#     "attributes": [
#         {
#             "name": "doubleSided",
#             "type": "bool",
#             "value": "False"
#         },
#         {
#             "name": "extent",
#             "type": "float3[]",
#             "value": "[(-1, -1, -1), (1, 1, 1)]"
#         },
#         {
#             "name": "orientation",
#             "type": "token",
#             "value": "rightHanded"
#         },
#         {
#             "name": "primvars:displayColor",
#             "type": "color3f[]",
#             "value": "None"
#         },
#         {
#             "name": "primvars:displayOpacity",
#             "type": "float[]",
#             "value": "None"
#         },
#         {
#             "name": "purpose",
#             "type": "token",
#             "value": "default"
#         },
#         {
#             "name": "size",
#             "type": "double",
#             "value": "2.0"
#         },
#         {
#             "name": "visibility",
#             "type": "token",
#             "value": "inherited"
#         },
#         {
#             "name": "xformOp:rotateXYZ",
#             "type": "float3",
#             "value": "(0, 0, 0)"
#         },
#         {
#             "name": "xformOp:scale",
#             "type": "float3",
#             "value": "(1, 1, 1)"
#         },
#         {
#             "name": "xformOp:translate",
#             "type": "double3",
#             "value": "(0, 0, 0)"
#         },
#         {
#             "name": "xformOp:translate:pivot",
#             "type": "float3",
#             "value": "(0, 0, 0)"
#         },
#         {
#             "name": "xformOpOrder",
#             "type": "token[]",
#             "value": "[xformOp:translate, xformOp:translate:pivot, xformOp:rotateXYZ, xformOp:scale, !invert!xformOp:translate:pivot]"
#         }
#     ],
#     "relationships": [
#         {
#             "name": "proxyPrim",
#             "targets": []
#         }
#     ],
#     "applied_schemas": []
# }

# INVALID PRIM TEST
# Prim not found: /World/Car
# -- 1 ---------------------------------------------------------------------------