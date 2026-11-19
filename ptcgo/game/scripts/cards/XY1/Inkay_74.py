from ptcgo.game.attributes import AttrID
from ptcgo.game.content.definitions import Triggers, evolves_from
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

def _is_confused(board, player_id, pokemon) -> bool:
    return "Confused" in (pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])


async def _upside_down_evolution(ctx):
    """While Confused: search the deck for the card that evolves directly from
    this Pokemon and put it onto this Pokemon."""
    pokemon = ctx.attacker
    if pokemon is None:
        return
    logic_name = pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
    if not logic_name:
        return
    stage = pokemon.get_attribute(AttrID.STAGE)

    def _direct_evolution(card):
        if not evolves_from(getattr(card, "archetype_id", None) or "", logic_name):
            return False
        return stage is None or card.get_attribute(AttrID.STAGE) == stage + 1

    picks = await ctx.search_deck(_direct_evolution, count=1, minimum=0,
                                  prompt="Choose an Evolution card")
    if picks:
        await ctx.evolve_pokemon(pokemon, picks[0])
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="ed0be64c-c5c0-58ef-8f90-847e563c0c78",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name",
    display_name="Inkay",
    searchable_by=["Inkay", "Basic", "Inkay"],
    subtypes=["Basic"],
    collector_number=74,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=686,
    abilities=[
        Ability(
            title="Upside-Down Evolution",
            game_text="Once during your turn, (before your attack), if this Pok\u00e9mon is Confused, you may search your deck for a card that evolves from this Pok\u00e9mon and put it onto this Pok\u00e9mon. (This counts as evolving this Pok\u00e9mon.) Shuffle your deck afterward.",
            trigger=Triggers.ON_EVOLVE,
            condition=_is_confused,
            effect=_upside_down_evolution,
        ),
        Attack(
            title="Confusion Wave",
            game_text="Both Active Pok\u00e9mon are now Confused.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=condition_attack(SpecialConditions.CONFUSED, both_actives=True),
        ),
    ],
)