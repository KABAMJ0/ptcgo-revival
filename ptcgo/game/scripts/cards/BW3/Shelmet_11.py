from ptcgo.game.card_effects.attacks_common import named_in_play
from ptcgo.game.content.definitions import evolves_from
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

_PARTNER_IN_PLAY = named_in_play("Karrablast", side="both")


async def _mysterious_evolution(ctx):
    """With the partner in play, search the deck for the card that evolves
    directly from this Pokemon and put it onto this Pokemon (an evolution)."""
    if not _PARTNER_IN_PLAY(ctx):
        return
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
    guid="489f3fbd-b612-5b4a-9a1b-2d90187bd979",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shelmet.Name",
    display_name="Shelmet",
    searchable_by=["Shelmet", "Basic", "Shelmet"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="BW3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=616,
    abilities=[
        Attack(
            title="Mysterious Evolution",
            game_text="If Karrablast is in play, search your deck for a card that evolves from this Pok\u00e9mon and put it onto this Pok\u00e9mon. (This counts as evolving this Pok\u00e9mon.) Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_mysterious_evolution,
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)