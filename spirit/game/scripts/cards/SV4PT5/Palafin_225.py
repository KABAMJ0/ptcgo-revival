from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f1342128-6aa1-51a4-bb30-db4bdb918b0b",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palafin.Name",
    display_name="Palafin",
    searchable_by=["Palafin", "Stage 1", "Palafin"],
    subtypes=["Stage 1"],
    collector_number=225,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Finizen.Name",
    family_id=963,
    abilities=[
        Attack(
            title="Jet Punch",
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Justice Kick",
            game_text="If this Pok\u00e9mon didn't move from the Bench to the Active Spot this turn, this attack does nothing.",
            cost={PokemonTypes.WATER: 2},
            damage=210,
            effect=unimplemented,
        ),
    ],
)