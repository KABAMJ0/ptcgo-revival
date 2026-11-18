from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d711bc59-5b24-5108-9ad8-e8114a0ef8a4",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zoroark.Name",
    display_name="Zoroark",
    searchable_by=["Zoroark", "Stage 1", "Zoroark"],
    subtypes=["Stage 1"],
    collector_number=32,
    set_code="SV6PT5",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zorua.Name",
    family_id=570,
    abilities=[
        Attack(
            title="Illusory Hijacking",
            game_text="This attack does 60 damage for each of your opponent's Pok\u00e9mon ex and Pok\u00e9mon V in play.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Claw Slash",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
        ),
    ],
)