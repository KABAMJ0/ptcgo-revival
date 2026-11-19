from ptcgo.game.card_effects.attacks_common import flip_or_nothing
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_or_nothing

card = PokemonCardDef(
    guid="1161717f-d8e5-5a9c-accb-8fc104efbe80",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoran.Name",
    display_name="Nidoran ♂",
    searchable_by=["Nidoran \u2642", "Basic", "Nidoran"],
    subtypes=["Basic"],
    collector_number=72,
    set_code="PL2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=32,
    abilities=[
        Attack(
            title="Leer",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon can't attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Horn Hazard",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=flip_or_nothing(),
        ),
    ],
)