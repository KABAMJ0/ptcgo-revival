from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import energy_move_attack


card = PokemonCardDef(
    guid="919ae753-fcb6-5965-b628-3221c3def5b8",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golurk.Name",
    display_name="Golurk",
    searchable_by=["Golurk", "Stage 1", "Golurk"],
    subtypes=["Stage 1"],
    collector_number=35,
    set_code="XY7",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Golett.Name",
    family_id=622,
    abilities=[
        Ability(
            title="Double Type",
            game_text="As long as this Pok\u00e9mon is in play, it is Psychic and Fighting type.",
            effect=energy_move_attack(1),
        ),
        Attack(
            title="Superpower",
            game_text="You may do 40 more damage. If you do, this Pok\u00e9mon does 20 damage to itself.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)