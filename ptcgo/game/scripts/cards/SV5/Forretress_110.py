from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b1757be8-97f5-5326-8a72-dad91d0544ef",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Forretress.Name",
    display_name="Forretress",
    searchable_by=["Forretress", "Stage 1", "Forretress"],
    subtypes=["Stage 1"],
    collector_number=110,
    set_code="SV5",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pineco.Name",
    family_id=204,
    abilities=[
        Attack(
            title="Spike Cannon",
            game_text="Flip 3 coins. This attack does 30 damage for each heads.",
            cost={PokemonTypes.METAL: 1},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Steel Tackle",
            game_text="This Pok\u00e9mon also does 40 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
            effect=unimplemented,
        ),
    ],
)