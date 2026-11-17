from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3395e0ca-2210-59d5-8edb-e12be8556bbf",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seismitoad.Name",
    display_name="Seismitoad",
    searchable_by=["Seismitoad", "Stage 2", "Seismitoad"],
    subtypes=["Stage 2"],
    collector_number=105,
    set_code="ZSV10PT5",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Palpitoad.Name",
    family_id=535,
    abilities=[
        Attack(
            title="Round",
            game_text="This attack does 70 damage for each of your Pok\u00e9mon in play that has the Round attack.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Hyper Voice",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=160,
        ),
    ],
)