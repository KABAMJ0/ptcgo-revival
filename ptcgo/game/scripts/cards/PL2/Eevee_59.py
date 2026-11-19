from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, evolves_from_chain
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand


def _evolves_from_eevee(card):
    """A card whose evolution line takes it from Eevee (Flareon, Vaporeon, ...)."""
    return any(name.lower() == "eevee" for name in evolves_from_chain(card.archetype_id))

card = PokemonCardDef(
    guid="1d6de8d8-d812-5a98-912e-5653ba67713c",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    display_name="Eevee",
    searchable_by=["Eevee", "Basic", "Eevee"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="PL2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Attack(
            title="Signs of Evolution",
            game_text="Search your deck for up to 2 cards that evolve from Eevee, show them to your opponent, and put them into your hand. Shuffle your deck afterward.",
            cost={},
            effect=search_to_hand(_evolves_from_eevee, count=2, minimum=0, reveal=True),
        ),
        Attack(
            title="Bounce",
            game_text="Switch Eevee with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)