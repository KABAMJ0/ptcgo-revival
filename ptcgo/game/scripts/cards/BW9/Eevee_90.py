from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.content.definitions import evolves_from


def _card_types(card) -> set:
    return set(card.get_attribute(AttrID.POKEMON_TYPES) or [])


async def signs_of_evolution(ctx):
    """Up to three Eevee evolutions of three different types, one per pick so
    the type restriction is enforced between them."""
    chosen, taken, seen_types = [], set(), set()
    for _ in range(3):
        def pickable(card):
            return (evolves_from(getattr(card, "archetype_id", None) or "", "Eevee")
                    and card.entity_id not in taken
                    and not (_card_types(card) & seen_types))

        picks = await ctx.search_deck(
            pickable, count=1, minimum=0,
            prompt="Choose a Pok\u00e9mon that evolves from Eevee of a new type")
        if not picks:
            break
        chosen.append(picks[0])
        taken.add(picks[0].entity_id)
        seen_types |= _card_types(picks[0])
    if chosen:
        await ctx.put_in_hand(chosen, reveal=True)
    await ctx.shuffle_deck()

card = PokemonCardDef(
    guid="c8e7168d-f809-5cf4-81f8-f9dc1bfed5e5",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    display_name="Eevee",
    searchable_by=["Eevee", "Basic", "Eevee"],
    subtypes=["Basic"],
    collector_number=90,
    set_code="BW9",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Attack(
            title="Signs of Evolution",
            game_text="Search your deck for 3 Pok\u00e9mon of different types that evolve from Eevee. Reveal them and put them into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=signs_of_evolution,
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)