from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="81a57251-9148-5989-827d-cb50b9b91a91",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skiploom.Name",
    display_name="Skiploom",
    searchable_by=["Skiploom", "Stage 1", "Skiploom"],
    subtypes=["Stage 1"],
    collector_number=65,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hoppip.Name",
    family_id=187,
    abilities=[
        Ability(
            title="Cotton Balloon",
            game_text="If Skiploom has any Grass Energy attached to it, any damage done to Skiploom by attacks from your opponent's Evolved Pok\u00e9mon is reduced by 20 (after applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="U-turn",
            game_text="Switch Skiploom with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=unimplemented,
        ),
    ],
)