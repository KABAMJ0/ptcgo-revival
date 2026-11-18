from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8cbf43d5-bb9d-552f-8233-e0a0d52d2aa8",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Farigirafex.Name",
    display_name="Farigiraf ex",
    searchable_by=["Farigiraf ex", "Stage 1", "Tera", "ex", "Farigirafex"],
    subtypes=["Stage 1", "Tera", "ex"],
    collector_number=194,
    set_code="SV5",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Girafarig.Name",
    family_id=203,
    abilities=[
        Ability(
            title="Armor Tail",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from your opponent's Basic Pok\u00e9mon ex.",
            effect=unimplemented,
        ),
        Attack(
            title="Dirty Beam",
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=unimplemented,
        ),
    ],
)