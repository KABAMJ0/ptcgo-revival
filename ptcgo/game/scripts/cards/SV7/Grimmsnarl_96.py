from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bbd0f52f-6fe3-512b-8e7c-e4a4727844c1",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grimmsnarl.Name",
    display_name="Grimmsnarl",
    searchable_by=["Grimmsnarl", "Stage 2", "Grimmsnarl"],
    subtypes=["Stage 2"],
    collector_number=96,
    set_code="SV7",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Morgrem.Name",
    family_id=859,
    abilities=[
        Attack(
            title="Goad 'n' Grab",
            game_text="Switch out your opponent's Active Pok\u00e9mon to the Bench. (Your opponent chooses the new Active Pok\u00e9mon.) If you do, this attack does 160 damage to the new Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Knuckle Sandwich",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=unimplemented,
        ),
    ],
)