from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bddc8102-8e12-51b4-9d9e-fe56dc4ab739",
    key="SWSH12PT5GG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DeoxysVMAX.Name",
    display_name="Deoxys VMAX",
    searchable_by=["Deoxys VMAX", "VMAX", "DeoxysVMAX"],
    subtypes=["VMAX"],
    collector_number=45,
    set_code="SWSH12PT5GG",
    rarity=Rarities.RareHoloVMAX,
    hp=330,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DeoxysV.Name",
    family_id=386,
    abilities=[
        Ability(
            title="Protective DNA",
            game_text="All of your Pok\u00e9mon take 30 less damage from attacks from your opponent's Pok\u00e9mon VSTAR (after applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Max Drain",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=unimplemented,
        ),
    ],
)