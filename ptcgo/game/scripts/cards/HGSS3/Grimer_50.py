from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.passives_common import raise_defender_retreat_cost_next_turn
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5fe47fcd-9113-55ca-8f7f-2f8964e503a5",
    key="HGSS3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grimer.Name",
    display_name="Grimer",
    searchable_by=["Grimer", "Basic", "Grimer"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="HGSS3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=88,
    abilities=[
        Attack(
            title="Sticky Liquid",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon's Retreat Cost is Colorless more.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=raise_defender_retreat_cost_next_turn(1),
        ),
        Attack(
            title="Sludge Toss",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
